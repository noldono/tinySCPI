import numpy as np

from . import scpi_functional
from . import scpi_parser


def user_input(input_cmd: str) -> str:
    parser = scpi_parser.SCPI_Parser()
    functional = scpi_functional.SCPI_functional()
    cmd, args = parser.parse_command(input_cmd)
    usb_str = functional.convert_scpi_to_usb(cmd, args)
    return functional.send(usb_str)


def debug_input(input_cmd: str) -> str:
    functional = scpi_functional.SCPI_functional()
    return functional.send(input_cmd)


def execute_from_file(filepath: str) -> None:
    with open(filepath, "r") as file:
        list_of_cmds = []
        for line in file:
            list_of_cmds.append(line)
        for cmd in list_of_cmds:
            print(user_input(cmd.replace("\n", "")))
    file.close()


def capture(filename: str) -> str:
    functional = scpi_functional.SCPI_functional()
    functional.take_screenshot(filename)
    return f"Success, saved as {filename} in current directory"


def scan_raw_points(savedata: bool, start_freq: int, stop_freq: int, num_points: int) -> str:
    functional = scpi_functional.SCPI_functional()
    result = functional.scan_raw(start_freq, stop_freq, num_points)
    if savedata:
        np.savetxt('data.csv', result, delimiter=',', fmt='%.8f')
        print(f"Successfully saved data in current working directory as data.csv")

    return result
