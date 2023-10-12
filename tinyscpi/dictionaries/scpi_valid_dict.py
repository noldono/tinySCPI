validCommandTable = {
                     # System commands
                     '*IDN?': [],
                     '*RST': [],
                     '*CLR': [],
                     '*TST?': [],
                     '*HLP': [],

                     # FREQuency Subsystem
                     'FREQ:START': [['int', 0, 350000000]],
                     'FREQ:STOP': [['int', 0, 350000000]],
                     'FREQ:CENT': [['int', 0, 350000000]],
                     'FREQ:SPAN': [['int', 0, 290]],
                     'FREQ:SPAN:ZERO': [],
                     'FREQ:RBW': [['str', '3', '10', '30', '100', '300', '600']],
                     'FREQ:RBW:AUTO': [],
                     'FREQ:DUMP': [],

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
                     'CONF:CAPT': [],
                     'CONF:CORR:LOW' : [['int', 0, 19], ['int', 0, 999999999], ['int', 0, 999999999]],
                     'CONF:CORR:HIGH' :[['int', 0, 19], ['int', 0, 999999999], ['int', 0, 999999999]],

                    }
