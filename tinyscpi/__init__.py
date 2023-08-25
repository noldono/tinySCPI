import time

import tinySCPI
from threading import Event

def main():
    info = tinySCPI.userInput("SYSTem:THREADs?")
    print(info)
if __name__=="__main__":
    main()