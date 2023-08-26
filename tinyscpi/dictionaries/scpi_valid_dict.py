validCommandTable = {'*IDN?': [],
                     '*TST?': [],
                     'BAND:RES': [['int', 3, 600]],
                     'BAND:RES:AUTO': [['bool']],
                     'SYSTem:VERSion?': [],
                     'AMPLitude:ATTenuation': [['int', 0, 31]],
                     'AMPLitude:ATTenuation:AUTO': [],
                     'SOURce:POWer:LEVel:IMMediate:AMPLitude': [['str', 'OFF', '30', '15', '10', '4', '3', '2', '1']],
                     '*RST': [],
                     '*RST:CLEARCONFIG':[],
                     'DISPlay:GRAPhics:COLor?': [],
                     'DISPlay:GRAPhics:COLor': [['int', 0, 31], ['hex', '0x000000', '0xFFFFFF']],
                     'SENSe:CORRection?': [],
                     'SYSTem:HELP?': [],
                     'SOURce:POWer:LEVel:IMMediate:AMPLitude': [['int', -76, 13]],
                     'SOURCe:POWer:LEVel:IMMediate:AMPLitude:OFFSet': [['int', -70, 70]],
                     'FREQuency:OFFSet?': [],
                     'FREQuency:OFFSet': [['str', 'low', 'high', 'switch'], ['int', -20, 20]], # Needs tweaking
                     'SYSTem:PRESet': [['int', 0, 4]],
                     'SOURce:DM:FORMat' : [['str', 'off', 'AM_1kHz', 'AM_10Hz', 'NFM', 'WFM', 'extern']],
                     'SOURce:POWer:AMPLitude': [['int', -100, 100]],
                     'OUTPut': [['bool']],
                     'PROGram:SELected:STATe:PAUSe': [],
                     'SENSe:CORRection': [],
                     'DISPLay:DATA:START':[['int', 0, 320], ['int', 0, 240]],
                     'HCOPy:SDUMp:DATA?':[],
                     'SOURce:VOLTage:LEVel:IMMediate:AMPLitude?': [],
                     'SOURce:VOLTage:LEVel:IMMediate:AMPLitude': [['int', 0, 4096]],
                     'TRACe:DATA?': ['int', 0, 2], #TODO: modify args
                     'MARKer:LEVel?': [],
                     'MARKer:LEVel?': [['int', 1, 4], ['int or str', 0, 355, 'on', 'off', 'peak']], # TODO: change int limit on second argument.
                     'DISPlay:ENABle': [['bool']],
                     '*RST?': [],
                     'PROGram:SELected:STATe:RESUme': [],
                     'TRACe:MEMory:SAVE': [['int', 0, 4]],
                     'SYSTem:SAVE': [['input']],
                     'SYSTem:SERialnumber?': [],
                     'SYSTem:SERialnumber': [['input']],
                     'CONFigure':[['str', 'off', 'minh', 'maxh', 'maxd', 'aver4', 'aver16', 'quasi']],
                     'DISPlay:DATA:START': [['int', 0, 320], ['int', 0, 240]],
                     'DISPlay:DATA:STOP': [['int', 0, 320], ['int', 0, 320]],
                     'DISPlay:DATA:WIDTH': [['int', 0, 320]],
                     'DISPlay:DATA:HEIGHT': [['int', 0, 240]],
                     'DISPlay:DATA:TYPE': [['']],
                     'CALCulate:MEASure:PN:SPURious:OMISsion:STATe': [['str', 'on', 'off']],
                     'SENS:FREQ:STARt:STOP:DATA':[['int', 0, 1000000000], ['int', 0, 1000000000]],
                     'SOURce:POWer:LEVel:IMMediate:AMPLitude:OFFset': [['int', -70, 70]],
                     'SYSTem:VERSion?': [],
                     'SYSTem:MODE': [['str', 'low', 'high'], ['str', 'input', 'output']],
                     'MEASure:SWEep:BEGin:LOW': [['int', 0, 350000000], ['int', 0, 350000000], ['int', 0, 290]], # TODO: Add the high input bounds, currently 0-350MHz are the low bounds
                     'MEASure:SWEep:BEGin:HIGH': [['int', 240000000, 959000000], ['int', 240000000, 959000000], ['int', 0, 290]],
                     'MEASure:SWEep:TIME': [['int', 0, 600]],
                     'MEASure:SCAN:RAW:START': [['int', 0, 350000000], ['int', 0, 350000000], ['int', 0, 2147483647]],
                     'CAPTure': [],
                     'SYSTem:THREADs?': []
                    }
