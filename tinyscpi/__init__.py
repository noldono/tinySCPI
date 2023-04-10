import time

import tinySCPI
from threading import Event

def main():
    info = tinySCPI.userInput("SWEep:BEGin 200000000 350000000 290")
    print(info)
    #tinySCPI.userInput('PROGram:SELected:STATe CONTinue')
if __name__=="__main__":
    main()