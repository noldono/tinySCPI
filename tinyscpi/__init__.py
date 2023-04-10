import time

import tinySCPI
from threading import Event

def main():
    #placeholder
    info = tinySCPI.userInput("SYSTem:MODE low output")
    print(info)
    info = tinySCPI.userInput("SOURce:POWer:LEVel:IMMediate:AMPLitude:OFFset -30")
    print(info)
    #tinySCPI.userInput('PROGram:SELected:STATe CONTinue')
if __name__=="__main__":
    main()