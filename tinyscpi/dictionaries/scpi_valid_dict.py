validCommandTable = {'*IDN?': [],
                     '*TST?': [],
                     'BAND:RES': [['int', 3, 600]],
                     'BAND:RES:AUTO': [['bool']],
                     'SYST:VERS?': [],
                     'AMPL:ATT': [['int', 0, 31]],
                     'AMPL:ATT:AUTO': [],
                     'OUTP:CALI': [['str', 'OFF', '30', '15', '10', '4', '3', '2', '1']],
                     '*RST': [],
                     '*RST:CLEARCONFIG':[],
                     'DISP:GRAP:COL?': [],
                     'DISP:GRAP:COL': [['int', 0, 31], ['hex', '0x000000', '0xFFFFFF']],
                     'SENS:CORR?': [],
                     'SYST:HELP?': [],
                     'MEAS:TRIG': [['int or str', -200, 10, 'auto', 'normal', 'single']],
                     'SOUR:POW:LEV:IMM:AMPL': [['int', -76, 13]],
                     'SOUR:POW:LEV:IMM:AMPL:OFFS': [['int', -70, 70]],
                     'FREQ:OFFS?': [],
                     'FREQ:OFFS': [['str', 'low', 'high', 'switch'], ['int', -20, 20]], # Needs tweaking
                     'SYST:PRES': [['int', 0, 4]],
                     'SOUR:DM:FORM': [['str', 'off', 'AM_1kHz', 'AM_10Hz', 'NFM', 'WFM', 'extern']],
                     'SOUR:POW:AMPL': [['int', -100, 100]],
                     'OUTP': [['bool']],
                     'PROG:SEL:STAT:PAUS': [],
                     'SENS:CORR': [], #TODO: is this command valid?
                     'HCOP:SDUM:DATA?':[],
                     'SOUR:VOLT:LEV:IMM:AMPL?': [],
                     'SOUR:VOLT:LEV:IMM:AMPL': [['int', 0, 4096]],
                     'TRAC:DATA?': [['int', 0, 2]], #TODO: modify args
                     'MARK:LEV?': [],
                     'MARK:LEV': [['int', 1, 4], ['int or str', 0, 355, 'on', 'off', 'peak']], # TODO: change int limit on second argument.
                     'DISP:ENAB': [['bool']],
                     '*RST?': [], #TODO is *RST same with *RST?
                     'PROG:SEL:STAT:RESU': [],
                     'TRAC:MEM:SAVE': [['int', 0, 4]],
                     'SYST:SAVE': [['input']], # WHAT IS THIS?
                     'SYST:SER?': [],
                     'SYST:SER': [['input']], # WHAT IS THIS?
                     'CONF':[['str', 'off', 'minh', 'maxh', 'maxd', 'aver4', 'aver16', 'quasi']],
                     'DISP:DATA:START': [['int', 0, 320], ['int', 0, 240]],
                     'DISP:DATA:STOP': [['int', 0, 320], ['int', 0, 320]],
                     'DISP:DATA:WIDTH': [['int', 0, 320]],
                     'DISP:DATA:HEIGHT': [['int', 0, 240]],
                     'DISP:DATA:TYPE': [['']], # TODO: Validate Arguments.
                     'CALC:MEAS:PN:SPUR:OMIS:STAT': [['str', 'on', 'off']],
                     'SENS:FREQ:STAR:STOP:DATA':[['int', 0, 1000000000], ['int', 0, 1000000000]],
                     'SOUR:POW:LEV:IMM:AMPL:OFF': [['int', -70, 70]],
                     'SYST:MODE': [['str', 'low', 'high'], ['str', 'input', 'output']],
                     'MEAS:SWE:BEG:LOW': [['int', 0, 350000000], ['int', 0, 350000000], ['int', 0, 290]], # TODO: Add the high input bounds, currently 0-350MHz are the low bounds
                     'MEAS:SWE:BEG:HIGH': [['int', 240000000, 959000000], ['int', 240000000, 959000000], ['int', 0, 290]],
                     'MEAS:SWE:TIME': [['int', 0, 600]],
                     'MEAS:SCAN:RAW:START': [['int', 0, 350000000], ['int', 0, 350000000], ['int', 0, 2147483647]],
                     'CAPT': [],
                     'SYST:THREAD?': [],
                     'SYST:VOLT:DC:OFFS':[['int', 0, 4095]]
                    }