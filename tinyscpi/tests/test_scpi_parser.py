from tinyscpi import scpi_parser
import unittest


class ParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = scpi_parser.SCPI_Parser()

    def testBasics(self) -> None:
        with self.assertRaises(Exception):
            self.parser.parse_command('')

    def testParseCommand_IDN(self) -> None:
        self.assertEqual(self.parser.parse_command('*IDN?'), ('*IDN?', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*IDN')
        with self.assertRaises(Exception):
            self.parser.parse_command('*IDN? on')
        with self.assertRaises(Exception):
            self.parser.parse_command('*IDN? 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('*IDN? 1.1')

    def testParseCommand_RST(self) -> None:
        self.assertEqual(self.parser.parse_command('*RST'), ('*RST', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*RST?')
        with self.assertRaises(Exception):
            self.parser.parse_command('*RST factory')
        with self.assertRaises(Exception):
            self.parser.parse_command('*RST 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('*RST 3.1')

    def testParseCommand_CLR(self) -> None:
        self.assertEqual(self.parser.parse_command('*CLR'), ('*CLR', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*CLR?')
        with self.assertRaises(Exception):
            self.parser.parse_command('*CLR clear')
        with self.assertRaises(Exception):
            self.parser.parse_command('*CLR 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('*CLR 3.5')

    def testParseCommand_TST(self) -> None:
        self.assertEqual(self.parser.parse_command('*TST?'), ('*TST?', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*TST')
        with self.assertRaises(Exception):
            self.parser.parse_command('*TST? all')
        with self.assertRaises(Exception):
            self.parser.parse_command('*TST? 1')
        with self.assertRaises(Exception):
            self.parser.parse_command('*TST? 3.3')

    def testParseCommand_HLP(self) -> None:
        self.assertEqual(self.parser.parse_command('*HLP'), ('*HLP', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('*HLP?')
        with self.assertRaises(Exception):
            self.parser.parse_command('*HLP show')
        with self.assertRaises(Exception):
            self.parser.parse_command('*HLP 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('*HLP 2.2')

    def testParseCommand_FREQ_START(self):
        self.assertEqual(self.parser.parse_command('FREQ:START 0'), ('FREQ:START', [0]))
        self.assertEqual(self.parser.parse_command('FREQuency:START 350000000'), ('FREQ:START', [350000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START 350000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START start')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START 5.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:START 1 1')

    def testParseCommand_FREQ_STOP(self):
        self.assertEqual(self.parser.parse_command('FREQ:STOP 0'), ('FREQ:STOP', [0]))
        self.assertEqual(self.parser.parse_command('FREQuency:STOP 350000000'), ('FREQ:STOP', [350000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP 350000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP default')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP 350000.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:STOP 340000000 350000000')

    def testParseCommand_FREQ_CENT(self):
        self.assertEqual(self.parser.parse_command('FREQ:CENT 0'), ('FREQ:CENT', [0]))
        self.assertEqual(self.parser.parse_command('FREQuency:CENTer 350000000'), ('FREQ:CENT', [350000000]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT 350000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT peak')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT 100000.02')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:CENT 0 0')

    def testParseCommand_FREQ_SPAN(self):
        self.assertEqual(self.parser.parse_command('FREQ:SPAN 0'), ('FREQ:SPAN', [0]))
        self.assertEqual(self.parser.parse_command('FREQuency:SPAN 290'),
                         ('FREQ:SPAN', [290]))

        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN 350000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN span')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN 5.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('FREQ:SPAN 1 1')

    def testParseCommand_FREQ_SPAN_ZERO(self):
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

    def testParseCommand_FREQ_RBW(self):
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
        
    def testParseCommand_FREQ_RBW_AUTO(self):
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

    def testParseCommand_FREQ_DUMP(self):
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

    def testParseCommand_LVL_ATT(self):
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

    def testParseCommand_LVL_ATT_AUTO(self):
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

    def testParseCommand_LVL_ATT_QUERY(self):
        self.assertEqual(self.parser.parse_command('LVL:ATT?'), ('LVL:ATT?', []))
        self.assertEqual(self.parser.parse_command('LeVeL:ATTenuation?'), ('LVL:ATT?', []))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT? 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT? 1.1')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT? one')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:ATT? 0 1')

    def testParseCommand_LVL_REF(self):
        self.assertEqual(self.parser.parse_command('LVL:REF -100'), ('LVL:REF', [-100]))
        self.assertEqual(self.parser.parse_command('LeVeL:REFerence 100.33'), ('LVL:REF', [100.33]))

        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF default')
        with self.assertRaises(Exception):
            self.parser.parse_command('LVL:REF 1.1 20.1')

    def testParseCommand_LVL_REF_AUTO(self):
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

    def testParseCommand_LVL_SCAL(self):
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

    def testParseCommand_LVL_SCAL_AUTO(self):
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

    def testParseCommand_LVL_UNIT(self):
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

    def testParseCommand_LVL_XGAIN(self):
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

    def testParseCommand_TRAC_FREZ_ON(self):
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

    def testParseCommand_TRAC_FREZ_OFF(self):
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

    def testParseCommand_TRAC_VIEW_ON(self):
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

    def testParseCommand_TRAC_VIEW_OFF(self):
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

    def testParseCommand_TRAC_VAL(self):
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

    def testParseCommand_TRAC_COPY(self):
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

    def testParseCommand_TRAC_SUB(self):
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

    def testParseCommand_TRAC_SUB_OFF(self):
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

    def testParseCommand_DISP_PAUSE(self):
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

    def testParseCommand_DISP_RESUME(self):
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

    def testParseCommand_DISP_REFRESH(self):
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

    def testParseCommand_DISP_COLOR(self):
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

    def testParseCommand_DISP_SWEEPTIME(self):
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

    def testParseCommand_DISP_SPUR(self):
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

    def testParseCommand_MARK_FREQ(self):
        self.assertEqual(self.parser.parse_command('MARK:FREQ 1   0'), ('MARK:FREQ', [1, 0]))
        self.assertEqual(self.parser.parse_command('MARKer:FREQuency 4 0'), ('MARK:FREQ', [4, 0]))
        self.assertEqual(self.parser.parse_command('MARK:FREQ 1      350000000'), ('MARK:FREQ', [1, 350000000]))
        self.assertEqual(self.parser.parse_command('MARK:FREQ 4      350000000'), ('MARK:FREQ', [4, 350000000]))

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
            self.parser.parse_command('MARK:FREQ  1  350000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  1  1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  1  on')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:FREQ  1  1  1')


    def testParseCommand_MARK_DELT(self):
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

    def testParseCommand_MARK_DELT_OFF(self):
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

    def testParseCommand_MARK_NOIS_SET(self):
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

    def testParseCommand_MARK_NOIS_OFF(self):
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

    def testParseCommand_MARK_TRAK_SET(self):
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

    def testParseCommand_MARK_TRAK_OFF(self):
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


    def testParseCommand_MARK_TRAC(self):
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

    def testParseCommand_MARK_AVER_SET(self):
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

    def testParseCommand_MARK_AVER_OFF(self):
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



    def testParseCommand_MARK_SRCH_PEAK(self):
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

    def testParseCommand_MARK_SRCH_MINR(self):
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

    def testParseCommand_MARK_SRCH_MINL(self):
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

    def testParseCommand_MARK_SRCH_MAXR(self):
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

    def testParseCommand_MARK_SRCH_MAXL(self):
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

    def testParseCommand_MARK_SRCH_FREQ(self):
        self.assertEqual(self.parser.parse_command('MARK:SRCH:FREQ 0 0'), ('MARK:SRCH:FREQ', [0, 0]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:FREQuency 0 350000000'), ('MARK:SRCH:FREQ', [0, 350000000]))
        self.assertEqual(self.parser.parse_command('MARK:SRCH:FREQ 350000000 0'), ('MARK:SRCH:FREQ', [350000000, 0]))
        self.assertEqual(self.parser.parse_command('MARKer:SeaRCH:FREQuency 350000000 350000000'), ('MARK:SRCH:FREQ', [350000000, 350000000]))

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
            self.parser.parse_command('MARK:SRCH:FREQ 350000001 0')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 -1')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 350000001')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 1.5')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 max')
        with self.assertRaises(Exception):
            self.parser.parse_command('MARK:SRCH:FREQ 0 1 2')

    def testParseCommand_MARK_DEL(self):
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

    def testParseCommand_MARK_RST(self):
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

    def testParseCommand_MARK_DIFF(self):
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

    def testParseCommand_MARK_DIFF_OFF(self):
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



    def testParseCommand_CONF_CAPT(self):
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


if __name__ == '__main__':
    unittest.main()
