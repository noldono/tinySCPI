import re
import string

from .dictionaries import scpi_cmds_mapped_to_funcs_dict
from .dictionaries import scpi_lookup_dict as scpi_lookup_dict
from .dictionaries import scpi_valid_dict as scpi_valid_dict
from . import helpers

class SCPI_Parser:
    # what if parser drops every single lower case insturctions?

    def __init__(self):
        self.a = 0
        self.validCommandTable = scpi_valid_dict.validCommandTable
        self.scpiLookupTable = scpi_lookup_dict.SCPILookUpTable
        self.scpiCmdsMappedToFuncs = scpi_cmds_mapped_to_funcs_dict.SCPI_Commands_Mapped_To_Funcs
        self.cmd = ""
        self.table = str.maketrans('', '', string.ascii_lowercase)

    def parseCommand(self, command: str):

        if len(command.strip()) == 0:
            raise KeyError('no string value provided')
        strs = command.split(' ')
        self.cmd = strs[0]
        self.cmd = self.cmd.translate(self.table)
        self.handleUSBCommandInput()

        if self.cmd not in self.validCommandTable:
            raise Exception('"', self.cmd + '" is not a valid scpi command')

        validation = self.validCommandTable.get(self.cmd)

        if len(strs) == 1 and len(validation) == 0:
            return self.cmd, []

        if (len(strs) - 1) != len(validation):
            raise Exception(len(validation), ' inputs required but ', len(strs - 1), ' inputs given' )

        new_args = []
        args = strs[1:]
        for arg, val in zip(args, validation):
            if val[0] == 'int':
                arg = int(arg)
                if val[1] > arg or val[2] < arg:
                    raise Exception('Invalid Param')

            elif val[0] == 'bool':
                if arg == 'ON':
                    arg = True
                elif arg == 'OFF':
                    arg = False
                else:
                    raise Exception('Invalid Param')


            elif val[0] == 'str':
                if arg == 'str' or arg not in val:
                    raise Exception('Invalid Param')

            elif val[0] == 'input':
                if not re.match(arg, 'A-Za-z0-9'):
                    raise Exception('Invalid Param')
                if not re.match(arg.at(0), 'A-Za-z'):
                    raise Exception('Invalid Param')

            elif val[0] == 'hex':
                if int(val[1], 16) > int(arg, 16) or int(val[2], 16) < int(arg, 16):
                    raise Exception('Invalid Param')

            elif val[0] == 'int or str':  # TODO
                arg_int = None
                arg_str = None
                try:
                    arg_int = int(arg)
                except:
                    arg_int = None

                try:
                    arg_str = str(arg)
                except:
                    arg_str = None

                if arg_int != None:
                    if arg_int < int(val[1]) or arg_int > int(val[2]):
                        raise Exception('Invalid Param')
                    arg = arg_int
                elif arg_str != None:
                    if arg_str == 'str' or arg_str not in val:
                        raise Exception("Invalid param")
                    arg = arg_str
                else:
                    raise Exception('Not supported param')

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
