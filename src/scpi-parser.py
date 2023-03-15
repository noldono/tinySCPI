class SCPI_Parser:
    validCommandTable = {}
    def __init__(self):
        self.a = 1

    def parseCommand(self, commmand)->int:
        return 0

    def parseArgument(self, args)->list:
        return []

    def parseResult(self, result)->str:
        return ""