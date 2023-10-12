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
    'SYST:MODE:LOW:IN': 'mode',
    'SYST:MODE:LOW:OUT': 'mode',
    'SYST:MODE:HIGH:IN': 'mode',
    'SYST:MODE:HIGH:OUT': 'mode',
    'SYST:OFFS': 'vbat_offset',
    'SYST:VBAT': 'vbat',
    'SYST:SAVE': 'save',
    'SYST:SCONF': 'saveconfig',
    'SYST:TCAL': 'touchcal',
    'SYST:TTEST': 'touchtest',
    'SYST:THRE': 'threads',
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
    'FREQ:IF:AUTO': 'if 0',
    'FREQ:IF': 'if',
  
    # LEVEL subsystem
    'LEVEL:ATT': 'attenuate',
    'LEVEL:ATT:AUTO': 'attenuate auto',
    'LEVEL:ATT?': 'attenuate',
    'LEVEL:REF': 'trace reflevel',
    'LEVEL:REF:AUTO': 'trace reflevel auto',
    'LEVEL:SCAL': 'trace scale',
    'LEVEL:SCAL:AUTO': 'trace scale auto',
    'LEVEL:UNIT': 'trace',
    'LEVEL:EXT': 'ext_gain',

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
    'DISP:TIME': 'sweeptime',
    'DISP:COLOR': 'color',
    'DISP:CAPT': sf.SCPI_functional.takeScreenshot,
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
    # 'MARK:SRCH:MINR': [['int', 1, 4]],
    # 'MARK:SRCH:MINL': [['int', 1, 4]],
    # 'MARK:SRCH:MAXR': [['int', 1, 4]],
    # 'MARK:SRCH:MAXL': [['int', 1, 4]],
    # 'MARK:SRCH:FREQ': [['int', 0, 350000000], ['int', 0, 350000000]],
    # TODO: Fill in the rest of this

    #Config subsystem
    'CONF:CORR:LOW' : 'correction low',
    'CONF:CORR:HIGH' : 'correction high',
}