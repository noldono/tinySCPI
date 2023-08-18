import time

import tinySCPI
from threading import Event

def main():
    info = tinySCPI.scanRawPoints(True)
    print(info)
if __name__=="__main__":
    main()