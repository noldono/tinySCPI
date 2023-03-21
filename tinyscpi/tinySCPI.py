'''
This file contains all of the functions that will be available to the user of our library.
'''
from tinyscpi import scpi_functional
from tinyscpi import scpi_parser
def userInput(input)->str:
    parser = scpi_parser.SCPI_Parser()
    functional = scpi_functional.SCPI_funcitnoal()
    usb_str = functional.convertSCPItoUSB(input, [])
    functional.write(usb_str)
    return functional.read()

