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
    'SYST:MODE': 'mode',
    'SYST:VBAT': 'vbat',
    'SYST:SAVE': 'save',
    'SYST:SCONF': 'saveconfig',
    'SYST:TCAL': 'touchcal',
    'SYST:TTEST': 'touchtest',
    'SYST:THRE': 'threads',

    # FREQuency subsystem
    'FREQ:START': 'sweep start',
    'FREQ:STOP': 'sweep stop',
    'FREQ:CENT': 'sweep center',
    'FREQ:SPAN': 'sweep span',
    'FREQ:SPAN:ZERO': 'sweep span 0',
    'FREQ:RBW': 'rbw',
    'FREQ:RBW:AUTO': 'rbw auto',
    'FREQ:DUMP': 'frequencies',

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
    'DISP:REFR': 'resume',
    'DISP:COLOR?': 'color',
    'DISP:TIME': 'sweeptime',
    'DISP:COLOR': 'color',
    'DISP:CAPT': sf.SCPI_functional.takeScreenshot,
    'DISP:TOUCH:PUSH': 'touch',
    'DISP:TOUCH:RELE': 'release',

    # MARKer Subsystem
    'MARK:DELT': 'marker [src] delta [dst]',
    'MARK:DELT:OFF': 'marker [src] delta off',
    'MARK:NOIS:SET': 'marker [src] noise on',
    'MARK:NOIS:OFF': 'marker [src] noise off',
    # 'MARK:TRAKING': [['int', 1, 4]],
    # 'MARK:TRAC': [['int', 1, 4], ['int', 1, 3]],
    # 'MARK:AVER': [['int', 1, 4]],
    'MARK:SRCH:PEAK': 'marker [src] peak',
    # 'MARK:SRCH:MINR': [['int', 1, 4]],
    # 'MARK:SRCH:MINL': [['int', 1, 4]],
    # 'MARK:SRCH:MAXR': [['int', 1, 4]],
    # 'MARK:SRCH:MAXL': [['int', 1, 4]],
    # 'MARK:SRCH:FREQ': [['int', 0, 350000000], ['int', 0, 350000000]],
    'MARK:DEL': 'marker [src] off',
    # 'MARK:RST': [],
}