import argparse
import serial
from serial.tools import list_ports
import sys
import usb_cmds
import pyvisa


class SCPI_funcitnoal:
    SCPILookUpTable = {"*TST?":"selftest", "PROGram:SELected:STATe PAUSe":"pause", "PROGram:SELected:STATe CONTinue":"resume", "BAND:RES":"rbw"}
    def __init__(self):
        self.VID = 0x0483 # Version ID
        self.PID = 0x5740 # Product ID
        self.rm = pyvisa.ResourceManager()
        print(self.rm.list_resources())
        self.inst = self.rm.open_resource('ASRL/dev/ttyACM0::INSTR')
        self.inst.baud_rate = 115200
        self.inst.read_termination = "\r"
        self.inst.write_termination = "\r"

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

    def convertSCPItoUSB(self, command: str, args: list) -> str:
        if len(args) == 0: return self.SCPILookUpTable[command]
        else: return self.SCPILookUpTable[command] + " TODO: add arguments"


    def write(self, command) -> None:
        self.inst.write(command)


    def read(self) -> str:
        return self.inst.read()

