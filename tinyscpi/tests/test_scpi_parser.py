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

    def testParseResult(self):
        self.assertEqual(1, 1)
        #TODO: Unimplemented Method Stub

if __name__ == '__main__':
    unittest.main()