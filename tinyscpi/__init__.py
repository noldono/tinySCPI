import tinySCPI
from threading import Event

def main():
    #Serial
    info = tinySCPI.debugInput('scan 1000000000 2000000000 5 3')

    #SCPI
    #info = tinySCPI.userInput("FREQuency:OFFSet low output")
    print(info)
    #tinySCPI.userInput('PROGram:SELected:STATe CONTinue')

if __name__=="__main__":
    main()