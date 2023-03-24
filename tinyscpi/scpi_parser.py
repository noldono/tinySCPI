from scpi_functional import SCPI_functional
class SCPI_Parser:
    validCommandTable = {}

    def __init__(self):
        # Initialize valid command table
        self.validCommandTable = {
            "*IDN?": self.get_instrument_id,
            "SYSTem:VERSion?": self.get_instrument_version,
            "MEASure:VOLTage:DC?": self.get_instrument_battery
        }
        self.Functional = SCPI_functional()

    def parseCommand(self, command: str) -> int:
        # Look up command in valid command table
        if command in self.validCommandTable:
            # Execute the corresponding Python function and return the result
            return self.validCommandTable[command](command)
        else:
            # Invalid command
            return -1

    def parseArgument(self, args: str) -> list:
        # Parse the argument string and return a list of values
        # ...
        return []

    def parseResult(self, result: str) -> str:
        # Format the result string in a user-friendly format and return it
        # ...
        return ""
    
    def get_instrument_id(self, command: str) -> str:
        # Call the get_id method of the Instrument instance to get the instrument ID
        return self.Functional.get_id()
    
    def get_instrument_version(self, command: str) -> str:
        return self.Functional.get_version()
    
    def get_instrument_battery(self, command: str) -> str:
        return self.Functional.get_battery()