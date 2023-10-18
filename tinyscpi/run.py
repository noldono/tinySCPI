import time

from . import tinySCPI


def main():
    print(tinySCPI.execute_from_file('script.txt'))


if __name__ == "__main__":
    main()
