validCommandTable = {'*IDN?': [],
                     '*TST?': [],
                     'BAND:RES': [['int', 3, 600]],
                     'BAND:RES:AUTO': [['bool']],
                     'SYSTem:VERSion?': [],
                     'AMPLitude:ATTenuation': [['int', 0, 31]],
                     'SOURce:POWer:LEVel:IMMediate:AMPLitude': [['str', 'OFF', '30', '15', '10', '4', '3', '2', '1']],
                     '*RST': [],
                     '*RST:CONFIGDATA':[],
                     'DISPlay:GRAPhics:COLor?': [],
                     'DISPlay:GRAPhics:COLor': [['int', 0, 65535]],
                     'SENSe:CORRection': [],
                     'DISPLay:DATA:START':[['int', 0, 320], ['int', 0, 240]],
                     'HCOPy:SDUMp:DATA?':[],
                     'SOURce:VOLTage:LEVel:IMMediate:AMPLitude?': [],
                     'SOURce:VOLTage:LEVel:IMMediate:AMPLitude': [['int', 0, 4096]],
                     'TRACe:DATA?': ['int', 0, 2],
                     'MARKer:LEVel?': [],
                     'MARKer:LEVel?': [['int', 1, 4], ['int or str', 0, 355, 'on', 'off', 'peak']] # TODO: change int limit on second argument.



                    }