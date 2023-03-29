import scpi_valid_dict
class SCPI_Parser:
    # what if parser drops every single lower case insturctions?

    def __init__(self):
        self.a = 0
        self.validCommandTable = scpi_valid_dict.validCommandTable

    def parseCommand(self, command: str) -> (str, list):
        if len(command.strip()) == 0:
            raise KeyError('no string value provided')
        strs = command.split(' ')
        cmd = strs[0]
        if cmd not in self.validCommandTable:
            raise KeyError('not a valid scpi command')

        validation = self.validCommandTable.get(cmd)

        if len(strs) == 1 and len(validation) == 0:
            return cmd, []

        if (len(strs)-1) != len(validation):
            raise SyntaxError

        new_args = []
        args = strs[1:]
        for arg, val in zip(args, validation):
            if val == 'int':
                new_args.append(int(arg))
            if val == 'str':
                new_args.append(arg)
        return cmd, new_args

    def parseResult(self, result: str) -> str:
        return ""