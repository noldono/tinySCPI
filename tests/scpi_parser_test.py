import unittest

import tinyscpi.scpi_parser


class ParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = tinyscpi.scpi_parser.SCPI_Parser()
        # TODO: Unimplemented Method Stub

    def testParseCommand(self):
        self.assertEqual(self.parser.parseCommand('*IDN?'), ('*IDN?', []))
        self.assertEqual(self.parser.parseCommand('BAND:RES 3'), ('BAND:RES', [3]))
        with self.assertRaises(KeyError):
            self.parser.parseCommand('*IDN')
        with self.assertRaises(ValueError):
            self.parser.parseCommand('BAND:RES str')
        with self.assertRaises(SyntaxError):
            self.parser.parseCommand('BAND:RES')
        self.assertEqual(self.parser.parseCommand('DISPlay:GRAPhics:COLor 3 0x000000'),
                         ('DISPlay:GRAPhics:COLor', [3, '0x000000']))
        # TODO: Unimplemented Method Stub

    def testParseResult(self):
        self.assertEqual(1, 1)
        # TODO: Unimplemented Method Stub


if __name__ == '__main__':
    unittest.main()
