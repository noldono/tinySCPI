import sys

def main():
    sys.path.insert(0,"./tinySCPI")
    from tinySCPI import tinySCPI
    input("TEST MODE\n")
    getMode = tinySCPI("MARKer:MODE?")
    print(getMode)

    input("TEST IDENTIFICATION\n")
    print(tinySCPI("*IDN?"))

    input("TEST RESET\n")
    tinySCPI(cmd="*RST")

if __name__ == "__main__":
    main()
