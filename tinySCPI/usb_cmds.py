import argparse
import serial
from serial.tools import list_ports
import sys

class USB_CMDS:
    def sendcommand(self, command) -> None:
        if self.serial is None:
            self.serial = serial.Serial(self.dev)
        self.serial.write(command.encode())
        self.serial.readline() # discard empty line

    def attenuate(self) -> None:
        # code goes here
        return ""

    def bulk(self):
        # code goes here
        return ""

    def calc(self):
        # code goes here
        return ""

    def caloutput(self):
        # code goes here
        return ""

    def capture(self):
        # code goes here
        return ""

    def clearconfig(self):
        # code goes here
        return ""

    def color(self):
        # code goes here
        return ""

    def correction(self):
        # code goes here
        return ""

    def dac(self):
        # code goes here
        return ""

    def data(self):
        # code goes here
        return ""

    def deviceid(self):
        # code goes here
        return ""

    def fill(self):
        # code goes here
        return ""

    def freq(self):
        # code goes here
        return ""

    def frequencies(self):
        # code goes here
        return ""

    def _if(self):
        # code goes here
        return ""

    def info(self):
        # code goes here
        return ""

    def help(self):
        # code goes here
        return ""

    def hop(self):
        # code goes here
        return ""

    def level(self):
        # code goes here
        return ""

    def levelchange(self):
        # code goes here
        return ""

    def leveloffset(self):
        # code goes here
        return ""

    def load(self):
        # code goes here
        return ""

    def marker(self):
        # code goes here
        return ""

    def mode(self):
        # code goes here
        return ""

    def modulation(self):
        # code goes here
        return ""

    def ext_gain(self):
        # code goes here
        return ""

    def output(self):
        # code goes here
        return ""

    def pause(self):
        # code goes here
        return ""

    def rbw(self):
        # code goes here
        return ""

    def recall(self):
        # code goes here
        return ""

    def refresh(self):
        # code goes here
        return ""

    def release(self):
        # code goes here
        return ""

    def reset(self):
        # code goes here
        return ""

    def resume(self):
        # code goes here
        return ""

    def save(self):
        # code goes here
        return ""

    def saveconfig(self):
        # code goes here
        return ""

    def scan(self):
        # code goes here
        return ""

    def scanraw(self):
        # code goes here
        return ""

    def selftest(self):
        # code goes here
        return ""

    def spur(self):
        # code goes here
        return ""

    def sweep(self):
        # code goes here
        return ""

    def sweeptime(self):
        # code goes here
        return ""

    def threads(self):
        # code goes here
        return ""

    def touch(self):
        # code goes here
        return ""

    def touchcal(self):
        # code goes here
        return ""

    def touchtest(self):
        # code goes here
        return ""

    def trace(self):
        # code goes here
        return ""

    def trigger(self):
        # code goes here
        return ""

    def vbat(self):
        # code goes here
        return ""

    def vbat_offset(self):
        # code goes here
        return ""

    def version(self):
        # code goes here
        return ""
