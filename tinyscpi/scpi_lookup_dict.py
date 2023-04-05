SCPILookUpTable = {
    "*TST?":"selftest",
    "PROGram:SELected:STATe PAUSe":"pause",
    "PROGram:SELected:STATe CONTinue":"resume",
    "BAND:RES":"rbw",
    "*IDN?":"info",
    'AMPLitude:ATTenuation': 'attenuate',
    'AMPLitude:ATTenuation:AUTO': 'attenuate auto',
    'CONFigure': 'calc',
    'SOURce:POWer:LEVel:IMMediate:AMPLitude': 'caloutput',
    ':HCOPy:SDUMp:DATA?': 'capture',
    '*RST:CLEARCONFIG': 'clearconfig 1234',
    '*RST': 'reset',
    'DISPlay:GRAPhics:COLor?': 'color',
    'DISPlay:GRAPhics:COLor': 'color',
    'SENSe:CORRection?': 'correction',
    'SENSe:CORRection': 'correction',
    'DISPlay:GRAPhics:COLor?' : 'color',
    'DISPlay:GRAPhics:COLor': 'color',
    'SYSTem:SERialnumber?': 'deviceid',
    'SYSTem:SERialnumber': 'deviceid'
}
