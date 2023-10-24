import time

import tinyscpi
from tinyscpi import tinySCPI


def main():

    tinySCPI.user_input('MEAS:AM 1000000 3000')
    tinySCPI.user_input('CONF:CAPT')


if __name__ == "__main__":
    main()
