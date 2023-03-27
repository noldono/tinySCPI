import argparse
import serial
from serial.tools import list_ports
import sys
import pyvisa
import time


class SCPI_functional:
    SCPILookUpTable = {}
    def __init__(self):
        self.baudrate = 115200
        self.ser = serial.Serial('COM4', self.baudrate, timeout=1)


    # '''
    # args: self
    # desc: finds the tinySA device if it is connected
    # '''

    def write(self, command) -> None:
        command_bytes = (command + "\r\n").encode()

        self.ser.write(command_bytes)


    def read(self) -> str:
        time.sleep(0.1)
        response = self.ser.read_all()

        return response.decode()

    
    def get_id(self) -> str:
        # Call the Python function to get the instrument ID
        # ...
        self.write('info')
        multiline_string = self.read()
        
        # When 'info' is sent to tinySA, a long string is returned with many info. To just get the version: in that string:
        for line in multiline_string.splitlines():
            if "Version:" in line:
                version = line.split(":")[1].strip()
                break
        
        return version
    
    def get_version(self) -> str:
        # Call the Python function to get the instrument ID
        # ...
        self.write('version')
        response = self.read()

        words = response.split()
        new_string = ' '.join(words[1:-1])
        return new_string
    
    def get_battery(self) -> str:
        # Call the Python function to get the instrument ID
        # ...
        self.write('vbat')
        response = self.read()

        words = response.split()
        new_string = ' '.join(words[1:-1])
        return new_string
=======
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
    args: self, command, args(list)
    desc: it will take in a SCPI command, 
    '''

    def convertSCPItoUSB(self, command: str, args: list) -> str:
        if len(args) == 0:
            return scpi_lookup_dict.SCPILookUpTable[command]
        else:
            return scpi_lookup_dict.SCPILookUpTable[command] + " TODO: add arguments"

    def send(self, command) -> None:
        device = self.getDevice()
        with serial.Serial(device, timeout=1) as tinySA_device:
            tinySA_device.write(command.encode() + self.cr)
            echo = tinySA_device.read_until(command.encode() + self.crlf)
            echo = tinySA_device.read_until(self.crlf + self.prompt)
            return echo[:-len(self.crlf + self.prompt)].decode()
