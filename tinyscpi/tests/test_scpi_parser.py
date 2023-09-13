from tinyscpi import scpi_parser
import unittest

class ParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = scpi_parser.SCPI_Parser()
        #TODO: Unimplemented Method Stub

    def testParseCommand_IDN(self):
        self.assertEqual(self.parser.parseCommand('*IDN?'), ('*IDN?',[]))
        self.assertEqual(self.parser.parseCommand('BAND:RES 3'), ('BAND:RES', [3]))
        with self.assertRaises(KeyError):
            self.parser.parseCommand('*IDN')
        with self.assertRaises(ValueError):
            self.parser.parseCommand('BAND:RES str')
        with self.assertRaises(SyntaxError):
            self.parser.parseCommand('BAND:RES')
        self.assertEqual(self.parser.parseCommand('DISP:GRAP:COLor 3 0x000000'), ('DISP:GRAP:COL', [3, '0x000000']))
                    #TODO: Unimplemented Method Stub


    def testParseCommand_TST(self):
        self.assertEqual(self.parser.parseCommand('*TST?'), ('*TST?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('*TST')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TST?')
        with self.assertRaises(Exception):
            self.parser.parseCommand('*TST? 1')

    def testParseCommand_BAND_RES(self):
        self.assertEqual(self.parser.parseCommand('BAND:RES 3'), ('BAND:RES', [3]))
        self.assertEqual(self.parser.parseCommand('BAND:RES 600'), ('BAND:RES', [600]))
        self.assertEqual(self.parser.parseCommand('BAND:RESolution 3'), ('BAND:RES', [3]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('BANDRES')

        with self.assertRaises(Exception):
            self.parser.parseCommand('BAND:RES')

        with self.assertRaises(Exception):
            self.parser.parseCommand('BAND:RES 601')
        with self.assertRaises(Exception):
            self.parser.parseCommand('BAND:RES 2')

        with self.assertRaises(Exception):
            self.parser.parseCommand('BAND:RES 3.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('BAND:RES band')

        with self.assertRaises(Exception):
            self.parser.parseCommand('BAND:RES 3 600')


    def testParseCommand_BAND_RES_AUTO(self):
        self.assertEqual(self.parser.parseCommand('BAND:RES:AUTO ON'), ('BAND:RES:AUTO', []))
        self.assertEqual(self.parser.parseCommand('BAND:RES:AUTO OFF'), ('BAND:RES:AUTO', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('BAND:RES:AUTO')

        with self.assertRaises(Exception):
            self.parser.parseCommand('BAND:RES:AUTO auto')

    def testParseCommand_SYST_VERS(self):
        self.assertEqual(self.parser.parseCommand('SYST:VERS?'), ('SYST:VERS?', []))
        self.assertEqual(self.parser.parseCommand('SYSTem:VERSion?'), ('SYST:VERS?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS? 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS? 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS? new')


    def testParseCommand_AMPL_ATT(self):
        self.assertEqual(self.parser.parseCommand('AMPL:ATT 0'), ('AMPL:ATT', [0]))
        self.assertEqual(self.parser.parseCommand('AMPLitude:ATTenuation 15'), ('AMPL:ATT', [15]))
        self.assertEqual(self.parser.parseCommand('AMPL:ATT 31'), ('AMPL:ATT', [31]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL:ATT 32')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL:ATT -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL:ATT 0.2')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL:ATT')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL:ATT 0 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL:ATT std')


    def testParseCommand_AMPL_ATT_AUTO(self):
        self.assertEqual(self.parser.parseCommand('AMPL:ATT:AUTO'), ('AMPL:ATT:AUTO', []))
        self.assertEqual(self.parser.parseCommand('AMPLitude:ATTenuation:AUTO'), ('AMPL:ATT:AUTO', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL_ATT_AUTO On')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL_ATT_AUT')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL_ATT_AUTO 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL_ATT_AUTO 1.5')

    def testParseCommand_SOUR_POW_LEV_IMM_AMPL(self):
        self.assertEqual(self.parser.parseCommand('SOURce:POWer:LEVel:IMMediate:AMPLitude OFF'), ('SOUR:POW:LEV:IMM:AMPL', ['OFF']))
        self.assertEqual(self.parser.parseCommand('SOURce:POWer:LEVel:IMMediate:AMPLitude 2'), ('SOUR:POW:LEV:IMM:AMPL', [2]))
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL OFF'), ('SOUR:POW:LEV:IMM:AMPL', ['OFF']))
        self.assertEqual(self.parser.parseCommand('SOURce:POWer:LEVel:IMMediate:AMPLitude 30'), ('SOUR:POW:LEV:IMM:AMPL', [30]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL ON')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 20')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 1.7')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL ON OFF')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 5 OFF')

    def testParseCommand_RST(self):
        self.assertEqual(self.parser.parseCommand('*RST'), ('*RST', []))
        with self.assertRaises(Exception):
            self.parser.parseCommand('RST')
        with self.assertRaises(Exception):
            self.parser.parseCommand('RST?')
        with self.assertRaises(Exception):
            self.parser.parseCommand('*RST 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('*RST reset')

    def testParseCommand_CLEARCONFIG(self):
        self.assertEqual(self.parser.parseCommand('*RST:CLEARCONFIG'), ('*RST:CLEARCONFIG', []))
        with self.assertRaises(Exception):
            self.parser.parseCommand('RST:CLEARCONFIG')
        with self.assertRaises(Exception):
            self.parser.parseCommand('*RST:CLEARCONFIG clear')
        with self.assertRaises(Exception):
            self.parser.parseCommand('RST:CLEARCONFIG 0')

    def testParseCommand_DISP_GRAP_COL1(self):
        self.assertEqual(self.parser.parseCommand('DISP:GRAP:COL?'), ('DISP:GRAP:COL?', []))
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL? red')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL? 0x111111')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL? 0 0xFFFFFF')

    def testParseCommand_DISP_GRAP_COL2(self):
        self.assertEqual(self.parser.parseCommand('DISP:GRAP:COL 0 0x000000'), ('DISP:GRAP:COL', [0, '0x000000']))
        self.assertEqual(self.parser.parseCommand('DISP:GRAP:COL 31 0x0'), ('DISP:GRAP:COL', [31, '0x0']))
        self.assertEqual(self.parser.parseCommand('DISP:GRAP:COL 20 0x9F9F0F'), ('DISP:GRAP:COL', [20, '0x9F9F0F']))

        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL -1 0x000000')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL 32 0x000000')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL 10 0xg00000')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL 1 red')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:GRAP:COL 10 0x000000 1')

    def testParseCommand_SENS_CORR(self):
        self.assertEqual(self.parser.parseCommand('SENS:CORR?'), ('SENS:CORR?', []))
        self.assertEqual(self.parser.parseCommand('SENSor:CORRection?'), ('SENS:CORR?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:CORR? correction')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:CORR? 0')

    def testParseCommand_SYST_HELP(self):
        self.assertEqual(self.parser.parseCommand('SYST:HELP?'), ('SYST:HELP?', []))
        self.assertEqual(self.parser.parseCommand('SYSTem:HELP?'), ('SYST:HELP?', []))
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:HELP? help')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:HELP')

    def testParseCommand_MEAS_TRIG(self):
        self.assertEqual(self.parser.parseCommand('MEAS:TRIG -200'), ('MEAS:TRIG', [-200]))
        self.assertEqual(self.parser.parseCommand('MEASure:TRIGger -200'), ('MEAS:TRIG', [-200]))
        self.assertEqual(self.parser.parseCommand('MEAS:TRIG 10'), ('MEAS:TRIG', [10]))
        self.assertEqual(self.parser.parseCommand('MEAS:TRIG auto'),('MEAS:TRIG', ['auto']))
        self.assertEqual(self.parser.parseCommand('MEAS:TRIG normal'), ('MEAS:TRIG', ['normal']))
        self.assertEqual(self.parser.parseCommand('MEAS:TRIG single'), ('MEAS:TRIG', ['single']))

        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:TRIG')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:TRIG -201')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:TRIG 11')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:TRIG high')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:TRIG 1.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:TRIG 10 auto')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:TRIG single 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:TRIG 1 1')

    def testParseCommand_SOUR_POW_LEV_IMM_AMPL(self):
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL -76'), ('SOUR:POW:LEV:IMM:AMPL', [-76]))
        self.assertEqual(self.parser.parseCommand('SOURce:POWer:LEVel:IMMediate:AMPL -76'), ('SOUR:POW:LEV:IMM:AMPL', [-76]))
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 13'), ('SOUR:POW:LEV:IMM:AMPL', [13]))
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 0'), ('SOUR:POW:LEV:IMM:AMPL', [0]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL -77')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 14')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 12.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL auto')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL 1 1')

    def testParseCommand_SOUR_POW_LEV_IMM_AMPL_OFFS(self):
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS 0'),('SOUR:POW:LEV:IMM:AMPL:OFFS', [0]))
        self.assertEqual(self.parser.parseCommand('SOURce:POW:LEVel:IMM:AMPL:OFFS 0'), ('SOUR:POW:LEV:IMM:AMPL:OFFS', [0]))
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS 70'), ('SOUR:POW:LEV:IMM:AMPL:OFFS', [70]))
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS -70'), ('SOUR:POW:LEV:IMM:AMPL:OFFS', [-70]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS -71')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS 71')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS On')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS 7.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFFS 1 1')

    def testParseCommand_FREQ_OFFS(self):
        self.assertEqual(self.parser.parseCommand('FREQ:OFFS?'), ('FREQ:OFFS?', []))
        self.assertEqual(self.parser.parseCommand('FREQuency:OFFS?'), ('FREQ:OFFS?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS? 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS? on')

    def testParseCommand_FREQ_OFFS2(self):
        self.assertEqual(self.parser.parseCommand('FREQ:OFFS low -20'), ('FREQ:OFFS', ['low', -20]))
        self.assertEqual(self.parser.parseCommand('FREQuency:OFFS low -20'), ('FREQ:OFFS', ['low', -20]))
        self.assertEqual(self.parser.parseCommand('FREQ:OFFS high 0'), ('FREQ:OFFS', ['high', 0]))
        self.assertEqual(self.parser.parseCommand('FREQ:OFFS switch 20'), ('FREQ:OFFS', ['switch', 20]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS 20')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS low')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS 20 switch')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS 20 20')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS low switch')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS low 21')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS high -21')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS high 1.3')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS on 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('FREQ:OFFS 20 low on')

    def testParseCommand_SYST_PRES(self):
        self.assertEqual(self.parser.parseCommand('SYST:PRES 0'), ('SYST:PRES', [0]))
        self.assertEqual(self.parser.parseCommand('SYSTem:PRESet 1'), ('SYST:PRES', [1]))
        self.assertEqual(self.parser.parseCommand('SYSTem:PRESet 4'), ('SYST:PRES', [4]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:PRES')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:PRES -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:PRES 1.2')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:PRES 5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:PRES preset')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:PRES 2 1')

    def testParseCommand_SOUR_DM_FORM(self):
        self.assertEqual(self.parser.parseCommand('SOUR:DM:FORM off'), ('SOUR:DM:FORM', ['off']))
        self.assertEqual(self.parser.parseCommand('SOURce:DM:FORM AM_1kHz'), ('SOUR:DM:FORM', ['AM_1kHz']))
        self.assertEqual(self.parser.parseCommand('SOUR:DM:FORM AM_10Hz'), ('SOUR:DM:FORM', ['AM_10Hz']))
        self.assertEqual(self.parser.parseCommand('SOUR:DM:FORM NFM'), ('SOUR:DM:FORM', ['NFM']))
        self.assertEqual(self.parser.parseCommand('SOURce:DM:FORM WFM'), ('SOUR:DM:FORM', ['WFM']))
        self.assertEqual(self.parser.parseCommand('SOUR:DM:FORM extern'), ('SOUR:DM:FORM', ['extern']))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:DM:FORM')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:DM:FORM on')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:DM:FORM 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:DM:FORM 1.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:DM:FORM off off')

    def testParseCommand_SOUR_POW_AMPL(self):
        self.assertEqual(self.parser.parseCommand('SOUR:POW:AMPL -100'), ('SOUR:POW:AMPL', [-100]))
        self.assertEqual(self.parser.parseCommand('SOURce:POW:AMPLlitude 100'), ('SOUR:POW:AMPL', [100]))
        self.assertEqual(self.parser.parseCommand('SOURce:POW:AMPLlitude 0'), ('SOUR:POW:AMPL', [0]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:AMPL')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:AMPL 101')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:AMPL -101')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:AMPL 5.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:AMPL max')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:AMPL 50 50')

    def testParseCommand_OUTP(self):
        self.assertEqual(self.parser.parseCommand('OUTP ON'), ('OUTP', ['ON']))
        self.assertEqual(self.parser.parseCommand('OUTPut OFF'), ('OUTP', ['OFF']))

        with self.assertRaises(Exception):
            self.parser.parseCommand('OUTP')
        with self.assertRaises(Exception):
            self.parser.parseCommand('OUTP 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('OUTP True')
        with self.assertRaises(Exception):
            self.parser.parseCommand('OUTP ON ON')

    def testParseCommand_PROG_SEL_STAT_PAUS(self):
        self.assertEqual(self.parser.parseCommand('PROG:SELect:STAT:PAUSe'), ('PROG:SEL:STAT:PAUS', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('PROG:SEL:STAT:PAUS On')
        with self.assertRaises(Exception):
            self.parser.parseCommand('PROG:SEL:STAT:PAUS 1')

    def testParseCommand_HCOP_SDUM_DATA(self):
        self.assertEqual(self.parser.parseCommand('HCOP:SDUM:DATA?'), ('HCOP:SDUM:DATA?', []))
        self.assertEqual(self.parser.parseCommand('HCOP:SDUMp:DATA?'), ('HCOP:SDUM:DATA?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('HCOP:SDUM:DATA')
        with self.assertRaises(Exception):
            self.parser.parseCommand('HCOP:SDUM:DATA? 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('HCOP:SDUM:DATA? True')
        with self.assertRaises(Exception):
            self.parser.parseCommand('HCOP:SDUM:DATA? 0.1')

    def testParseCommand_SOUR_VOLT_LEV_IMM_AMPL(self):
        self.assertEqual(self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL?'), ('SOUR:VOLT:LEV:IMM:AMPL?', []))
        self.assertEqual(self.parser.parseCommand('SOUR:VOLTage:LEVel:IMM:AMPL?'), ('SOUR:VOLT:LEV:IMM:AMPL?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL? 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL? True')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL? 1.1')

    def testParseCommand_SOUR_VOLT_LEV_IMM_AMPL2(self):
        self.assertEqual(self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL 0'), ('SOUR:VOLT:LEV:IMM:AMPL', [0]))
        self.assertEqual(self.parser.parseCommand('SOURce:VOLTage:LEV:IMM:AMPL 4096'), ('SOUR:VOLT:LEV:IMM:AMPL', [4096]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL 4097')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL 1.02')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL Default')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:VOLT:LEV:IMM:AMPL 1 2')

    def testParseCommand_TRAC_DATA(self):
        self.assertEqual(self.parser.parseCommand('TRAC:DATA? 0'), ('TRAC:DATA?', [0]))
        self.assertEqual(self.parser.parseCommand('TRACe:DATA? 1'), ('TRAC:DATA?', [1]))
        self.assertEqual(self.parser.parseCommand('TRAC:DATA? 2'), ('TRAC:DATA?', [2]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:DATA?')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:DATA 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:DATA? 1.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:DATA? -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:DATA? 3')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:DATA? One')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:DATA? 1 1')

    def testParseCommand_MARK_LEV(self):
        self.assertEqual(self.parser.parseCommand('MARK:LEV?'), ('MARK:LEV?', []))
        self.assertEqual(self.parser.parseCommand('MARK:LEVel?'), ('MARK:LEV?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV? 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV? 1.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV? One')

    def testParseCommand_MARK_LEV2(self):
        self.assertEqual(self.parser.parseCommand('MARK:LEV 1 0'), ('MARK:LEV', [1, 0]))
        self.assertEqual(self.parser.parseCommand('MARK:LEVel 2 355'), ('MARK:LEV', [2, 355]))
        self.assertEqual(self.parser.parseCommand('MARKer:LEV 3 on'), ('MARK:LEV', [3, 'on']))
        self.assertEqual(self.parser.parseCommand('MARK:LEV 4 off'), ('MARK:LEV', [4, 'off']))

        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV on')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV -1 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV 5 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV 2.5 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV on 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV 1 -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV 1 366')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV 1 300.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV 1 True')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MARK:LEV 1 1 1')

    def testParseCommand_DISP_ENAB(self):
        self.assertEqual(self.parser.parseCommand('DISP:ENAB ON'), ['DISP:ENAB', True])
        self.assertEqual(self.parser.parseCommand('DISPlay:ENAB OFF'), ['DISP:ENAB', False])
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:ENAB')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:ENAB on')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:ENAB one')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:ENAB 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:ENAB 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:ENAB ON 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:ENAB ON OFF')

    def testParseCommand_PROG_SEL_STAT_RESU(self):
        self.assertEqual(self.parser.parseCommand('PROG:SEL:STAT:RESU'), ('PROG:SEL:STAT:RESU', []))
        self.assertEqual(self.parser.parseCommand('PROG:SELelct:STAT:RESUme'), ('PROG:SEL:STAT:RESU', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('PROG:SEL:STAT:RESU?')
        with self.assertRaises(Exception):
            self.parser.parseCommand('PROG:SEL:STAT:RESU True')
        with self.assertRaises(Exception):
            self.parser.parseCommand('PROG:SEL:STAT:RESU 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('PROG:SEL:STAT:RESU 1.2')

    def testParseCommand_TRAC_MEM_SAVE(self):
        self.assertEqual(self.parser.parseCommand('TRAC:MEM:SAVE 0'), ('TRAC:MEM:SAVE', [0]))
        self.assertEqual(self.parser.parseCommand('TRAC:MEMory:SAVE 4'), ('TRAC:MEM:SAVE', [4]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:MEM:SAVE')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:MEM:SAVE -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:MEM:SAVE 5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:MEM:SAVE 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:MEM:SAVE save')
        with self.assertRaises(Exception):
            self.parser.parseCommand('TRAC:MEM:SAVE 1 1')

    def testParseCommand_SYST_SAVE(self):
        self.assertEqual(1, 1)
        #TODO: WHAT IS THIS

    def testParseCommand_SYST_SER(self):
        self.assertEqual(self.parser.parseCommand('SYST:SER?'), ('SYST:SER?', []))
        self.assertEqual(self.parser.parseCommand('SYSTem:SER?'), ('SYST:SER?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:SER')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:SER? True')

    def testParseCommand_SYST_SER2(self):
        self.assertEqual(1, 1)
        #TODO: WHAT IS THIS

    def testParseCommand_CONF(self):
        self.assertEqual(self.parser.parseCommand('CONF off'), ('CONF', ['off']))
        self.assertEqual(self.parser.parseCommand('CONFig minh'), ('CONF', ['minh']))
        self.assertEqual(self.parser.parseCommand('CONF maxh'), ('CONF', ['maxh']))
        self.assertEqual(self.parser.parseCommand('CONFiguration maxd'), ('CONF', ['maxd']))
        self.assertEqual(self.parser.parseCommand('CONF aver4'), ('CONF', ['aver4']))
        self.assertEqual(self.parser.parseCommand('CONF aver16'), ('CONF', ['aver16']))
        self.assertEqual(self.parser.parseCommand('CONF quasi'), ('CONF', ['quasi']))

        with self.assertRaises(Exception):
            self.parser.parseCommand('CONF')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CONF on')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CONF 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CONF 1.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CONF minh maxh')
    def testParseCommand_DISP_DATA_START(self):
        self.assertEqual(self.parser.parseCommand('DISP:DATA:START 0, 0'), ('DISP:DATA:START', [0, 0]))
        self.assertEqual(self.parser.parseCommand('DISPlay:DATA:START 0, 240'), ('DISP:DATA:START', [0, 240]))
        self.assertEqual(self.parser.parseCommand('DISPlay:DATA:START 360, 240'), ('DISP:DATA:START', [360, 240]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START -1 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START 0 -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START 321 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START 0 241')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START 5.5 5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START 5 5.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START True')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:START 320 240 1')

    def testParseCommand_DISP_DATA_STOP(self):
        self.assertEqual(self.parser.parseCommand('DISPl:DATA:STOP 0, 0'), ('DISPl:DATA:STOP', [0, 0]))
        self.assertEqual(self.parser.parseCommand('DISPlay:DATA:STOP 0, 240'), ('DISPl:DATA:STOP', [0, 240]))
        self.assertEqual(self.parser.parseCommand('DISPlay:DATA:STOP 360, 240'), ('DISPl:DATA:STOP', [360, 240]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP -1 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP 0 -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP 321 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP 0 241')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP 5.5 5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP 5 5.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP True')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISPlay:DATA:STOP 320 240 1')

    def testParseCommand_DISP_DATA_WIDTH(self):
        self.assertEqual(self.parser.parseCommand('DISP:DATA:WIDTH 0'), ('DISP:DATA:WIDTH', [0]))
        self.assertEqual(self.parser.parseCommand('DISPlay:DATA:WIDTH 320'), ('DISP:DATA:WIDTH', [320]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:WIDTH')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:WIDTH -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:WIDTH 321')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:WIDTH 4.0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:WIDTH Default')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:WIDTH 1 1')

    def testParseCommand_DISP_DATA_HEIGHT(self):
        self.assertEqual(self.parser.parseCommand('DISP:DATA:HEIGHT 0'), ('DISP:DATA:HEIGHT', [0]))
        self.assertEqual(self.parser.parseCommand('DISPlay:DATA:HEIGHT 240'), ('DISP:DATA:HEIGHT', [240]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:HEIGHT')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:HEIGHT -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:HEIGHT 241')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:HEIGHT 4.0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:HEIGHT Default')
        with self.assertRaises(Exception):
            self.parser.parseCommand('DISP:DATA:HEIGHT 1 1')

    def testParseCommand_DISP_DATA_TYPE(self):
        self.assertEqual(1, 1)
        #TODO: see valid dictionary

    def testParseCommand_CALC_MEAS_PN_SPUR_OMIS_STAT(self):
        self.assertEqual(self.parser.parseCommand('CALC:MEAS:PN:SPUR:OMIS:STAT on'), ('CALC:MEAS:PN:SPUR:OMIS:STAT', ['on']))
        self.assertEqual(self.parser.parseCommand('CALCulate:MEASure:PN:SPUR:OMIS:STAT off'), ('CALC:MEAS:PN:SPUR:OMIS:STAT', ['off']))

        with self.assertRaises(Exception):
            self.parser.parseCommand('CALC:MEAS:PN:SPUR:OMIS:STAT')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CALC:MEAS:PN:SPUR:OMIS:STAT 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CALC:MEAS:PN:SPUR:OMIS:STAT 1.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CALC:MEAS:PN:SPUR:OMIS:STAT start')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CALC:MEAS:PN:SPUR:OMIS:STAT on on')

    def testParseCommand_SENS_FREQ_STAR_STOP_DATA(self):
        self.assertEqual(self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 0 0'), ('SENS:FREQ:STAR:STOP:DATA', [0, 0]))
        self.assertEqual(self.parser.parseCommand('SENS:FREQuency:STAR:STOP:DATA 1000000000 0'), ('SENS:FREQ:STAR:STOP:DATA', [1000000000, 0]))
        self.assertEqual(self.parser.parseCommand('SENSe:FREQ:STARt:STOP:DATA 0 1000000000'), ('SENS:FREQ:STAR:STOP:DATA', [0, 1000000000]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 11.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA data')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA -1 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 0 -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 1000000001 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 0 1000000001')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 0 1.1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 1.1 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 1 raw')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA raw 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SENS:FREQ:STAR:STOP:DATA 0 1 2')

    def testParseCommand_SOUR_POW_LEV_IMM_AMPL_OFF(self):
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFF 70'), ('SOUR:POW:LEV:IMM:AMPL:OFF', [70]))
        self.assertEqual(self.parser.parseCommand('SOUR:POWer:LEV:IMM:AMPLlitude:OFF 0'), ('SOUR:POW:LEV:IMM:AMPL:OFF', [0]))
        self.assertEqual(self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFF -70'), ('SOUR:POW:LEV:IMM:AMPL:OFF', [-70]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFF')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFF -71')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFF 71')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFF 3.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFF on')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SOUR:POW:LEV:IMM:AMPL:OFF 20 30')

    def testParseCommand_SYST_VERS(self):
        self.assertEqual(self.parser.parseCommand('SYST:VERS?'), ('SYST:VERS?', []))
        self.assertEqual(self.parser.parseCommand('SYSTem:VERSion?'), ('SYST:VERS?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS? new')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS? 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS? 1.5')

    def testParseCommand_SYST_MODE(self):
        self.assertEqual(self.parser.parseCommand('SYST:MODE low input'), ('SYST:MODE', ['low', 'input']))
        self.assertEqual(self.parser.parseCommand('SYSTem:MODE low output'), ('SYST:MODE', ['low', 'output']))
        self.assertEqual(self.parser.parseCommand('SYST:MODE high input'), ('SYST:MODE', ['high', 'input']))
        self.assertEqual(self.parser.parseCommand('SYSTem:MODE high output'), ('SYST:MODE', ['high', 'output']))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE?')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE low')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE low low')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE med input')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE low 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE high 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:MODE low input turbo')

    def testParseCommand_MEAS_SWE_BEG_LOW(self):
        self.assertEqual(self.parser.parseCommand('MEAS:SWE:BEG:LOW 0 0 0'), ('MEAS:SWE:BEG:LOW', [0, 0, 0]))
        self.assertEqual(self.parser.parseCommand('MEASure:SWE:BEG:LOW 350000000 0 0'), ('MEAS:SWE:BEG:LOW', [350000000, 0, 0]))
        self.assertEqual(self.parser.parseCommand('MEAS:SWEep:BEGin:LOW 0 350000000 0'), ('MEAS:SWE:BEG:LOW', [0, 350000000, 0]))
        self.assertEqual(self.parser.parseCommand('MEAS:SWE:BEG:LOW 0 0 290'), ('MEAS:SWE:BEG:LOW', [0, 0, 290]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 100')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW range')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 100 200')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 100 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 100 on')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW -1 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 0 -1 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 0 0 -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 350000001 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 0 350000001 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 0 0 291')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:LOW 0 0 0 0')

    def testParseCommand_MEAS_SWE_BEG_HIGH(self):
        self.assertEqual(self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000 240000000 0'), ('MEAS:SWE:BEG:HIGH', [240000000, 240000000, 0]))
        self.assertEqual(self.parser.parseCommand('MEAS:SWEep:BEGin:HIGH 959000000 240000000 0'), ('MEAS:SWE:BEG:HIGH', [959000000, 240000000, 0]))
        self.assertEqual(self.parser.parseCommand('MEASure:SWE:BEG:HIGH 240000000 959000000 0'), ('MEAS:SWE:BEG:HIGH', [240000000, 959000000, 0]))
        self.assertEqual(self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000 240000000 290'), ('MEAS:SWE:BEG:HIGH', [240000000, 240000000, 290]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH range')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000 240000000')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000 240000001.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000 on')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 239999999 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 0 239999999 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 0 0 -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 959000001 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 0 959000001 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 0 0 291')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000 240000000 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:BEG:HIGH 240000000 240000000 0 959000000')

    def testParseCommand_MEAS_SWE_TIME(self):
        self.assertEqual(self.parser.parseCommand('MEAS:SWE:TIME 0'), ('MEAS:SWE:TIME', [0]))
        self.assertEqual(self.parser.parseCommand('MEASure:SWEep:TIME 600'), ('MEAS:SWE:TIME', [600]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:TIME')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:TIME -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:TIME 601')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:TIME 300.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:TIME one')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SWE:TIME 1 1')

    def testParseCommand_MEAS_SCAN_RAW_START(self):
        self.assertEqual(self.parser.parseCommand('MEAS:SCAN:RAW:START 0 0 0'), ('MEAS:SCAN:RAW:START', [0, 0, 0]))
        self.assertEqual(self.parser.parseCommand('MEASure:SCAN:RAW:START 350000000 0 0'), ('MEAS:SCAN:RAW:START', [350000000, 0, 0]))
        self.assertEqual(self.parser.parseCommand('MEASure:SCAN:RAW:START 0 350000000 0'), ('MEAS:SCAN:RAW:START', [0, 350000000, 0]))
        self.assertEqual(self.parser.parseCommand('MEAS:SCAN:RAW:START 0 0 2147483647'), ('MEAS:SCAN:RAW:START', [0, 0, 2147483647]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 100')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START range')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 100 200')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 100 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 100 on')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START -1 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 0 -1 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 0 0 -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 350000001 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 0 350000001 0 0')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 0 0 2147483648')
        with self.assertRaises(Exception):
            self.parser.parseCommand('MEAS:SCAN:RAW:START 0 0 0 0')

    def testParseCommand_CAPT(self):
        self.assertEqual(self.parser.parseCommand('CAPT'), ('CAPT', []))
        self.assertEqual(self.parser.parseCommand('CAPTure'), ('CAPT', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('CAPT?')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CAPT 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CAPT 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('CAPT on')

    def testParseCommand_SYST_THREAD(self):
        self.assertEqual(self.parser.parseCommand('SYST:THREAD?'), ('SYST:THREAD?', []))
        self.assertEqual(self.parser.parseCommand('SYSTem:THREADs?'), ('SYST:THREAD?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:THREAD')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:THREAD? 1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:THREAD? 1.5')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:THREAD? all')

    def testParseCommand_SYST_VOLT_DC_OFFS(self):
        self.assertEqual(self.parser.parseCommand('SYST:VOLT:DC:OFFS 0'), ('SYST:VOLT:DC:OFFS', [0]))
        self.assertEqual(self.parser.parseCommand('SYST:VOLTage:DC:OFFSet 4095'), ('SYST:VOLT:DC:OFFS', [4095]))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VOLT:DC:OFFS')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VOLT:DC:OFFS -1')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VOLT:DC:OFFS 4096')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VOLT:DC:OFFS 5.2')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VOLT:DC:OFFS default')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VOLT:DC:OFFS 1 2')

    def testParseResult(self):
        self.assertEqual(1, 1)
        #TODO: Unimplemented Method Stub





if __name__ == '__main__':
    unittest.main()
