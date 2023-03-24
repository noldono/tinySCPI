import argparse
import serial
from serial.tools import list_ports
import sys
import usb_cmds
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
