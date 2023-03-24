import argparse
import serial
from serial.tools import list_ports
import sys
import usb_cmds
import pyvisa


class SCPI_functional:
    SCPILookUpTable = {"*TST?":"selftest", "PROGram:SELected:STATe PAUSe":"pause", "PROGram:SELected:STATe CONTinue":"resume", "BAND:RES":"rbw", "*IDN?":"info"}
    def __init__(self):
        self.VID = 0x0483 # Version ID
        self.PID = 0x5740 # Product ID

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
        if len(args) == 0: return self.SCPILookUpTable[command]
        else: return self.SCPILookUpTable[command] + " TODO: add arguments"


    def send(self, command) -> None:
        device = self.getDevice()
        with serial.Serial(device, timeout=1) as tinySA_device:
            tinySA_device.write(command.encode() + self.cr)
            echo = tinySA_device.read_until(command.encode() + self.crlf)
            echo = tinySA_device.read_until(self.crlf + self.prompt)
            return echo[ :-len( self.crlf + self.prompt ) ].decode()

