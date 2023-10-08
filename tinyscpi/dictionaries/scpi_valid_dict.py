validCommandTable = {
                     # System commands
                     '*IDN?': [],
                     '*RST': [],
                     '*CLR': [],
                     '*TST?': [],
                     '*HLP': [],

                     # SYSTem Subtree
                     'SYST:DAC': [],
                     'SYST:ID': [],
                     'SYST:VERS': [],
                     'SYST:MODE:LOW': [['str', 'input', 'output']],
                     'SYST:MODE:HIGH': [['str', 'input', 'output']],
                     'SYST:VBAT': [],
                     'SYST:SAVE': [['int', 0, 4]],
                     'SYST:SCONF': [],
                     'SYST:TCAL': [],
                     'SYST:TTEST': [],
                     'SYST:THRE': [],
                     'SYST:OFFS': [['int', 0, 4095]],
                     'SYST:CLRCONF': [],

                     # FREQuency Subsystem
                     'FREQ:START': [['int', 0, 350000000]],
                     'FREQ:STOP': [['int', 0, 350000000]],
                     'FREQ:CENT': [['int', 0, 350000000]],
                     'FREQ:SPAN': [['int', 0, 290]],
                     'FREQ:SPAN:ZERO': [],
                     'FREQ:RBW': [['str', '3', '10', '30', '100', '300', '600']],
                     'FREQ:RBW:AUTO': [],
                     'FREQ:DUMP': [],
                     'FREQ:IF:AUTO': [],
                     'FREQ:IF': [['int', 433000000, 435000000]],

                     # LeVeL Subsystem
                     'LVL:ATT': [['int', 0, 30]],
                     'LVL:ATT:AUTO': [],
                     'LVL:ATT?': [],
                     'LVL:REF': [['float', float('-inf'), float('inf')]], #TODO: double check range
                     'LVL:REF:AUTO': [],
                     'LVL:SCAL': [['str', '1', '2', '5', '10', '20']],
                     'LVL:SCAL:AUTO': [],
                     'LVL:UNIT': [['str', 'dBm', 'dBmV', 'dBuV', 'V', 'W']],
                     'LVL:XGAIN': [['int', -100, 100]],

                     # TRACe Subsystem
                     'TRAC:FREZ:ON': [['int', 1, 3]],
                     'TRAC:FREZ:OFF': [['int', 1, 3]],
                     'TRAC:VIEW:ON': [['int', 1, 3]],
                     'TRAC:VIEW:OFF': [['int', 1, 3]],
                     'TRAC:VAL': [['int', 1, 3]],
                     'TRAC:COPY': [['int', 1, 3], ['int', 1, 3]],
                     'TRAC:SUB': [['int', 1, 3], ['int', 1, 3]],
                     'TRAC:SUB:OFF': [['int', 1, 3]],

                     # DISPlay Subsystem
                     'DISP:PAUSE': [],
                     'DISP:RESUME': [],
                     'DISP:REFRESH': [],
                     'DISP:COLOR': [['int', 0, 30], ['hex', 0x0, 0xffffff]], #TODO: double check int range
                     'DISP:SWEEPTIME': [['int', 0, 10]], # TODO: double check range
                     'DISP:SPUR': [['bool']],
                     'DISP:CAPT': [],

                     # OUTput Subsystem
                     'OUT:LEV': [['int', -76, 13]],
                     'OUT:LEVO:LOW': [['int', -70, 70]],
                     'OUT:LEVO:HIGH': [['int', -70, 70]],
                     'OUT:LEVO:SWIT': [['int', -70, 70]],
                     'OUT:LEVCH': [['int', -70, 70]],
                     'OUT:MOD': [['str', 'off', 'am', 'nfm', 'wfm', 'extern']],
                     'OUT:MOD:FREQ': [['int', 100, 6000]],
                     'OUT:ON': [],
                     'OUT:OFF': [],
                     'OUT:CALI:OFF': [],
                     'OUT:CALI': [['str', '30', '15', '10', '4', '3', '2', '1']],

                     # MARKer Subsystem
                     'MARK:DIFF': [['int', 1, 4], ['int', 1, 4]],
                     'MARK:DIFF:OFF': [['int', 1, 4]],
                     'MARK:NOIS:SET': [['int', 1, 4]],
                     'MARK:NOIS:OFF': [['int', 1, 4]],
                     'MARK:TRAKING': [['int', 1, 4]],
                     'MARK:FREQ': [['int', 1, 4], ['int', 0, 350000000]],

                     'MARK:DELT': [['int', 1, 4], ['int', 1, 4]],
                     'MARK:DELT:OFF': [['int', 1, 4]],

                     'MARK:NOIS:SET': [['int', 1, 4]],
                     'MARK:NOIS:OFF': [['int', 1, 4]],

                     'MARK:TRAK:SET': [['int', 1, 4]],
                     'MARK:TRAK:OFF': [['int', 1, 4]],

                     'MARK:TRAC': [['int', 1, 4], ['int', 1, 3]],

                     'MARK:AVER:SET': [['int', 1, 4]],
                     'MARK:AVER:OFF': [['int', 1, 4]],

                     'MARK:SRCH:PEAK': [['int', 1, 4]],

                     'MARK:SRCH:MINR': [['int', 1, 4]],
                     'MARK:SRCH:MINL': [['int', 1, 4]],
                     'MARK:SRCH:MAXR': [['int', 1, 4]],
                     'MARK:SRCH:MAXL': [['int', 1, 4]],

                     'MARK:SRCH:FREQ': [['int', 0, 350000000], ['int', 0, 350000000]],
                     'MARK:DEL': [['int', 1, 4]],
                     'MARK:RST': [],

                     'MARK:DIFF': [['int', 1, 4], ['int', 1, 4]],
                     'MARK:DIFF:OFF': [['int', 1, 4]],

                     # MEASure Subsystem
                     #TODO: MEASure section

                     # CONFiguration Subsystem
                     'CONF:CAPT': []

                    }
