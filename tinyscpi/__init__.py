import time

import tinySCPI
from threading import Event

def main():
    tinySCPI.userInput("MEASure:TRIGger -140")
if __name__=="__main__":
    main()