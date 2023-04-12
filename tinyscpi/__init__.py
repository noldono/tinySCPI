import time

import tinySCPI
from threading import Event

def main():
    # info = tinySCPI.userInput("MEASure:SCAN:RAW:START 0 240000000 290")
    # print(info)
    info = tinySCPI.scanRawPoints()
    print(info)
if __name__=="__main__":
    main()