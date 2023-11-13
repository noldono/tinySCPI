import time
import random 

from . import tinySCPI
from . import scpi_functional 

# Prequisite: 30 dB attenuator on output, load device, tinySA updated firmware 
# Program that randomly generates an unmodulated square wave output between 391 MHz and 393 MHz in 60 KHz steps
# Note that there is a delay between switching frequencies due to serial transmission delays.

def main():
    # Sets tinySA to High Output Mode
    tinySCPI.userInput("SYST:MODE:HIGH:OUT")
    # start at 392 MHz
    tinySCPI.userInput("FREQ:START 392000000")
    # Sets external gain to -30 dBm
    tinySCPI.userInput("LVL:XGAIN -30")
    # sets device output power to -35 dBm. This will give us -30 + -35 = -65 dBm of effective output, without load gain calculations
    tinySCPI.userInput("OUT:LEV -35")
    # turn on output 
    tinySCPI.userInput("OUT:ON")

    for i in range(300):
        # Choose random frequency
        randomUHF = random.randrange(391000000, 393000000, 60000)
        # hop to random frequency
        tinySCPI.userInput(f"FREQ:START {randomUHF}")
    
    # after loop ends, turn off tinySA.
    tinySCPI.userInput("OUT:OFF")

if __name__ == "__main__":
    main()