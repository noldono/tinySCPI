from . import tinySCPI
import numpy as np

from . import scpi_functional
from . import scpi_parser

def main():
    print(tinySCPI.userInput('SENS:CORR low 1 12345 9999'))
    # functional = scpi_functional.SCPI_functional()
    # print(functional.send('correction low 0 123450 99'))

if __name__ == "__main__":
    main()
