'''
This file contains all of the functions that will be available to the user of our library.
'''

import time

def tinySCPI(cmd: str):
    if cmd == "MARK:MODE" or cmd == "MARKer:MODE?":
        return "Current Mode = LOW INPUT\n"

    if cmd == "*IDN?":
        return "TinySA S/N 2213567\n"

    if cmd == "*RST":
        print("Resetting DEV: TinySA 2213567")
        time.sleep(0.2)
        print("\tDeleting stored configurations...")
        time.sleep(0.6)
        print("\tDefaulting to LOW INPUT...")
        time.sleep(0.1)
        print("\tOverwriting TRIGGER to AUTO...")
        time.sleep(0.1)
        print("Reset Complete!")

    return "Invalid SCPI Command.\n"

def userInput(self, input)->str:
    return ""

