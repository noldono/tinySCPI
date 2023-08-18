import argparse
import time

import numpy as np
import serial
from serial.tools import list_ports
import sys
import csv
import scpi_lookup_dict
import struct
import numpy
from PIL import Image
import datetime


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

    def getDevice(self) -> str:
        # In the future, append the device to a list to enable the use of multiple tinySA's
        device_list = list_ports.comports()
        for device in device_list:
            if device.vid == self.VID and device.pid == self.PID:
                return device.device
        raise OSError("device not found")

    '''
    Create tinySA usb command, given the valid command and arguments.
    '''

    def convertSCPItoUSB(self, command: str, args: list) -> str:
        print(command)
        usb_cmd: str = scpi_lookup_dict.SCPILookUpTable[command]
        usb_cmd += ' '
        for arg in args:
            usb_cmd += str(arg)
            usb_cmd += ' '

        print(usb_cmd)
        return usb_cmd

    def send(self, command) -> None:
        try:
            device = self.getDevice()
            with serial.Serial(device, timeout=1) as tinySA_device:
                tinySA_device.write(command.encode() + self.cr)
                echo = tinySA_device.read_until(command.encode() + self.crlf)
                echo = tinySA_device.read_until(self.crlf + self.prompt)
                decoded = echo[:-len(self.crlf + self.prompt)].decode()
                return decoded
        except Exception as e:
            return f"Error sending commmand '{command}': {str(e)}"

    # Taken from https://github.com/Ho-Ro/nanovna-tools/blob/main/nanovna_capture.py
    def takeScreenshot(self, filename: str = ""):
        try:
            device = self.getDevice()
            with serial.Serial(device, timeout=1) as tinySA_device:
                tinySA_device.write(b'pause\r')  # stop screen update
                echo = tinySA_device.read_until(b'pause' + self.crlf + self.prompt)  # wait for completion
                tinySA_device.write(b'capture\r')  # request screen capture
                echo = tinySA_device.read_until(b'capture' + self.crlf)  # wait for start of transfer
                captured_bytes = tinySA_device.read(2 * self.screen_width * self.screen_height)
                echo = tinySA_device.read_until(self.prompt)  # wait for cmd completion
            rgb565 = struct.unpack(f'>{self.screen_width * self.screen_height}H', captured_bytes)
            # convert to 32bit numpy array Rrrr.rGgg.gggB.bbbb -> 0000.0000.0000.0000.Rrrr.rGgg.gggB.bbbb
            rgb565_32 = numpy.array(rgb565, dtype=numpy.uint32)
            rgba8888 = 0xFF000000 + (
                    ((rgb565_32 & 0xF800) >> 8) + ((rgb565_32 & 0x07E0) << 5) + ((rgb565_32 & 0x001F) << 19))
            image = Image.frombuffer('RGBA', (self.screen_width, self.screen_height), rgba8888, 'raw', 'RGBA', 0, 1)
            file = filename or datetime.now().strftime(f'{self.device_name}_%Y%m%d_%H%M%S.png')
            try:
                image.save(filename)  # .. and save it to file (format according extension)
            except ValueError:  # unknown (or missing) exension
                image.save(filename + '.png')  # force PNG format
        except Exception as e:
            return f"Error sending capture command: {str(e)}"

    # Taken from https://github.com/Ho-Ro/nanovna-tools/blob/main/tinysa_scanraw.py
    def scanRaw(self, f_low: int, f_high: int, points: int, filename: str = "", verbose=None, rbw=0):
        try:
            device = self.getDevice()
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
            SCALE = 128
            dBm_power = raw_data / 32 - SCALE  # scale 0..4095 -> -128..-0.03 dBm
            return dBm_power
        except Exception as e:
            return f"Error sending capture command: {str(e)}"
