import argparse
import serial
from serial.tools import list_ports
import sys
import pyvisa
import csv
import scpi_lookup_dict


class SCPI_functional:
    def __init__(self):
        self.VID = 0x0483  # Version ID
        self.PID = 0x5740  # Product ID

        # Variables for using pySerial
        self.cr = b'\r'
        self.lf = b'\n'
        self.crlf = self.cr + self.lf
        self.prompt = b'ch> '

        # # Variables for using pyVISA
        # self.rm = pyvisa.ResourceManager()
        # print(self.rm.list_resources())
        # self.inst = self.rm.open_resource('ASRL/dev/ttyACM0::INSTR')
        # self.inst.baud_rate = 115200
        # self.inst.read_termination = "\r"
        # self.inst.write_termination = "\r"

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
        usb_cmd: str = scpi_lookup_dict.SCPILookUpTable[command]
        for arg in args:
            usb_cmd += str(arg)
            usb_cmd += ' '

        return usb_cmd

    def send(self, command) -> None:
        device = self.getDevice()
        with serial.Serial(device, timeout=1) as tinySA_device:
            tinySA_device.write(command.encode() + self.cr)
            echo = tinySA_device.read_until(command.encode() + self.crlf)
            echo = tinySA_device.read_until(self.crlf + self.prompt)
            return echo[:-len(self.crlf + self.prompt)].decode()
