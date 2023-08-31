import tinyscpi
import unittest

class ParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = tinyscpi.tinySCPI.scpi_parser.SCPI_Parser()
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
        self.assertEqual(self.parser.parseCommand('DISPlay:GRAPhics:COLor 3 0x000000'), ('DISPlay:GRAPhics:COLor', [3, '0x000000']))
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
        self.assertEqual(self.parser.parseCommand('SOURce:POWer:LEVel:IMMediate:AMPLitude OFF'), ('SOUR:POW:LEV:IMM:AMPL', ['off']))
        self.assertEqual(self.parser.parseCommand('SOURce:POWer:LEVel:IMMediate:AMPLitude 30'), ('SOUR:POW:LEV:IMM:AMPL', ['30']))



    def testParseResult(self):
        self.assertEqual(1, 1)
        #TODO: Unimplemented Method Stub

if __name__ == '__main__':
    unittest.main()