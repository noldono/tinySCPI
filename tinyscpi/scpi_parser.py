import string

from .dictionaries import scpi_cmds_mapped_to_funcs_dict
from .dictionaries import scpi_lookup_dict as scpi_lookup_dict
from .dictionaries import scpi_valid_dict as scpi_valid_dict


class SCPI_Parser:

    def __init__(self):
        self.validCommandTable = scpi_valid_dict.validCommandTable
        self.scpiLookupTable = scpi_lookup_dict.SCPILookUpTable
        self.scpiCmdsMappedToFuncs = scpi_cmds_mapped_to_funcs_dict.SCPI_Commands_Mapped_To_Funcs
        self.cmd = ""

        ''' Table used to drop all the lowercase letters from a SCPI command'''
        self.table = str.maketrans('', '', string.ascii_lowercase)

    '''
    Parse a command string from user and validate command and parameters
    '''

    def parse_command(self, command: str):

        if len(command.strip()) == 0:
            raise KeyError('no string value provided')

        strs = command.strip().split()

        # extract command from command string
        self.cmd = strs[0]
        self.cmd = self.cmd.translate(self.table)

        #
        if self.cmd not in self.validCommandTable:
            raise KeyError('"', self.cmd + '" is not a valid scpi command')

        validation = self.validCommandTable.get(self.cmd)

        if len(strs) == 1 and len(validation) == 0:
            return self.cmd, []

        if (len(strs) - 1) != len(validation):
            raise SyntaxError(len(validation), ' inputs required but ', len(strs) - 1, ' inputs given')

        new_args = []
        args = strs[1:]
        for arg, val in zip(args, validation):
            if val[0] == 'int':
                arg = int(arg)
                if val[1] > arg or val[2] < arg:
                    raise ValueError('Invalid Param')

            elif val[0] == 'float':
                arg = float(arg)
                if val[1] > arg or val[2] < arg:
                    raise ValueError('Invalid Param')

            elif val[0] == 'bool':
                if arg == 'ON':
                    arg = True
                elif arg == 'OFF':
                    arg = False
                else:
                    raise ValueError('Invalid Param')

            elif val[0] == 'str':
                if arg == 'str' or arg not in val:
                    raise ValueError('Invalid Param')

            elif val[0] == 'hex':
                if int(val[1]) > int(arg, 16) or int(val[2]) < int(arg, 16):
                    raise ValueError('Invalid Param')
                arg = hex(int(arg, 16))

            new_args.append(arg)
        return self.cmd, new_args
