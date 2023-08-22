import time

import tinySCPI
from threading import Event

def main():
    info = tinySCPI.userInput("CAPTure")
    tinySCPI.userInput("PROGram:SELected:STATe:RESUme")
if __name__=="__main__":
    main()