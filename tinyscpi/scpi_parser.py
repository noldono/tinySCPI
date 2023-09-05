import re
import string

import dictionaries.scpi_cmds_mapped_to_funcs_dict as scpi_commands_mapped_to_funcs_dict
import dictionaries.scpi_lookup_dict as scpi_lookup_dict
import dictionaries.scpi_valid_dict as scpi_valid_dict
import helpers as helpers

class SCPI_Parser:
    # what if parser drops every single lower case insturctions?

    def __init__(self):
        self.a = 0
        self.validCommandTable = scpi_valid_dict.validCommandTable
        self.scpiLookupTable = scpi_lookup_dict.SCPILookUpTable
        self.scpiCmdsMappedToFuncs = scpi_commands_mapped_to_funcs_dict.SCPI_Commands_Mapped_To_Funcs
        self.cmd = ""

    def parseCommand(self, command: str):

        if len(command.strip()) == 0:
            raise KeyError('no string value provided')
        strs = command.split(' ')
        self.cmd = strs[0]

        self.handleUSBCommandInput()

        if self.cmd not in self.validCommandTable:
            raise KeyError('not a valid scpi command')

        validation = self.validCommandTable.get(self.cmd)

        if len(strs) == 1 and len(validation) == 0:
            return self.cmd, []

        if (len(strs) - 1) != len(validation):
            raise SyntaxError

        new_args = []
        args = strs[1:]
        for arg, val in zip(args, validation):
            if val[0] == 'int':
                arg = int(arg)
                if val[1] > arg or val[2] < arg:
                    raise ValueError

            elif val[0] == 'bool':
                if arg != 'ON' and arg != 'OFF':
                    raise ValueError
                return self.cmd, new_args

            elif val[0] == 'str':
                if arg == 'str' or arg not in val:
                    raise ValueError

            elif val[0] == 'input':
                if not re.match(arg, 'A-Za-z0-9'):
                    raise ValueError
                if not re.match(arg.at(0), 'A-Za-z'):
                    raise ValueError

            elif val[0] == 'hex':
                if int(val[1], 16) > int(arg, 16) or int(val[2], 16) < int(arg, 16):
                    raise ValueError

            elif val[0] == 'int or str':  # TODO
                if not arg.replace("-", "").isalnum():
                    raise TypeError
                if arg.isnumeric():
                    if int(val[1]) > int(arg) or int(val[2]) < int(arg):
                        raise ValueError
                if arg.isalpha():
                    if arg not in val[1:]:
                        raise ValueError
            else:
                raise TypeError

            new_args.append(arg)
        return self.cmd, new_args

    def parseResult(self, result: str) -> str:
        return ""

    def handleUSBCommandInput(self) -> None:
        # If user inputs a usb command instead of a SCPI command, set cmd equal to the corresponding scpi command
        matching_scpi_command = helpers.find_key_by_value(self.scpiLookupTable, self.cmd)
        cmd_mapped_to_func = self.scpiCmdsMappedToFuncs.get(self.cmd, None)

        if matching_scpi_command is not None:
            self.cmd = matching_scpi_command
        elif cmd_mapped_to_func is not None:
            self.cmd = cmd_mapped_to_func
