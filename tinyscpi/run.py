import time

import tinyscpi
from tinyscpi import tinySCPI


def main():

    tinySCPI.user_input('TRIG:LVL -30.2')

    # tinySCPI.user_input('MEAS:HARM 10000')
    # tinySCPI.user_input('MEAS:OIP3 90 1200')

    # functional = tinyscpi.scpi_functional.SCPI_functional()
    # functional.convert_scpi_to_usb('MEAS:STH', [3, 3])
    # tinySCPI.user_input()
    # #print(tinySCPI.execute_from_file('C:\\Users\\black\\Desktop\\tinySCPI\\examples\\example_script.txt'))


if __name__ == "__main__":
    main()
