'''
This file contains all of the functions that will be available to the user of our library.
'''
import scpi_functional
import scpi_parser

def userInput(input)->str:
    parser = scpi_parser.SCPI_Parser()
    functional = scpi_functional.SCPI_functional()
    # Consider adding an args checking function here so that we don't waste resources trying to send an invalid command
    usb_str = functional.convertSCPItoUSB(input, [])
    return functional.send(usb_str)

