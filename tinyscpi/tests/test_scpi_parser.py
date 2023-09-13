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

        # TODO: Alias Testing, this line currently fails
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

        # TODO: Alias Testing, this line currently fails
        self.assertEqual(self.parser.parseCommand('SYSTem:VERSion?'), ('SYST:VERS?', []))

        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS')
        with self.assertRaises(Exception):
            self.parser.parseCommand('SYST:VERS? 1')


    def testParseCommand_AMPL_ATT(self):
        self.assertEqual(self.parser.parseCommand('AMPL:ATT 0'), ('AMPL:ATT', [0]))
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

        # TODO: Alias Testing, this line currently fails
        self.assertEqual(self.parser.parseCommand('AMPLitude:ATTenuation 0'), ('AMPL:ATT', [0]))

    def testParseCommand_AMPL_ATT_AUTO(self):
        self.assertEqual(self.parser.parseCommand('AMPL:ATT:AUTO'), ('AMPL:ATT:AUTO', []))
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL_ATT_AUTO On')
        with self.assertRaises(Exception):
            self.parser.parseCommand('AMPL_ATT_AUT')

        # TODO: Alias Testing, this line currently fails
        self.assertEqual(self.parser.parseCommand('AMPLitude:ATTenuation:AUTO'), ('AMPL:ATT:AUTO', []))

    def testParseCommand_SOUR_POW_LEV_IMM_AMPL(self):
        #self.assertEqual(self.parser.parseCommand('SOURce:POWer:LEVel:IMMediate:AMPLitude OFF'), ('SOUR:POW:LEV:IMM:AMPL', ['off']))
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
        self.assertEqual(self.parser.parseCommand('MEAS:TRIG -200'), ('MEAS:TRIG', ['-200']))
        self.assertEqual(self.parser.parseCommand('MEASure:TRIGger -200'), ('MEAS:TRIG', ['-200']))
        self.assertEqual(self.parser.parseCommand('MEAS:TRIG 10'), ('MEAS:TRIG', ['10']))
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



    def testParseResult(self):
        self.assertEqual(1, 1)
        #TODO: Unimplemented Method Stub

if __name__ == '__main__':
    unittest.main()