import tinySCPI
from threading import Event

def main():
    #placeholder
    info = tinySCPI.userInput('*IDN?')
    print(info)
    #Event().wait(10)
    #tinySCPI.userInput('PROGram:SELected:STATe CONTinue')
if __name__=="__main__":
    main()