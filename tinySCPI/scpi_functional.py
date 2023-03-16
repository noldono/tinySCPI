import argparse
import serial
from serial.tools import list_ports
import sys
import usb_cmds

class SCPI_funcitnoal:
    SCPILookUpTable = {}
    def __init__(self):
        self.a = 1
        self.VID = 0x0483 # Version ID
        self.PID = 0x5740 # Product ID
    '''
    args: self
    desc: finds the tinySA device if it is connected
    '''
    def getDevice(self) -> str:
        device_list = list_ports.comports()
        for device in device_list:
            if device.vid == self.VID and device.pid == self.PID:
                return device.device
        raise OSError("device not found")

    def convertSCPItoUSB(self, command) -> str:
        return ""

    def write(self, command) -> None:
        return None

    def read(self) -> str:
        return ""

