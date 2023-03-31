import tinySCPI
from threading import Event

def main():
    #placeholder
    info = tinySCPI.userInput('DISPlay:GRAPhics:COLor 3 0x00FF00')
    print(info)
    #Event().wait(10)
    #tinySCPI.userInput('PROGram:SELected:STATe CONTinue')
if __name__=="__main__":
    main()