class SCPI_Parser:
    validCommandTable = {'PROGram:SELected:STATe CONTinue':0, 'PROGram:SELected:STATe CONTinue':0, '*TST?':0, "BAND:RES": 1}
    def __init__(self):
        self.a = 0

    def parseCommand(self, commmand: str) -> (str, list):

        return "", []

    def parseArgument(self, args)->list:
        return []

    def parseResult(self, result)->str:
        return ""