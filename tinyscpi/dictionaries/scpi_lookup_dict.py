from tinyscpi import scpi_functional as sf

SCPILookUpTable = {
                    '*TST?':'selftest',
                    'PROG:SEL:STAT:PAUS': 'pause',
                    'PROG:SEL:STAT:RESU': 'resume',
                    '*IDN?':'info',
                    'AMPL:ATT': 'attenuate',
                    'AMPL:ATT:AUTO': 'attenuate auto',
                    'CONF': 'calc',
                    'CAPT': sf.SCPI_functional.takeScreenshot,
                    'OUTP:CALI': 'caloutput',
                    '*RST:CONFIGDATA': 'clearconfig',
                    'DISP:GRAP:COL?': 'color',
                    'DISP:GRAP:COL': 'color',
                    'SENS:CORR': 'correction',
                    'SOUR:VOLT:LEV:IMM:AMPL?': 'dac',
                    'SOUR:VOLT:LEV:IMM:AMPL': 'dac',
                    'SYST:DATA?': 'data',
                    'SYST:SER?': 'deviceid',
                    'SYST:SER': 'deviceid',
                    'SOUR:FREQ:FIX': 'freq',
                    'FREQ:CENT': 'freq',
                    'SOUR:FREQ:STAR?': 'frequencies',
                    'SOUR:FREQ:STOP?': 'frequencies',
                    'SENS:BAND':'if',
                    'SENS:BWID': 'if',
                    'SYST:HELP?': 'help',
                    'SOUR:POW:LEV:IMM:AMPL': 'level',
                    'SOUR:POW:LEV:IMM::AMPL:OFFS': 'levelchange',
                    'FREQ:OFFS?':'leveloffset',
                    'FREQ:OFFS': 'leveloffset',
                    'SYST:PRES': 'load',
                    'MARK:SET:LEV?': 'marker',
                    'MARK:SET:LEV': 'marker',
                    'MARK:MODE': 'mode',
                    'SOUR:DM:FORM': 'modulation',
                    'SOUR:POW:AMPL': 'ext_gain',
                    'OUTP': 'output',
                    'BAND:RES': 'rbw',
                    'BAND:RES:AUTO': 'rbw auto',
                    'SYST:P': 'recall',
                    'DISP:ENAB': 'refresh',
                    '*RST': 'reset',
                    'TRAC:MEM:SAVE': 'save',
                    'SYST:SET:USER': 'saveconfig',
                    'INIT:IMM': 'scan',
                    'CALC:PAR:SEL': 'scan',
                    'FETC:IMM?': 'scan',
                    'SCANRAW:START': 'scanraw',
                    'SCANRAW:STOP':'scanraw',
                    'SCANRAW:POINTS': 'scanraw',
                    'CALC:MEAS:PN:SPUR:OMIS:STAT': 'spur',
                    'SWE:STAT': 'sweep',
                    'SWE:TIME': 'sweeptime',
                    'SYST:THREAD?': 'threads',
                    'SYST:TOUC:TEST:STAR': 'touchtest',
                    'TRAC:DATA?':'trace',
                    'TRAC:DATA':'trace',
                    'TRAC:FEED?':'trace',
                    'TRAC:FEED': 'trace',
                    'SYST:VOLT:DC?': 'vbat',
                    'SYST:VOLT:DC:OFFS?': 'vbat_offset',
                    'SYST:VOLT:DC:OFFS': 'vbat_offset',
                    'SENS:CORR:LOW?': 'correction low',
                    'SENS:CORR:HIGH?': 'correction high',
                    'SOUR:POW:LEV:IMM:AMPL:OFF': 'levelchange',
                    'SYST:MODE': 'mode',
                    'SYST:VERS?': 'version',
                    'MEAS:SWE:BEG:LOW': 'sweep',
                    'MEAS:SWE:BEG:HIGH': 'sweep',
                    'MEAS:SWE:TIME': 'sweeptime',
                    'MEAS:SCAN:RAW:START': 'scanraw',
                    'MEAS:TRIG': 'trigger',
}
