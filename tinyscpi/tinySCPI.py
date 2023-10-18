'''
This file contains all of the functions that will be available to the user of our library.
'''
import numpy as np

from . import scpi_functional
from . import scpi_parser


def userInput(input: str) -> str:
    parser = scpi_parser.SCPI_Parser()
    functional = scpi_functional.SCPI_functional()
    # Consider adding an args checking function here so that we don't waste resources trying to send an invalid command
    cmd, args = parser.parse_command(input)
    usb_str = functional.convert_scpi_to_usb(cmd, args)
    return functional.send(usb_str)


def debugInput(input: str) -> str:
    functional = scpi_functional.SCPI_functional()
    return functional.send(input)


def executeFromFile(filepath: str) -> None:
    with open(filepath, "r") as file:
        list_of_cmds = []
        for line in file:
            list_of_cmds.append(line)
        for cmd in list_of_cmds:
            print(userInput(cmd.replace("\n", "")))
    file.close()

def capture(filename: str) -> str:
    functional = scpi_functional.SCPI_functional()
    functional.take_screenshot(filename)
    return f"Success, saved as {filename} in current directory"


def scanRawPoints(savedata: bool) -> str:
    functional = scpi_functional.SCPI_functional()
    result = functional.scan_raw(0, 350000000, 200)
    if savedata:
        np.savetxt('data.csv', result, delimiter=',', fmt='%.8f')
        print(f"Successfully saved data in current working directory as data.csv")

    return result
