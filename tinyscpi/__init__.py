import tinySCPI
from threading import Event

def main():
    #placeholder
    tinySCPI.userInput('PROGram:SELected:STATe PAUSe')
    Event().wait(10)
    tinySCPI.userInput('PROGram:SELected:STATe CONTinue')
if __name__=="__main__":
    main()