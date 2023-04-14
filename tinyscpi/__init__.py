import tinySCPI
from threading import Event

def main():
    #Serial
    info = tinySCPI.debugInput('trace')

    #SCPI
    #info = tinySCPI.userInput("FREQuency:OFFSet low output")
    print(info)
    #tinySCPI.userInput('PROGram:SELected:STATe CONTinue')

if __name__=="__main__":
    main()