import struct
import sys
import time
from . import helpers
from datetime import datetime
from .dictionaries import digit_mappings_dict

import numpy
import numpy as np
import serial
from PIL import Image
from serial.tools import list_ports


class SCPI_functional:
    def __init__(self):
        self.VID = 0x0483  # Version ID
        self.PID = 0x5740  # Product ID

        # Variables for using pySerial
        self.cr = b'\r'
        self.lf = b'\n'
        self.crlf = self.cr + self.lf
        self.prompt = b'ch> '
        self.screen_width = 320
        self.screen_height = 240
        self.device_name = "TinySA"

    '''
    args: self
    desc: finds the tinySA device if it is connected
    '''
    def get_device(self) -> str:
        # In the future, append the device to a list to enable the use of multiple tinySA's
        device_list = list_ports.comports()
        for device in device_list:
            if device.vid == self.VID and device.pid == self.PID:
                return device.device
        raise OSError("device not found")

    '''
    args: self, command, args
        command: SCPI command in str format
        args: SCPI command arguments/parameters in list format
    desc: Create tinySA usb command, given the valid command and arguments.
    '''
    def convert_scpi_to_usb(self, command: str, args: list):
        from .dictionaries import scpi_lookup_dict
        usb_cmd = scpi_lookup_dict.SCPILookUpTable[command]

        if callable(usb_cmd):
            if 'MEAS' in command:
                # MEASure subsystem commands require arguments to be passed to their functions
                usb_cmd(self, args)
            else:
                usb_cmd(self)

            return usb_cmd

        if "[src]" in usb_cmd or "[dst]" in usb_cmd:
            usb_cmd = helpers.replace_src_dst(usb_cmd, args)
            print("Running" + usb_cmd)
            return usb_cmd

        usb_cmd += ' '
        for arg in args:
            if isinstance(arg, bool):
                if arg:
                    arg = "on"
                else:
                    arg = "off"

            usb_cmd += str(arg)
            usb_cmd += ' '

        print("Running " + usb_cmd)
        return usb_cmd.strip()


    def send(self, command) -> str:
        if not callable(command):
            try:
                device = self.get_device()
                with serial.Serial(device, timeout=1) as tinySA_device:
                    tinySA_device.write(command.encode() + self.cr)
                    _ = tinySA_device.read_until(command.encode() + self.crlf)
                    echo = tinySA_device.read_until(self.crlf + self.prompt)
                    decoded = echo[:-len(self.crlf + self.prompt)].decode()
                    return decoded
            except Exception as e:
                return f"Error sending commmand '{command}': {str(e)}"

    # From https://github.com/Ho-Ro/nanovna-tools/blob/main/nanovna_capture.py
    def take_screenshot(self):
        try:
            device = self.get_device()
            with serial.Serial(device, timeout=1) as tinySA_device:
                tinySA_device.write(b'pause\r')  # stop screen update
                _ = tinySA_device.read_until(b'pause' + self.crlf + self.prompt)  # wait for completion
                tinySA_device.write(b'capture\r')  # request screen capture
                _ = tinySA_device.read_until(b'capture' + self.crlf)  # wait for start of transfer
                captured_bytes = tinySA_device.read(2 * self.screen_width * self.screen_height)
                _ = tinySA_device.read_until(self.prompt)  # wait for cmd completion
            rgb565 = struct.unpack(f'>{self.screen_width * self.screen_height}H', captured_bytes)
            # convert to 32bit numpy array Rrrr.rGgg.gggB.bbbb -> 0000.0000.0000.0000.Rrrr.rGgg.gggB.bbbb
            rgb565_32 = numpy.array(rgb565, dtype=numpy.uint32)
            rgba8888 = 0xFF000000 + (
                    ((rgb565_32 & 0xF800) >> 8) + ((rgb565_32 & 0x07E0) << 5) + ((rgb565_32 & 0x001F) << 19))
            image = Image.frombuffer('RGBA', (self.screen_width, self.screen_height), rgba8888, 'raw', 'RGBA', 0, 1)
            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            image.save(f"tinysa_capture_{current_datetime}.png")
        except Exception as e:
            print(str(e))
            return f"Error sending capture command: {str(e)}"

    # From https://github.com/Ho-Ro/nanovna-tools/blob/main/tinysa_scanraw.py
    def scan_raw(self, f_low: int, f_high: int, points: int, verbose=None, rbw=0):
        try:
            device = self.get_device()
            with serial.Serial(device, timeout=1) as tinySA:
                tinySA.timeout = 1
                while tinySA.inWaiting():
                    tinySA.read_all()  # keep the serial buffer clean
                    time.sleep(0.1)

                span_k = (f_high - f_low) / 1e3
                if 0 == rbw:  # calculate from scan range and steps
                    rbw_k = span_k / points  # RBW / kHz
                else:
                    rbw_k = rbw / 1e3

                if rbw_k < 3:
                    rbw_k = 3
                elif rbw_k > 600:
                    rbw_k = 600

                rbw_command = f'rbw {int(rbw_k)}\r'.encode()
                tinySA.write(rbw_command)
                tinySA.read_until(b'ch> ')  # skip command echo and prompt

                # set timeout accordingly - can be very long - use a heuristic approach
                timeout = int(span_k / (rbw_k * rbw_k) + points / 1e3 + 5)
                tinySA.timeout = timeout

                if verbose:
                    sys.stderr.write(f'frequency step: {int(span_k / (points - 1))} kHz\n')
                    sys.stderr.write(f'RBW: {int(rbw_k)} kHz\n')
                    sys.stderr.write(f'serial timeout: {timeout} s\n')

                scan_command = f'scanraw {int(f_low)} {int(f_high)} {int(points)}\r'.encode()
                tinySA.write(scan_command)
                tinySA.read_until(b'{')  # skip command echoes
                raw_data = tinySA.read_until(b'}ch> ')
                tinySA.write('rbw auto\r'.encode())  # switch to auto RBW for faster tinySA screen update

            raw_data = struct.unpack('<' + 'xH' * points, raw_data[:-5])  # ignore trailing '}ch> '
            raw_data = np.array(raw_data, dtype=np.uint16)
            # tinySA:  SCALE = 128
            # tinySA4: SCALE = 174
            scale = 128
            dBm_power = raw_data / 32 - scale  # scale 0..4095 -> -128..-0.03 dBm
            return dBm_power
        except Exception as e:
            return f"Error sending capture command: {str(e)}"

    def selftest(self):
        try:
            self.send('selftest 0')

            time.sleep(30)  # Test can take up to 30 seconds to complete

            self.send('touch 0 0')
            self.send('release')
        except Exception as e:
            return f"Error sending selftest command: {str(e)}"

    '''
    MEASure subsystem pseudo-command functions
    '''
    '''
    desc: pseudo-command function for MEASure:HARMonic
    '''
    def MEASure_OFF(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 10')
        self.send('release')

    '''
    desc: pseudo-command function for MEASure:HARMonic
    '''
    def MEASure_HARMonic(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 35')
        self.send('release')
        self._enter_digits_on_screen(args)

    '''
    desc: pseudo-command function for MEASure:OIP3
    '''
    def MEASure_OIP3(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 60')
        self.send('release')
        print(self._enter_digits_on_screen(args))

    '''
    desc: pseudo-command function for MEASure:PhaseNOISe
    '''
    def MEASure_PhaseNOISe(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 90')
        self.send('release')
        print(self._enter_digits_on_screen(args))

    '''
    desc: pseudo-command function for MEASure:SNR
    '''
    def MEASure_SNR(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 120')
        self.send('release')
        self._enter_digits_on_screen(args)

    '''
    desc: pseudo-command function for MEASure:3DB
    '''
    def MEASure_3DB(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 150')
        self.send('release')

    '''
    desc: pseudo-command function for MEASure:AM
    '''
    def MEASure_AM(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 180')
        self.send('release')
        self.send('touch 320 10')
        self.send('release')
        print(self._enter_digits_on_screen(args))

    '''
    desc: pseudo-command function for MEASure:FM
    '''
    def MEASure_FM(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 180')
        self.send('release')
        self.send('touch 320 40')
        self.send('release')
        print(self._enter_digits_on_screen(args))

    '''
    desc: pseudo-command function for MEASure:THD
    '''
    def MEASure_THD(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 180')
        self.send('release')
        self.send('touch 320 80')
        self.send('release')
    '''
    desc: pseudo-command function for MEASure:CHPOW
    '''
    def MEASure_CHPOW(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 180')
        self.send('release')
        self.send('touch 320 110')
        self.send('release')
        print(self._enter_digits_on_screen(args))

    '''
    desc: pseudo-command function for MEASure:LINEar
    '''
    def MEASure_LINEar(self, args):
        self.send('touch 300 100')
        self.send('release')
        self.send('touch 320 160')
        self.send('release')
        self.send('touch 320 180')
        self.send('release')
        self.send('touch 320 150')
        self.send('release')

    '''
    desc: pseudo-command function for MEASure:LINEar
    '''
    def _enter_digits_on_screen(self, args) -> None:
        command_sequence = []
        for arg in args:
            shortened_freq = helpers.shorten_frequency(arg)
            for c in shortened_freq:
                command_sequence.append(digit_mappings_dict.commands[c])
                command_sequence.append('release')

            # If the arg is just in Hz, press x1 to go to the next screen
            if str(arg) == shortened_freq:
                command_sequence.append(digit_mappings_dict.commands['x1'])
                command_sequence.append('release')

        for command in command_sequence:
            self.send(command)
