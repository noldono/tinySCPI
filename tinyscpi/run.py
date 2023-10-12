import time

from . import tinySCPI


def main():
    print(tinySCPI.executeFromFile('script.txt'))


if __name__ == "__main__":
    main()
