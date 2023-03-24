class SCPI_Parser:
    # what if parser drops every single lower case insturctions?
    validCommandTable = {'PROGram:SELected:STATe CONTinue': 0, '*TST?': 0, "BAND:RES": 1}

    def __init__(self):
        self.a = 0

    def parseCommand(self, commmand: str) -> tuple[str, list]:
        return "", []

    def parseArgument(self, args: str) -> list:
        return []

    def parseResult(self, result: str) -> str:
        return ""
