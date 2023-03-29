import scpi_parser
import unittest
class ParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = scpi_parser.SCPI_Parser()
        #TODO: Unimplemented Method Stub

    def testParseCommand(self):
        self.assertEqual(self.parser.parseCommand('*IDN?'), ('*IDN?',[]))
        self.assertEqual(self.parser.parseCommand('BAND:RES 1'), ('BAND:RES', [1]))
        with self.assertRaises(KeyError):
            self.parser.parseCommand('*IDN')
        with self.assertRaises(ValueError):
            self.parser.parseCommand('BAND:RES str')
        with self.assertRaises(SyntaxError):
            self.parser.parseCommand('BAND:RES')
        #TODO: Unimplemented Method Stub

    def testParseResult(self):
        self.assertEqual(1, 1)
        #TODO: Unimplemented Method Stub

if __name__ == '__main__':
    unittest.main()
