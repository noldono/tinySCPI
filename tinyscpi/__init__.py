import tinySCPI
from threading import Event

def main():
    #placeholder
    info = tinySCPI.capture("file.png")
    #tinySCPI.userInput("*RST:CONFIGDATA")
    print(info)
    #tinySCPI.userInput('PROGram:SELected:STATe CONTinue')
if __name__=="__main__":
    main()