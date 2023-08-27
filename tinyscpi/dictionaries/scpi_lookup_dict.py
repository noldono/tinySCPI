from tinyscpi import scpi_functional as sf

SCPILookUpTable = {
    "*TST?":"selftest",
    "PROGram:SELected:STATe PAUSe":"pause",
    "PROGram:SELected:STATe CONTinue":"resume",
    "BAND:RES":"rbw",
    "*IDN?":"info",
    'AMPLitude:ATTenuation': 'attenuate',
    'AMPLitude:ATTenuation:AUTO': 'attenuate auto',
    'CONFigure': 'calc',
    'CAPTure': sf.SCPI_functional.takeScreenshot,
    'SOURce:POWer:LEVel:IMMediate:AMPLitude': 'caloutput',
    ':HCOPy:SDUMp:DATA?': 'capture',
    '*RST:CONFIGDATA': 'clearconfig',
    'DISPlay:GRAPhics:COLor?': 'color',
    'DISPlay:GRAPhics:COLor': 'color',
    'SENSe:CORRection': 'correction',
    'SOURce:VOLTage:LEVel:IMMediate:AMPLitude?': 'dac',
    'SOURce:VOLTage:LEVel:IMMediate:AMPLitude': 'dac',
    'TRACe:DATA?': 'data',
    'SYSTem:SERialnumber?': 'deviceid',
    'SYSTem:SERialnumber': 'deviceid',
    'SYSTem:SERialnumber?': 'deviceid',
    'SOURce:FREQuency:FIXed': 'freq',
    'FREQuency:CENTer': 'freq',
    'SOURce:FREQuency:STARt?': 'frequencies',
    'SOURce:FREQuency:STOP?': 'frequencies',
    'SENSe:BANDwidth':'if',
    'SENSe:BWIDth': 'if',
    'SYSTem:HELP?': 'help',
    'SOURce:POWer:LEVel:IMMediate:AMPLitude': 'level',
    'SOURce:POWer:LEVel:IMMediate::AMPLitude:OFFSet': 'levelchange',
    'FREQuency:OFFSet?':'leveloffset',
    'FREQuency:OFFSet': 'leveloffset',
    'SYSTem:PRESet': 'load',
    'MARKer:SET:LEVel?': 'marker',
    'MARKer:SET:LEVel': 'marker',
    'MARKer:MODE': 'mode',
    'SOURce:DM:FORMat': 'modulation',
    'SOURce:POWer AMPLitude': 'ext_gain',
    'OUTPut': 'output',
    'PROGram:SELected:STATe:PAUSe': 'pause',
    'BAND:RES': 'rbw',
    'BAND:RES:AUTO': 'rbw auto',
    'SYSTem:Preset': 'recall',
    'DISPlay:ENABle': 'refresh',
    '*RST': 'reset',
    'SYSTem:PRESet': 'reset',
    'PROGram:SELected:STATe:RESUme': 'resume',
    'TRACe:MEMory:SAVE': 'save',
    'SYST:SET:USER': 'saveconfig',
    'INITiate:IMMediate': 'scan',
    'CALCulate:PARameter:SELect': 'scan',
    'FETCh:IMMediate?': 'scan',
    'SCANRAW:START': 'scanraw',
    'SCANRAW:STOP':'scanraw',
    'SCANRAW:POINTS': 'scanraw',
    'CALCulate:MEASure:PN:SPURious:OMISsion:STATe': 'spur',
    'SWEep:STATe': 'sweep',
    'SWEep:TIME': 'sweeptime',
    'SYSTem:THREADs?': 'threads',
    'SYSTem:TOUCh:TEST:STARt': 'touchtest',
    'TRACe:DATA?':'trace',
    'TRACe:DATA':'trace',
    'TRACe:FEED?':'trace',
    'TRACe:FEED': 'trace',
    'SYSTem:VOLTage:DC?': 'vbat',
    'SYSTem:VOLTage:DC:OFFSet?': 'vbat_offset',
    'SYSTem:VOLTage:DC:OFFSet': 'vbat_offset',
    'SYSTem:VERSion?': 'version',
    'SENSe:CORRection?': 'correction low',
    'SOURce:POWer:LEVel:IMMediate:AMPLitude:OFFset': 'levelchange',
    'SYSTem:MODE': 'mode',
    'SYSTem:VERSion?': 'version',
    'MEASure:SWEep:BEGin:LOW': 'sweep',
    'MEASure:SWEep:BEGin:HIGH': 'sweep',
    'MEASure:SWEep:TIME': 'sweeptime',
    'MEASure:SCAN:RAW:START': 'scanraw',
}
