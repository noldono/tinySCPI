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
            if val[0] == 'int':
                arg = int(arg)
                if val[1] > arg or val[2] < arg:
                    raise ValueError

            if val[0] == 'bool':
                if arg != 'ON' and arg != 'OFF':
                    raise ValueError

            if val[0] == 'str':
                if arg == 'str' or arg not in val:
                    raise ValueError

            new_args.append(arg)
        return cmd, new_args

    def parseResult(self, result: str) -> str:
        return ""