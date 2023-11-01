from tinyscpi import scpi_functional as sf

SCPILookUpTable = {
    # Standard SCPI Commands
    '*IDN?': 'info',
    '*TST?': 'selftest',
    '*RST': 'reset',
    '*CLR': 'clearconfig',
    '*HLP': 'help',

    # System Subtree
    'SYST:DAC': 'dac',
    'SYST:ID': 'deviceid',
    'SYST:VERS': 'version',
    'SYST:MODE:LOW:IN': 'mode low input',
    'SYST:MODE:LOW:OUT': 'mode low output',
    'SYST:MODE:HIGH:IN': 'mode high input',
    'SYST:MODE:HIGH:OUT': 'mode high output',
    'SYST:OFFS': 'vbat_offset',
    'SYST:VBAT': 'vbat',
    'SYST:SAVE': 'save',
    'SYST:SCONF': 'saveconfig',
    'SYST:TCAL': 'touchcal',
    'SYST:TTEST': 'touchtest',
    'SYST:THRE': 'threads',
    'SYST:STEST': sf.SCPI_functional.selftest,
    'SYST:CLRCONF': 'clearconfig 1234',

    # FREQuency subsystem
    'FREQ:START': 'sweep start',
    'FREQ:STOP': 'sweep stop',
    'FREQ:CENT': 'sweep center',
    'FREQ:SPAN': 'sweep span',
    'FREQ:SPAN:ZERO': 'sweep span 0',
    'FREQ:RBW': 'rbw',
    'FREQ:RBW:AUTO': 'rbw auto',
    'FREQ:DUMP': 'frequencies',
    'FREQ:SCAN:FREQ': 'scan [src] [dst] 290 1',
    'FREQ:SCAN:MEAS': 'scan [src] [dst] 290 2',
    'FREQ:SCAN:STOR': 'scan [src] [dst] 290 4',

    'FREQ:IF:AUTO': 'if 0',
    'FREQ:IF': 'if',

    # LVL subsystem
    'LVL:ATT': 'attenuate',
    'LVL:ATT:AUTO': 'attenuate auto',
    'LVL:REF': 'trace reflevel',
    'LVL:REF:AUTO': 'trace reflevel auto',
    'LVL:SCAL': 'trace scale',
    'LVL:SCAL:AUTO': 'trace scale auto',
    'LVL:UNIT': 'trace',
    'LVL:XGAIN': 'ext_gain',

    # TRIGger subsystem
    'TRIG:TYPE:AUTO': 'trigger auto',
    'TRIG:TYPE:NORM': 'trigger normal',
    'TRIG:TYPE:SNGL': 'trigger single',
    'TRIG:LVL': 'trigger [src]',

    # TRACe subsystem
    'TRAC:FREZ:ON': 'trace [src] freeze on',
    'TRAC:FREZ:OFF': 'trace [src] freeze off',
    'TRAC:VIEW:ON': 'trace [src] view on',
    'TRAC:VIEW:OFF': 'trace [src] view off',
    'TRAC:VAL': 'trace [src] value',
    'TRAC:COPY': 'trace [src] copy [dst]',
    'TRAC:SUB': 'trace [src] subtract [dst]',
    'TRAC:SUB:OFF': 'trace [src] subtract off',

    # DISPlay subsystem
    'DISP:PAUSE': 'pause',
    'DISP:RESUME': 'resume',
    'DISP:REFRESH': 'resume',
    'DISP:COLOR?': 'color',
    'DISP:SWEEPTIME': 'sweeptime',
    'DISP:COLOR': 'color',
    'DISP:TOUCH:PUSH': 'touch',
    'DISP:TOUCH:RELE': 'release',
    'DISP:SPUR': 'spur',

    # OUTput Subsystem
    'OUT:LEV': 'level',
    'OUT:LEVO:LOW': 'leveloffset low',
    'OUT:LEVO:HIGH': 'leveloffset high',
    'OUT:LEVO:SWIT': 'leveloffset switch',
    'OUT:LEVCH': 'levelchange',
    'OUT:MOD': 'modulation',
    'OUT:MOD:FREQ': 'modulation freq',
    'OUT:ON': 'output on',
    'OUT:OFF': 'output off',
    'OUT:CALI:OFF': 'caloutput off',
    'OUT:CALI': 'caloutput',

    # Marker Subsystem
    'MARK:FREQ': 'marker [src] [dst]',
    'MARK:DELT': 'marker [src] delta [dst]',
    'MARK:DELT:OFF': 'marker [src] delta off',
    'MARK:NOIS:SET': 'marker [src] noise on',
    'MARK:NOIS:OFF': 'marker [src] noise off',
    'MARK:TRAK:SET': 'marker [src] tracking on',
    'MARK:TRAK:OFF': 'marker [src] tracking off',
    'MARK:TRAC': 'marker [src] trace [dst]',
    'MARK:AVER:SET': 'marker [src] trace_aver on',
    'MARK:AVER:OFF': 'marker [src] trace_aver off',
    'MARK:SRCH:PEAK': 'marker [src] peak',
    'MARK:DEL': 'marker [src] off',
    'MARK:RST': 'marker off',

    # MEASure subsystem
    'MEAS:HARM': (lambda obj, args: sf.SCPI_functional.MEASure_HARMonic(obj, args)),
    'MEAS:OIP3': (lambda obj, args: sf.SCPI_functional.MEASure_OIP3(obj, args)),
    'MEAS:PNOIS': (lambda obj, args: sf.SCPI_functional.MEASure_PhaseNOISe(obj, args)),
    'MEAS:SNR': (lambda obj, args: sf.SCPI_functional.MEASure_SNR(obj, args)),
    'MEAS:3DB': (lambda obj, args: sf.SCPI_functional.MEASure_3DB(obj, args)),
    'MEAS:AM': (lambda obj, args: sf.SCPI_functional.MEASure_AM(obj, args)),
    'MEAS:FM': (lambda obj, args: sf.SCPI_functional.MEASure_FM(obj, args)),
    'MEAS:THD': (lambda obj, args: sf.SCPI_functional.MEASure_THD(obj, args)),
    'MEAS:CHPOW': (lambda obj, args: sf.SCPI_functional.MEASure_CHPOW(obj, args)),
    'MEAS:LINE': (lambda obj, args: sf.SCPI_functional.MEASure_LINEar(obj, args)),
    'MEAS:DUMP': 'data',

    # CONFig subsystem
    'CONF:CALC': 'calc',
    'CONF:CAPT': sf.SCPI_functional.take_screenshot,
    'CONF:CORR:LOW': 'correction low',
    'CONF:CORR:HIGH': 'correction high',

}
