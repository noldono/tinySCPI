import time

import tinyscpi
from tinyscpi import tinySCPI


def main():
    start_freq = 90000000
    stop_freq = 105000000

    tinySCPI.user_input(f'FREQ:START {start_freq}')
    tinySCPI.user_input(f'FREQ:STOP {stop_freq}')

    while True:
        data = tinySCPI.scan_raw_points(False, start_freq, stop_freq, 290)
        for n in data:
            if int(n) > -55:
                time.sleep(2)
                tinySCPI.user_input('CONF:CAPT')
                return


if __name__ == "__main__":
    main()


