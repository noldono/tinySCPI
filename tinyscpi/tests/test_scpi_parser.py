from tinyscpi import scpi_parser
import unittest


class ParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = scpi_parser.SCPI_Parser()

    '''
    test empty string
    '''
    def testBasics(self) -> None:
        with self.assertRaises(Exception):
            self.parser.parse_command('')

    ''' test *IDN? command '''
    def test_parse_command_IDN(self) -> None:
        self.assertEqual(self.parser.parse_command('*IDN?'), ('*IDN?', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*IDN')
        with self.assertRaises(Exception):
            self.parser.parse_command('*IDN? on')
        with self.assertRaises(Exception):
            self.parser.parse_command('*IDN? 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('*IDN? 1.1')

    ''' test *RST command '''
    def test_parse_command_RST(self) -> None:
        self.assertEqual(self.parser.parse_command('*RST'), ('*RST', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*RST?')
        with self.assertRaises(Exception):
            self.parser.parse_command('*RST factory')
        with self.assertRaises(Exception):
            self.parser.parse_command('*RST 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('*RST 3.1')

    ''' test *CLR command '''
    def test_parse_command_CLR(self) -> None:
        self.assertEqual(self.parser.parse_command('*CLR'), ('*CLR', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*CLR?')
        with self.assertRaises(Exception):
            self.parser.parse_command('*CLR clear')
        with self.assertRaises(Exception):
            self.parser.parse_command('*CLR 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('*CLR 3.5')

    ''' test *TST command '''
    def test_parse_command_TST(self) -> None:
        self.assertEqual(self.parser.parse_command('*TST?'), ('*TST?', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*TST')
        with self.assertRaises(Exception):
            self.parser.parse_command('*TST? all')
        with self.assertRaises(Exception):
            self.parser.parse_command('*TST? 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('*TST? 3.3')

    ''' test *HLP command '''
    def test_parse_command_HLP(self) -> None:
        self.assertEqual(self.parser.parse_command('*HLP'), ('*HLP', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*HLP?')
        with self.assertRaises(Exception):
            self.parser.parse_command('*HLP show')
        with self.assertRaises(Exception):
            self.parser.parse_command('*HLP 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('*HLP 2.2')

    ''' test SYST:DAC command'''
    def test_parse_command_SYST_DAC(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:DAC'), ('SYST:DAC', []))
        self.assertEqual(self.parser.parse_command('SYSTem:DAC'), ('SYST:DAC', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:DAC?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:DAC 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:DAC 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:DAC off')

    ''' test SYST:ID command'''
    def test_parse_command_SYST_ID(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:ID'), ('SYST:ID', []))
        self.assertEqual(self.parser.parse_command('SYSTem:ID'), ('SYST:ID', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:ID?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:ID 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:ID 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:ID off')

    ''' test SYST_VERS command '''
    def test_parse_command_SYST_VERS(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:VERS'), ('SYST:VERS', []))
        self.assertEqual(self.parser.parse_command('SYSTem:VERSion'), ('SYST:VERS', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:VERS?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:VERS 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:VERS 2.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:VERS new')

    ''' test SYST_MODE_LOW_IN command '''
    def test_parse_command_SYST_MODE_LOW_IN(self)->None:
        self.assertEqual(self.parser.parse_command('SYST:MODE:LOW:IN'), ('SYST:MODE:LOW:IN', []))
        self.assertEqual(self.parser.parse_command('SYSTem:MODE:LOW:IN'), ('SYST:MODE:LOW:IN', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:LOW:IN?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:LOW:IN 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:LOW:IN 0.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:LOW:IN on')

    ''' test SYST_MODE_HIGH_IN command '''
    def test_parse_command_SYST_MODE_HIGH_IN(self)-> None:
        self.assertEqual(self.parser.parse_command('SYST:MODE:HIGH:IN'), ('SYST:MODE:HIGH:IN', []))
        self.assertEqual(self.parser.parse_command('SYSTem:MODE:HIGH:IN'), ('SYST:MODE:HIGH:IN', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:HIGH:IN?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:HIGH:IN 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:HIGH:IN 0.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:HIGH:IN on')

    ''' test SYST_MODE_LOW_OUT command '''
    def test_parse_command_SYST_MODE_LOW_OUT(self)->None:
        self.assertEqual(self.parser.parse_command('SYST:MODE:LOW:OUT'), ('SYST:MODE:LOW:OUT', []))
        self.assertEqual(self.parser.parse_command('SYSTem:MODE:LOW:OUT'), ('SYST:MODE:LOW:OUT', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:LOW:OUT?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:LOW:OUT 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:LOW:OUT 0.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:LOW:OUT on')

    ''' test SYST_MODE_HIGH_OUT command '''
    def test_parse_command_SYST_MODE_HIGH_OUT(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:MODE:HIGH:OUT'), ('SYST:MODE:HIGH:OUT', []))
        self.assertEqual(self.parser.parse_command('SYSTem:MODE:HIGH:OUT'), ('SYST:MODE:HIGH:OUT', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:HIGH:OUT?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:HIGH:OUT 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:HIGH:OUT 0.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:MODE:HIGH:OUT on')

    ''' test SYST_VBAT command '''
    def test_parse_command_SYST_VBAT(self)->None:
        self.assertEqual(self.parser.parse_command('SYST:VBAT'), ('SYST:VBAT', []))
        self.assertEqual(self.parser.parse_command('SYSTem:VBAT'), ('SYST:VBAT', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:VBAT?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:VBAT 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:VBAT 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:VBAT off')

    ''' test SYST_SAVE command '''
    def test_parse_command_SYST_SAVE(self)->None:
        self.assertEqual(self.parser.parse_command('SYST:SAVE 0'), ('SYST:SAVE', [0]))
        self.assertEqual(self.parser.parse_command('SYSTem:SAVE 4'), ('SYST:SAVE', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SAVE')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SAVE:-1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SAVE 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SAVE default')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SAVE 0.2')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SAVE 1 2')

    ''' test SYST_SCONF command '''
    def test_parse_command_SYST_SCONF(self)->None:
        self.assertEqual(self.parser.parse_command('SYST:SCONF'), ('SYST:SCONF', []))
        self.assertEqual(self.parser.parse_command('SYSTem:SCONFiguration'), ('SYST:SCONF', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SCONF?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SCONF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SCONF 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:SCONF off')

    ''' test SYST_TCAL command '''
    def test_parse_command_SYST_TCAL(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:TCAL'), ('SYST:TCAL', []))
        self.assertEqual(self.parser.parse_command('SYSTem:TCALibration'), ('SYST:TCAL', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:TCAL?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:TCAL 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:TCAL 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:TCAL off')

    ''' test SYST_TTEST command '''
    def test_parse_command_SYST_TTEST(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:TTEST'), ('SYST:TTEST', []))
        self.assertEqual(self.parser.parse_command('SYSTem:TouchTEST'), ('SYST:TTEST', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:TTEST?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:TTEST 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:TTEST 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:TTEST off')

    ''' test SYST_THRE command '''
    def test_parse_command_SYST_THRE(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:THRE'), ('SYST:THRE', []))
        self.assertEqual(self.parser.parse_command('SYSTem:THREshold'), ('SYST:THRE', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:THRE?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:THRE 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:THRE 2.3')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:THRE off')

    ''' test SYST_STEST command '''
    def test_parse_command_SYST_STEST(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:STEST'), ('SYST:STEST', []))
        self.assertEqual(self.parser.parse_command('SYSTem:SelfTEST'), ('SYST:STEST', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:STEST?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:STEST 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:STEST 0.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:STEST off')

    ''' test SYST_OFFS command '''
    def test_parse_command_SYST_OFFS(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:OFFS 0'), ('SYST:OFFS', [0]))
        self.assertEqual(self.parser.parse_command('SYSTem:OFFSet 4095'), ('SYST:OFFS', [4095]))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:OFFS?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:OFFS -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:OFFS 4096')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:OFFS default')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:OFFS 0.2')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:OFFS 1 2')

    ''' test SYST_CLRCONF command '''
    def test_parse_command_SYST_CLRCONF(self) -> None:
        self.assertEqual(self.parser.parse_command('SYST:CLRCONF'), ('SYST:CLRCONF', []))
        self.assertEqual(self.parser.parse_command('SYSTem:CLeaRCONFiguration'), ('SYST:CLRCONF', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:CLRCONF?')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:CLRCONF 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:CLRCONF 0.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('SYST:CLRCONF off')

    ''' test FREQ:START command '''
    def test_parse_command_FREQ_START(self):
        self.assertEqual(self.parser.parse_command('FREQ:START 0'), ('FREQ:START', [0]))
        self.assertEqual(self.parser.parse_command('FREQuency:START 959000000'), ('FREQ:START', [959000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START 959000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START start')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START 5.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START 1 1')

    ''' test FREQ:STOP command '''
    def test_parse_command_FREQ_STOP(self):
        self.assertEqual(self.parser.parse_command('FREQ:STOP 0'), ('FREQ:STOP', [0]))
        self.assertEqual(self.parser.parse_command('FREQuency:STOP 959000000'), ('FREQ:STOP', [959000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP 959000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP default')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP 959000.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP 340000000 959000000')

    ''' test FREQ:CENT command '''
    def test_parse_command_FREQ_CENT(self):
        self.assertEqual(self.parser.parse_command('FREQ:CENT 0'), ('FREQ:CENT', [0]))
        self.assertEqual(self.parser.parse_command('FREQuency:CENTer 959000000'), ('FREQ:CENT', [959000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT 959000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT peak')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT 100000.02')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT 0 0')

    ''' test FREQ:SPAN command '''
    def test_parse_command_FREQ_SPAN(self):
        self.assertEqual(self.parser.parse_command('FREQ:SPAN 0'), ('FREQ:SPAN', [0]))
        self.assertEqual(self.parser.parse_command('FREQuency:SPAN 290'),
                         ('FREQ:SPAN', [290]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN 959000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN span')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN 5.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN 1 1')

    ''' test FREQ:SPAN:ZERO command '''
    def test_parse_command_FREQ_SPAN_ZERO(self):
        self.assertEqual(self.parser.parse_command('FREQ:SPAN:ZERO'), ('FREQ:SPAN:ZERO', []))
        self.assertEqual(self.parser.parse_command('FREQuency:SPAN:ZERO'), ('FREQ:SPAN:ZERO', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN:ZERO?')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN:ZERO 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN:ZERO zero')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN:ZERO 3.5')

    ''' test FREQ:RBW command '''
    def test_parse_command_FREQ_RBW(self):
        self.assertEqual(self.parser.parse_command('FREQ:RBW 3'), ('FREQ:RBW', ['3']))
        self.assertEqual(self.parser.parse_command('FREQuency:RBW 10'), ('FREQ:RBW', ['10']))
        self.assertEqual(self.parser.parse_command('FREQ:RBW 30'), ('FREQ:RBW', ['30']))
        self.assertEqual(self.parser.parse_command('FREQuency:RBW 100'), ('FREQ:RBW', ['100']))
        self.assertEqual(self.parser.parse_command('FREQ:RBW 300'), ('FREQ:RBW', ['300']))
        self.assertEqual(self.parser.parse_command('FREQuency:RBW 600'), ('FREQ:RBW', ['600']))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW 2')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW 601')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW 3.01')    
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW center')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW 3 600')

    ''' test FREQ:RBW:AUTO command '''
    def test_parse_command_FREQ_RBW_AUTO(self):
        self.assertEqual(self.parser.parse_command('FREQ:RBW:AUTO'), ('FREQ:RBW:AUTO', []))
        self.assertEqual(self.parser.parse_command('FREQuency:RBandWidth:AUTO'), ('FREQ:RBW:AUTO', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW:AUTO?')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW:AUTO auto')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW:AUTO 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:RBW:AUTO 1.1')

    ''' test FREQ:DUMP command '''
    def test_parse_command_FREQ_DUMP(self):
        self.assertEqual(self.parser.parse_command('FREQ:DUMP'), ('FREQ:DUMP', []))
        self.assertEqual(self.parser.parse_command('FREQuency:DUMP'), ('FREQ:DUMP', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:DUMP?')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:DUMP all')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:DUMP 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:DUMP 3.3')

    ''' test FREQ:SCAN:FREQ command '''
    def test_parse_command_FREQ_SCAN_FREQ(self):
        self.assertEqual(self.parser.parse_command('FREQ:SCAN:FREQ 0 0'), ('FREQ:SCAN:FREQ', [0, 0]))
        self.assertEqual(self.parser.parse_command('FREQuency:SCAN:FREQuency 0 959000000'),('FREQ:SCAN:FREQ', [0, 959000000]))
        self.assertEqual(self.parser.parse_command('FREQuency:SCAN:FREQuency 959000000 0'), ('FREQ:SCAN:FREQ', [959000000, 0]))
        self.assertEqual(self.parser.parse_command('FREQuency:SCAN:FREQuency 959000000 959000000'), ('FREQ:SCAN:FREQ', [959000000, 959000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:FREQ')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:FREQ 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:FREQ scan')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:FREQ -1 959000000')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:FREQ 959000001 -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:FREQ 959000001 959000000 959000000')

    ''' test FREQ:SCAN:MEAS command '''
    def test_parse_command_FREQ_SCAN_MEAS(self)->None:
        self.assertEqual(self.parser.parse_command('FREQ:SCAN:MEAS 0 0'), ('FREQ:SCAN:MEAS', [0, 0]))
        self.assertEqual(self.parser.parse_command('FREQuency:SCAN:MEASure 0 959000000'), ('FREQ:SCAN:MEAS', [0, 959000000]))
        self.assertEqual(self.parser.parse_command('FREQuency:SCAN:MEASure 959000000 0 '), ('FREQ:SCAN:MEAS', [959000000, 0]))
        self.assertEqual(self.parser.parse_command('FREQuency:SCAN:MEASure 959000000 959000000 '), ('FREQ:SCAN:MEAS', [959000000, 959000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:MEAS')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:MEAS 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:MEAS scan')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:MEAS -1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:MEAS 959000001 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:MEAS 0 -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:MEAS 0 959000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:MEAS 900001 900000 900000')

    ''' test FREQ:SCAN:STOR command '''
    def test_parse_command_FREQ_SCAN_STOR(self) -> None:
        self.assertEqual(self.parser.parse_command('FREQ:SCAN:STOR 0 0'), ('FREQ:SCAN:STOR', [0, 0]))
        self.assertEqual(self.parser.parse_command('FREQ:SCAN:STOR 959000000 0'), ('FREQ:SCAN:STOR', [959000000, 0]))
        self.assertEqual(self.parser.parse_command('FREQ:SCAN:STOR 0 959000000'), ('FREQ:SCAN:STOR', [0, 959000000]))
        self.assertEqual(self.parser.parse_command('FREQ:SCAN:STOR 959000000 959000000'), ('FREQ:SCAN:STOR', [959000000, 959000000]))


        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:STOR')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:STOR 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:STOR scan')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:STOR -1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:STOR 959000001 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:STOR 0 -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:STOR 0 959000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SCAN:STOR 900001 900000 900000')

    ''' test FREQ:IF:AUTO command '''
    def test_parse_command_FREQ_IF_AUTO(self):
        self.assertEqual(self.parser.parse_command('FREQ:IF:AUTO'), ('FREQ:IF:AUTO', []))
        self.assertEqual(self.parser.parse_command('FREQuency:IF:AUTOmatic'), ('FREQ:IF:AUTO', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF:AUTO?')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF:AUTO auto')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF:AUTO 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF:AUTO 1.1')

    ''' test FREQ:IF command '''
    def test_parse_command_FREQ_IF(self):
        self.assertEqual(self.parser.parse_command('FREQ:IF 433000000'), ('FREQ:IF', [433000000]))
        self.assertEqual(self.parser.parse_command('FREQuency:IF 435000000'), ('FREQ:IF', [435000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF 432999999')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF 435000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF 433000000.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF if')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:IF 433000000 435000000')

    ''' test LVL:ATT command '''
    def test_parse_command_LVL_ATT(self):
        self.assertEqual(self.parser.parse_command('LVL:ATT 0'), ('LVL:ATT', [0]))
        self.assertEqual(self.parser.parse_command('LeVeL:ATTenuation 30'), ('LVL:ATT', [30]))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT 31')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT default')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT 0.2')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT 1 20')

    ''' test LVL:ATT:AUTO command '''
    def test_parse_command_LVL_ATT_AUTO(self):
        self.assertEqual(self.parser.parse_command('LVL:ATT:AUTO'), ('LVL:ATT:AUTO', []))
        self.assertEqual(self.parser.parse_command('LeVeL:ATTeunuation:AUTO'), ('LVL:ATT:AUTO', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT:AUTO?')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT:AUTO auto')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT:AUTO 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT:AUTO 3.1')

    ''' test LVL_REF command '''
    def test_parse_command_LVL_REF(self):
        self.assertEqual(self.parser.parse_command('LVL:REF -100'), ('LVL:REF', [-100]))
        self.assertEqual(self.parser.parse_command('LeVeL:REFerence 100.33'), ('LVL:REF', [100.33]))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF default')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF 1.1 20.1')

    ''' test LVL:REF:AUTO command '''
    def test_parse_command_LVL_REF_AUTO(self):
        self.assertEqual(self.parser.parse_command('LVL:REF:AUTO'), ('LVL:REF:AUTO', []))
        self.assertEqual(self.parser.parse_command('LeVeL:REFerence:AUTO'), ('LVL:REF:AUTO', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF:AUTO?')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF:AUTO auto')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF:AUTO 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF:AUTO 5.5')

    ''' test LVL:SCAL command '''
    def test_parse_command_LVL_SCAL(self):
        self.assertEqual(self.parser.parse_command('LVL:SCAL 1'), ('LVL:SCAL', ['1']))
        self.assertEqual(self.parser.parse_command('LeVeL:SCALe 2'), ('LVL:SCAL', ['2']))
        self.assertEqual(self.parser.parse_command('LVL:SCAL 5'), ('LVL:SCAL', ['5']))
        self.assertEqual(self.parser.parse_command('LeVeL:SCALe 10'), ('LVL:SCAL', ['10']))
        self.assertEqual(self.parser.parse_command('LVL:SCAL 20'), ('LVL:SCAL', ['20']))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL 3')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL 3.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL scale')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL 1 20')

    ''' test LVL:SCAL:AUTO command '''
    def test_parse_command_LVL_SCAL_AUTO(self):
        self.assertEqual(self.parser.parse_command('LVL:SCAL:AUTO'), ('LVL:SCAL:AUTO', []))
        self.assertEqual(self.parser.parse_command('LeVeL:SCALe:AUTO'), ('LVL:SCAL:AUTO', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL:AUTO?')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL:AUTO auto')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL:AUTO 2')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:SCAL:AUTO 5.5')

    ''' test LVL:UNIT command '''
    def test_parse_command_LVL_UNIT(self):
        self.assertEqual(self.parser.parse_command('LVL:UNIT dBm'), ('LVL:UNIT', ['dBm']))
        self.assertEqual(self.parser.parse_command('LeVeL:UNIT dBmV'), ('LVL:UNIT', ['dBmV']))
        self.assertEqual(self.parser.parse_command('LVL:UNIT dBuV'), ('LVL:UNIT', ['dBuV']))
        self.assertEqual(self.parser.parse_command('LeVeL:UNIT V'), ('LVL:UNIT', ['V']))
        self.assertEqual(self.parser.parse_command('LVL:UNIT W'), ('LVL:UNIT', ['W']))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:UNIT?')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:UNIT 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:UNIT 2.2')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:UNIT dB')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:UNIT dBm dBmV')

    ''' test LVL:XGAIN command '''
    def test_parse_command_LVL_XGAIN(self):
        self.assertEqual(self.parser.parse_command('LVL:XGAIN 0'), ('LVL:XGAIN', [0]))
        self.assertEqual(self.parser.parse_command('LeVeL:eXtraGAIN 100'), ('LVL:XGAIN', [100]))
        self.assertEqual(self.parser.parse_command('LVL:XGAIN -100'), ('LVL:XGAIN', [-100]))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:XGAIN')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:XGAIN 101')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:XGAIN -101')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:XGAIN 0.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:XGAIN OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:XGAIN 0 100')

    ''' test TRAC:FREZ:ON command '''
    def test_parse_command_TRAC_FREZ_ON(self):
        self.assertEqual(self.parser.parse_command('TRAC:FREZ:ON 1'), ('TRAC:FREZ:ON', [1]))
        self.assertEqual(self.parser.parse_command('TRACe:FREeZe:ON 2'), ('TRAC:FREZ:ON', [2]))
        self.assertEqual(self.parser.parse_command('TRACe:FREZ:ON 3'), ('TRAC:FREZ:ON', [3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:ON')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:ON 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:ON 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:ON 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:ON ON')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:ON 1 2')

    ''' test TRAC:FREZ:OFF command '''
    def test_parse_command_TRAC_FREZ_OFF(self):
        self.assertEqual(self.parser.parse_command('TRAC:FREZ:OFF 1'), ('TRAC:FREZ:OFF', [1]))
        self.assertEqual(self.parser.parse_command('TRACe:FREeZe:OFF 2'), ('TRAC:FREZ:OFF', [2]))
        self.assertEqual(self.parser.parse_command('TRACe:FREZ:OFF 3'), ('TRAC:FREZ:OFF', [3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:OFF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:OFF 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:OFF 3.3')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:OFF all')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:FREZ:OFF 1 2')

    ''' test TRAC:VIEW:ON command '''
    def test_parse_command_TRAC_VIEW_ON(self):
        self.assertEqual(self.parser.parse_command('TRAC:VIEW:ON 1'), ('TRAC:VIEW:ON', [1]))
        self.assertEqual(self.parser.parse_command('TRACe:VIEW:ON 2'), ('TRAC:VIEW:ON', [2]))
        self.assertEqual(self.parser.parse_command('TRACe:VIEW:ON 3'), ('TRAC:VIEW:ON', [3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:ON')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:ON 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:ON 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:ON 5.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:ON all')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:ON 1 2')

    ''' test TRAC:VIEW:OFF command '''
    def test_parse_command_TRAC_VIEW_OFF(self):
        self.assertEqual(self.parser.parse_command('TRAC:VIEW:OFF 1'), ('TRAC:VIEW:OFF', [1]))
        self.assertEqual(self.parser.parse_command('TRACe:VIEW:OFF 2'), ('TRAC:VIEW:OFF', [2]))
        self.assertEqual(self.parser.parse_command('TRACe:VIEW:OFF 3'), ('TRAC:VIEW:OFF', [3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:OFF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:OFF 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:OFF 5.7')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:OFF all')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VIEW:OFF 1 3')

    ''' test TRAC:VAL command '''
    def test_parse_command_TRAC_VAL(self):
        self.assertEqual(self.parser.parse_command('TRAC:VAL  1'), ('TRAC:VAL', [1]))
        self.assertEqual(self.parser.parse_command('TRACe:VALue  2'), ('TRAC:VAL', [2]))
        self.assertEqual(self.parser.parse_command('TRAC:VALue 3'), ('TRAC:VAL', [3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VAL')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VAL 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VAL 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VAL 5.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VAL one')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:VAL 1 2')

    ''' test TRAC:COPY command '''
    def test_parse_command_TRAC_COPY(self):
        self.assertEqual(self.parser.parse_command('TRAC:COPY  1 1'), ('TRAC:COPY', [1, 1]))
        self.assertEqual(self.parser.parse_command('TRACe:COPY 1   3'), ('TRAC:COPY', [1, 3]))
        self.assertEqual(self.parser.parse_command('TRAC:COPY 3   1'), ('TRAC:COPY', [3, 1]))
        self.assertEqual(self.parser.parse_command('TRAC:COPY 3   3'), ('TRAC:COPY', [3, 3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 3.3')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRACe:COPY on')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 0 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 3 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 4 3')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 3 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 3 on')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:COPY 1 1 2')

    ''' test TRAC:SUB command '''
    def test_parse_command_TRAC_SUB(self):
        self.assertEqual(self.parser.parse_command('TRAC:SUB  1 1'), ('TRAC:SUB', [1, 1]))
        self.assertEqual(self.parser.parse_command('TRACe:SUB 1   3'), ('TRAC:SUB', [1, 3]))
        self.assertEqual(self.parser.parse_command('TRAC:SUB 3   1'), ('TRAC:SUB', [3, 1]))
        self.assertEqual(self.parser.parse_command('TRAC:SUB 3   3'), ('TRAC:SUB', [3, 3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 3.3')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRACe:SUB on')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 0 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 3 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 4 3')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 3 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 3 on')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB 1 1 2')

    ''' test TRAC:SUB:OFF command '''
    def test_parse_command_TRAC_SUB_OFF(self):
        self.assertEqual(self.parser.parse_command('TRAC:SUB:OFF 1'), ('TRAC:SUB:OFF', [1]))
        self.assertEqual(self.parser.parse_command('TRACe:SUBtract:OFF 2'), ('TRAC:SUB:OFF', [2]))
        self.assertEqual(self.parser.parse_command('TRAC:SUBtract:OFF   3'), ('TRAC:SUB:OFF', [3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB:OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB:OFF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB:OFF 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB:OFF 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB:OFF off')
        with self.assertRaises(Exception):
            self.parser.parse_command('TRAC:SUB:OFF 1 3')

    ''' test TRAC:SUB:ON command '''
    def test_parse_command_DISP_PAUSE(self):
        self.assertEqual(self.parser.parse_command('DISP:PAUSE '), ('DISP:PAUSE', []))
        self.assertEqual(self.parser.parse_command('DISPlay:PAUSE '), ('DISP:PAUSE', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:PAUSE?')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:PAUSE 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:PAUSE 0.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:PAUSE pause')

    ''' test DISP:RESUME command '''
    def test_parse_command_DISP_RESUME(self):
        self.assertEqual(self.parser.parse_command('DISP:RESUME '), ('DISP:RESUME', []))
        self.assertEqual(self.parser.parse_command('DISPlay:RESUME '), ('DISP:RESUME', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:RESUME?')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:RESUME 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:RESUME 0.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:RESUME resume')

    ''' test DISP:REFRESH command '''
    def test_parse_command_DISP_REFRESH(self):
        self.assertEqual(self.parser.parse_command('DISP:REFRESH '), ('DISP:REFRESH', []))
        self.assertEqual(self.parser.parse_command('DISPlay:REFRESH '), ('DISP:REFRESH', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:REFRESH?')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:REFRESH 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:REFRESH 3.3')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:REFRESH on')

    ''' test DISP:COLOR command '''
    def test_parse_command_DISP_COLOR(self):
        self.assertEqual(self.parser.parse_command('DISP:COLOR 0 0x000000'), ('DISP:COLOR', [0, hex(0)]))
        self.assertEqual(self.parser.parse_command('DISPlay:COLOR 30 0x000000'), ('DISP:COLOR', [30, hex(0)]))
        self.assertEqual(self.parser.parse_command('DISP:COLOR 0 0xffffff'), ('DISP:COLOR', [0, hex(0xffffff)]))

        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR blue')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR -1 0x000000')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR 31 0x000000')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR 0 0xfffffg')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR 0 0x1000000')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR 0 0x0.3')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR 0 blue')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:COLOR 0 0x000000 0')

    ''' test DISP:SWEEPTIME command '''
    def test_parse_command_DISP_SWEEPTIME(self):
        self.assertEqual(self.parser.parse_command('DISP:SWEEPTIME 0'), ('DISP:SWEEPTIME', [0]))
        self.assertEqual(self.parser.parse_command('DISPlay:SWEEPTIME 10'), ('DISP:SWEEPTIME', [10]))

        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SWEEPTIME')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SWEEPTIME -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SWEEPTIME 11')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SWEEPTIME 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SWEEPTIME default')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SWEEPTIME 1 3')

    ''' test DISP:SPUR command '''
    def test_parse_command_DISP_SPUR(self):
        self.assertEqual(self.parser.parse_command('DISP:SPUR ON'), ('DISP:SPUR', [True]))
        self.assertEqual(self.parser.parse_command('DISPlay:SPUR OFF'), ('DISP:SPUR', [False]))

        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SPUR')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SPUR 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SPUR 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SPUR on')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:SPUR ON OFF')

    ''' test DISP:CAPT command '''
    def test_parse_command_DISP_CAPT(self):
        self.assertEqual(self.parser.parse_command('DISP:CAPT'), ('DISP:CAPT', []))
        self.assertEqual(self.parser.parse_command('DISPlay:CAPTure'), ('DISP:CAPT', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:CAPT,')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:CAPT 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:CAPT 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:CAPT on')
        with self.assertRaises(Exception):
            self.parser.parse_command('DISP:CAPT ON OFF')

    ''' test OUT:LEV command '''
    def test_parse_command_OUT_LEV(self):
        self.assertEqual(self.parser.parse_command('OUT:LEV -76'), ('OUT:LEV', [-76]))
        self.assertEqual(self.parser.parse_command('OUTput:LEVel 13'), ('OUT:LEV', [13]))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEV')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEV -77')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEV 14')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEV 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEV default')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEV 1 3')

    ''' test OUT:LEVO:LOW command '''
    def test_parse_command_OUT_LEVO_LOW(self):
        self.assertEqual(self.parser.parse_command('OUT:LEVO:LOW -70'), ('OUT:LEVO:LOW', [-70]))
        self.assertEqual(self.parser.parse_command('OUTput:LEVelOffset:LOW 70'), ('OUT:LEVO:LOW', [70]))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:LOW')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:LOW -71')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:LOW 71')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:LOW 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:LOW default')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:LOW 1 3')

    ''' test OUT:LEVO:HIGH command '''
    def test_parse_command_OUT_LEVO_HIGH(self):
        self.assertEqual(self.parser.parse_command('OUT:LEVO:HIGH -70'), ('OUT:LEVO:HIGH', [-70]))
        self.assertEqual(self.parser.parse_command('OUTput:LEVelOffset:HIGH 70'), ('OUT:LEVO:HIGH', [70]))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:HIGH')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:HIGH -71')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:HIGH 71')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:HIGH 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:HIGH default')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:HIGH 1 3')

    ''' test OUT:LEVO:SWIT command '''
    def test_parse_command_OUT_LEVO_SWIT(self):
        self.assertEqual(self.parser.parse_command('OUT:LEVO:SWIT -70'), ('OUT:LEVO:SWIT', [-70]))
        self.assertEqual(self.parser.parse_command('OUTput:LEVelOffset:SWITch 70'), ('OUT:LEVO:SWIT', [70]))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:SWIT')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:SWIT -71')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:SWIT 71')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:SWIT on')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:LEVO:SWIT 1 2')

    ''' test OUT:MOD command '''
    def test_parse_command_OUT_MOD(self):
        self.assertEqual(self.parser.parse_command('OUT:MOD off'), ('OUT:MOD', ['off']))
        self.assertEqual(self.parser.parse_command('OUT:MODe am'), ('OUT:MOD', ['am']))
        self.assertEqual(self.parser.parse_command('OUTput:MOD nfm'), ('OUT:MOD', ['nfm']))
        self.assertEqual(self.parser.parse_command('OUT:MODee wfm'), ('OUT:MOD', ['wfm']))
        self.assertEqual(self.parser.parse_command('OUT:MOdD extern'), ('OUT:MOD', ['extern']))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD on')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD low')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD on')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD high')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD off am')

    ''' test OUT:MOD:FREQ command '''
    def test_parse_command_OUT_MOD_FREQ(self):
        self.assertEqual(self.parser.parse_command('OUT:MOD:FREQ 100'), ('OUT:MOD:FREQ', [100]))
        self.assertEqual(self.parser.parse_command('OUT:MODe:FREQuency 6000'), ('OUT:MOD:FREQ', [6000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD:FREQ')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD:FREQ 99')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD:FREQ 6001')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD:FREQ 3023.3')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD:FREQ default')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:MOD:FREQ 1000 3000')

    ''' test OUT:ON command '''
    def test_parse_command_OUT_ON(self):
        self.assertEqual(self.parser.parse_command('OUT:ON'), ('OUT:ON', []))
        self.assertEqual(self.parser.parse_command('OUTput:ON'), ('OUT:ON', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:ON?')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:ON 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:ON 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:ON on')

    ''' test OUT:OFF command '''
    def test_parse_command_OUT_OFF(self):
        self.assertEqual(self.parser.parse_command('OUT:OFF'), ('OUT:OFF', []))
        self.assertEqual(self.parser.parse_command('OUTput:OFF'), ('OUT:OFF', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:OFF?')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:OFF 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:OFF 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:OFF off')

    ''' test OUT:CALI:OFF command '''
    def test_parse_command_OUT_CALI_OFF(self):
        self.assertEqual(self.parser.parse_command('OUT:CALI:OFF'), ('OUT:CALI:OFF', []))
        self.assertEqual(self.parser.parse_command('OUTput:CALIbration:OFF'), ('OUT:CALI:OFF', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI:OFF?')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI:OFF 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI:OFF 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI:OFF off')

    ''' test OUT:CALI command '''
    def test_parse_command_OUT_CALI(self):
        self.assertEqual(self.parser.parse_command('OUT:CALI 30'), ('OUT:CALI', ['30']))
        self.assertEqual(self.parser.parse_command('OUT:CALIbration 15'), ('OUT:CALI', ['15']))
        self.assertEqual(self.parser.parse_command('OUT:CALI 10'), ('OUT:CALI', ['10']))
        self.assertEqual(self.parser.parse_command('OUTput:CALI 4'), ('OUT:CALI', ['4']))
        self.assertEqual(self.parser.parse_command('OUT:CALI 3'), ('OUT:CALI', ['3']))
        self.assertEqual(self.parser.parse_command('OUT:CALIb 2'), ('OUT:CALI', ['2']))
        self.assertEqual(self.parser.parse_command('OUT:CALI 1'), ('OUT:CALI', ['1']))

        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI 20')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI 31')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI 1.2')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI on')
        with self.assertRaises(Exception):
            self.parser.parse_command('OUT:CALI 1 2')

    ''' test MARK:FREQ command '''
    def test_parse_command_MARK_FREQ(self):
        self.assertEqual(self.parser.parse_command('MARK:FREQ 1   0'), ('MARK:FREQ', [1, 0]))
        self.assertEqual(self.parser.parse_command('MARKer:FREQuency 4 0'), ('MARK:FREQ', [4, 0]))
        self.assertEqual(self.parser.parse_command('MARK:FREQ 1      959000000'), ('MARK:FREQ', [1, 959000000]))
        self.assertEqual(self.parser.parse_command('MARK:FREQ 4      959000000'), ('MARK:FREQ', [4, 959000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ   1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ   1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  default')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  0  0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  5 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  1  -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  1  959000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  1  1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  1  on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  1  1  1')

    ''' test MARK:DELT command '''
    def test_parse_command_MARK_DELT(self):
        self.assertEqual(self.parser.parse_command('MARK:DELT 1   1'), ('MARK:DELT', [1, 1]))
        self.assertEqual(self.parser.parse_command('     MARKer:DELTa 4 1'), ('MARK:DELT', [4, 1]))
        self.assertEqual(self.parser.parse_command('MARK:DELT 1      4'), ('MARK:DELT', [1, 4]))
        self.assertEqual(self.parser.parse_command('MARK:DELTa 4   4'), ('MARK:DELT', [4, 4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT   1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT   1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT  default')

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT  0  1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT  5 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT  1  0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT  1  5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT  1  1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT  1  on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT  1  1  1')

    ''' test MARK:DELT:OFF command '''
    def test_parse_command_MARK_DELT_OFF(self):
        self.assertEqual(self.parser.parse_command('MARK:DELT:OFF 1'), ('MARK:DELT:OFF', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:DELTa:OFF 4'), ('MARK:DELT:OFF', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT:OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT:OFF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT:OFF 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT:OFF 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT:OFF on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DELT:OFF 1 3')

    ''' test MARK:NOIS:SET command '''
    def test_parse_command_MARK_NOIS_SET(self):
        self.assertEqual(self.parser.parse_command('MARK:NOIS:SET 1'), ('MARK:NOIS:SET', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:NOISe:SET 4'), ('MARK:NOIS:SET', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:SET')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:SET 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:SET 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:SET 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:SET off')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:SET 1 3')

    ''' test MARK:NOIS:OFF command '''
    def test_parse_command_MARK_NOIS_OFF(self):
        self.assertEqual(self.parser.parse_command('MARK:NOIS:OFF 1'), ('MARK:NOIS:OFF', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:NOISe:OFF 4'), ('MARK:NOIS:OFF', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:OFF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:OFF 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:OFF 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:OFF on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:NOIS:OFF 1 3')

    ''' test MARK:TRAK:SET command '''
    def test_parse_command_MARK_TRAK_SET(self):
        self.assertEqual(self.parser.parse_command('MARK:TRAK:SET       1'), ('MARK:TRAK:SET', [1]))
        self.assertEqual(self.parser.parse_command('         MARKer:TRAcKing:SET 4'), ('MARK:TRAK:SET', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:SET')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:SET 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:SET 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:SET 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:SET off')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:SET 1 3')

    ''' test MARK:TRAK:OFF command '''
    def test_parse_command_MARK_TRAK_OFF(self):
        self.assertEqual(self.parser.parse_command('MARK:TRAK:OFF 1'), ('MARK:TRAK:OFF', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:TRAcKing:OFF 4'), ('MARK:TRAK:OFF', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:OFF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:OFF 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:OFF 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:OFF on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAK:OFF 1 3')

    ''' test MARK:TRAC command '''
    def test_parse_command_MARK_TRAC(self):
        self.assertEqual(self.parser.parse_command('MARK:TRAC 1 1'), ('MARK:TRAC', [1, 1]))
        self.assertEqual(self.parser.parse_command('MARKer:TRACe 1 3'), ('MARK:TRAC', [1, 3]))
        self.assertEqual(self.parser.parse_command('MARK:TRACe 4 1'), ('MARK:TRAC', [4, 1]))
        self.assertEqual(self.parser.parse_command('MARKer:TRAC 4  3'), ('MARK:TRAC', [4, 3]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC t')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 0 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 5 3')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 4 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 4 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 4 on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:TRAC 1 1 2')

    ''' test MARK:AVER:SET command '''
    def test_parse_command_MARK_AVER_SET(self):
        self.assertEqual(self.parser.parse_command('MARK:AVER:SET 1'), ('MARK:AVER:SET', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:AVERage:SET 4'), ('MARK:AVER:SET', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:SET')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:SET 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:SET 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:SET 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:SET on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:SET 1 3')

    ''' test MARK:AVER:OFF command '''
    def test_parse_command_MARK_AVER_OFF(self):
        self.assertEqual(self.parser.parse_command('MARK:AVER:OFF 1'), ('MARK:AVER:OFF', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:AVERage:OFF 4'), ('MARK:AVER:OFF', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:OFF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:OFF 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:OFF 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:OFF on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:AVER:OFF 1 3')

    ''' test MARK:MODE command '''
    def test_parse_command_MARK_SRCH_PEAK(self):
        self.assertEqual(self.parser.parse_command('MARK:SRCH:PEAK 1'), ('MARK:SRCH:PEAK', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:PEAK 4'), ('MARK:SRCH:PEAK', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:PEAK')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:PEAK 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:PEAK 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:PEAK 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:PEAK on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:PEAK 1 3')

    ''' test MARK:SRCH:MINR command '''
    def test_parse_command_MARK_SRCH_MINR(self):
        self.assertEqual(self.parser.parse_command('MARK:SRCH:MINR 1'), ('MARK:SRCH:MINR', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:MINRight 4'), ('MARK:SRCH:MINR', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINR')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINR 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINR 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINR 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINR on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINR 1 3')

    ''' test MARK:SRCH:MINL command '''
    def test_parse_command_MARK_SRCH_MINL(self):
        self.assertEqual(self.parser.parse_command('MARK:SRCH:MINL 1'), ('MARK:SRCH:MINL', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:MINLeft 4'), ('MARK:SRCH:MINL', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINL')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINL 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINL 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINL 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINL on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MINL 1 3')

    ''' test MARK:SRCH:MAXR command'''
    def test_parse_command_MARK_SRCH_MAXR(self):
        self.assertEqual(self.parser.parse_command('MARK:SRCH:MAXR 1'), ('MARK:SRCH:MAXR', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:MAXRight 4'), ('MARK:SRCH:MAXR', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXR')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXR 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXR 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXR 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXR on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXR 1 3')

    ''' test MARK:SRCH:MAXL command '''
    def test_parse_command_MARK_SRCH_MAXL(self):
        self.assertEqual(self.parser.parse_command('MARK:SRCH:MAXL 1'), ('MARK:SRCH:MAXL', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:MAXLeft 4'), ('MARK:SRCH:MAXL', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXL')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXL 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXL 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXL 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXL on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:MAXL 1 3')

    ''' test MARK:SRCH:FREQ command '''
    def test_parse_command_MARK_SRCH_FREQ(self):
        self.assertEqual(self.parser.parse_command('MARK:SRCH:FREQ 1 0'), ('MARK:SRCH:FREQ', [1, 0]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:FREQuency 1 959000000'), ('MARK:SRCH:FREQ', [1, 959000000]))
        self.assertEqual(self.parser.parse_command('MARK:SRCH:FREQ 4 0'), ('MARK:SRCH:FREQ', [4, 0]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:FREQuency 4 959000000'), ('MARK:SRCH:FREQ', [4, 959000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ all')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ -1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 959000001 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 959000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 max')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 1 2')

    ''' test MARK:DEL command '''
    def test_parse_command_MARK_DEL(self):
        self.assertEqual(self.parser.parse_command('MARK:DEL 1'), ('MARK:DEL', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:DELete 4'), ('MARK:DEL', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DEL')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DEL 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DEL 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DEL 2.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DEL on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DEL 1 3')

    ''' test MARK:RST command '''
    def test_parse_command_MARK_RST(self):
        self.assertEqual(self.parser.parse_command('MARK:RST'), ('MARK:RST', []))
        self.assertEqual(self.parser.parse_command('MARKer:ReSeT'), ('MARK:RST', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:RST?')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:RST 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:RST 3.3')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:RST all')

    ''' test MARK:DIFF command '''
    def test_parse_command_MARK_DIFF(self):
        self.assertEqual(self.parser.parse_command('MARK:DIFF 1 1'), ('MARK:DIFF', [1, 1]))
        self.assertEqual(self.parser.parse_command('MARKer:DIFFerence 1 4'), ('MARK:DIFF', [1, 4]))
        self.assertEqual(self.parser.parse_command('MARK:DIFFer 4 1'), ('MARK:DIFF', [4, 1]))
        self.assertEqual(self.parser.parse_command('MARKer:DIFF 4  4'), ('MARK:DIFF', [4, 4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF none')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 0 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 5 4')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 4 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 4 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 4 None')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF 1 1 2')

    ''' test MARK:DIFF:OFF command '''
    def test_parse_command_MARK_DIFF_OFF(self):
        self.assertEqual(self.parser.parse_command('MARK:DIFF:OFF 1'), ('MARK:DIFF:OFF', [1]))
        self.assertEqual(self.parser.parse_command('MARKer:DIFFerence:OFF 4'), ('MARK:DIFF:OFF', [4]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF:OFF')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF:OFF 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF:OFF 5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF:OFF 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF:OFF off')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:DIFF:OFF 1 3')

    ''' test MEAS:DUMP command '''
    def test_parse_command_MEAS_DUMP(self):
        self.assertEqual(self.parser.parse_command('MEAS:DUMP 0'), ('MEAS:DUMP', [0]))
        self.assertEqual(self.parser.parse_command('MEASure:DUMP 2'), ('MEAS:DUMP', [2]))

        with self.assertRaises(Exception):
            self.parser.parse_command('MEAS:DUMP')
        with self.assertRaises(Exception):
            self.parser.parse_command('MEAS:DUMP -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MEAS:DUMP 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MEAS:DUMP all')
        with self.assertRaises(Exception):
            self.parser.parse_command('MEAS:DUMP 1 2')

    ''' test CONF:CAPT command '''
    def test_parse_command_CONF_CAPT(self):
        self.assertEqual(self.parser.parse_command('CONF:CAPT'), ('CONF:CAPT', []))
        self.assertEqual(self.parser.parse_command('CONFigure:CAPTure'), ('CONF:CAPT', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CAPT?')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CAPT 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CAPT 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CAPT on')

    ''' test CONF:CALC command '''
    def test_parse_command_CONF_CALC(self):
        self.assertEqual(self.parser.parse_command('CONF:CALC off'), ('CONF:CALC', ['off']))
        self.assertEqual(self.parser.parse_command('CONFigure:CALCulation minh'), ('CONF:CALC', ['minh']))
        self.assertEqual(self.parser.parse_command('CONFigure:CALCulation maxh'), ('CONF:CALC', ['maxh']))
        self.assertEqual(self.parser.parse_command('CONFigure:CALCulation maxd'), ('CONF:CALC', ['maxd']))
        self.assertEqual(self.parser.parse_command('CONFigure:CALCulation aver4'), ('CONF:CALC', ['aver4']))
        self.assertEqual(self.parser.parse_command('CONFigure:CALCulation aver16'), ('CONF:CALC', ['aver16']))
        self.assertEqual(self.parser.parse_command('CONFigure:CALCulation quasip'), ('CONF:CALC', ['quasip']))

    ''' test CONF:CORR:LOW command '''
    def test_parse_command_CONF_CORR_LOW(self):
        self.assertEqual(self.parser.parse_command('CONF:CORR:LOW 0 0 -200', ), ('CONF:CORR:LOW', [0, 0, -200]))
        self.assertEqual(self.parser.parse_command('CONFigure:CORRection:LOW 19 0 0', ), ('CONF:CORR:LOW', [19, 0, 0]))
        self.assertEqual(self.parser.parse_command('CONFigure:CORRection:LOW 0 959000000 0', ), ('CONF:CORR:LOW', [0, 959000000, 0]))
        self.assertEqual(self.parser.parse_command('CONFigure:CORRection:LOW 0 0 13.0', ), ('CONF:CORR:LOW', [0, 0, 13.0]))

        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 0 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW -1 0 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 20 0 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 0 -1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 0 959000001 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 0 0 -201.0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 0 0 13.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 1.5 0 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 0 1.5 0')

        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:LOW 0 0 0 0')

    ''' test CONF:CORR:HIGH command '''
    def test_parse_command_CONF_CORR_HIGH(self):
        self.assertEqual(self.parser.parse_command('CONF:CORR:HIGH 0 0 -200.0', ), ('CONF:CORR:HIGH', [0, 0, -200.0]))
        self.assertEqual(self.parser.parse_command('CONFigure:CORRection:HIGH 19 0 0', ), ('CONF:CORR:HIGH', [19, 0, 0]))
        self.assertEqual(self.parser.parse_command('CONFigure:CORRection:HIGH 0 959000000 0', ), ('CONF:CORR:HIGH', [0, 959000000, 0]))
        self.assertEqual(self.parser.parse_command('CONFigure:CORRection:HIGH 0 0 13.0', ), ('CONF:CORR:HIGH', [0, 0, 13.0]))

        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 0 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH -1 0 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 20 0 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 0 -1 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 0 959000001 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 0 0 -200.00000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 0 0 13.0000000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 1.5 0 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 0 1.5 0')

        with self.assertRaises(Exception):
            self.parser.parse_command('CONF:CORR:HIGH 0 0 0 0')


if __name__ == '__main__':
    unittest.main()
