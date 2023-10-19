import unittest
from tinyscpi.scpi_functional import SCPI_functional
from tinyscpi.scpi_parser import SCPI_Parser
class FunctionalTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.functional = SCPI_functional()
        self.parser = SCPI_Parser()

    def testBasics(self):
        self.assertEqual(self.functional.VID, 0x0483)
        self.assertEqual(self.functional.PID, 0x5740)
        self.assertEqual(self.functional.cr, b'\r')
        self.assertEqual(self.functional.lf, b'\n')
        self.assertEqual(self.functional.crlf, b'\r\n')
        self.assertEqual(self.functional.prompt, b'ch> ')
        self.assertEqual(self.functional.screen_width, 320)
        self.assertEqual(self.functional.screen_height, 240)
        self.assertEqual(self.functional.device_name, "TinySA")

    #TODO: This test will pass if and only if tinySA and some other USB device is connected
    def testGetDevice(self):
        self.assertEqual(1, 1)
        #TODO: implement this test

    def testConvertSCPItoUSB_BASIC(self):
        # '*IDN?'
        result = self.functional.convert_scpi_to_usb('*IDN?', [])
        self.assertEqual(result, 'info')
        # '*RST'
        result = self.functional.convert_scpi_to_usb('*RST', [])
        self.assertEqual(result, 'reset')

        # '*CLR'
        result = self.functional.convert_scpi_to_usb('*CLR', [])
        self.assertEqual(result, 'clearconfig')
        # '*TST'
        result = self.functional.convert_scpi_to_usb('*TST?', [])
        self.assertEqual(result, 'selftest')
        # '*HLP'
        result = self.functional.convert_scpi_to_usb('*HLP', [])
        self.assertEqual(result, 'help')


    def testConvertSCPItoUSB_FREQ(self):
        # 'FREQ:START 0'
        result = self.functional.convert_scpi_to_usb('FREQ:START', [0])
        self.assertEqual(result, 'sweep start 0')
        # 'FREQuency:START 350000000'
        result = self.functional.convert_scpi_to_usb('FREQ:START', [350000000])
        self.assertEqual(result, 'sweep start 350000000')
        # 'FREQ:STOP 0'
        result = self.functional.convert_scpi_to_usb('FREQ:STOP', [0])
        self.assertEqual(result, 'sweep stop 0')
        # 'FREQuency:STOP 350000000'
        result = self.functional.convert_scpi_to_usb('FREQ:STOP', [350000000])
        self.assertEqual(result, 'sweep stop 350000000')
        # 'FREQ:CENT 0'
        result = self.functional.convert_scpi_to_usb('FREQ:CENT', [0])
        self.assertEqual(result, 'sweep center 0')
        # 'FREQuency:CENTer 350000000'
        result = self.functional.convert_scpi_to_usb('FREQ:CENT', [350000000])
        self.assertEqual(result, 'sweep center 350000000')
        # 'FREQ:SPAN 0'
        result = self.functional.convert_scpi_to_usb('FREQ:SPAN', [0])
        self.assertEqual(result, 'sweep span 0')
        # 'FREQuency:SPAN 290'
        result = self.functional.convert_scpi_to_usb('FREQ:SPAN', [290])
        self.assertEqual(result, 'sweep span 290')
        # 'FREQ:SPAN:ZERO'
        result = self.functional.convert_scpi_to_usb('FREQ:SPAN:ZERO', [])
        self.assertEqual(result, 'sweep span 0')
        # 'FREQ:RBW 3'
        result = self.functional.convert_scpi_to_usb('FREQ:RBW', [3])
        self.assertEqual(result, 'rbw 3')
        # 'FREQuency:RBW 10'
        result = self.functional.convert_scpi_to_usb('FREQ:RBW', [10])
        self.assertEqual(result, 'rbw 10')
        # 'FREQ:RBW 30'
        result = self.functional.convert_scpi_to_usb('FREQ:RBW', [30])
        self.assertEqual(result, 'rbw 30')
        # 'FREQuency:RBW 100'
        result = self.functional.convert_scpi_to_usb('FREQ:RBW', [100])
        self.assertEqual(result, 'rbw 100')
        # 'FREQ:RBW 300'
        result = self.functional.convert_scpi_to_usb('FREQ:RBW', [300])
        self.assertEqual(result, 'rbw 300')
        # 'FREQuency:RBW 600'
        result = self.functional.convert_scpi_to_usb('FREQ:RBW', [600])
        self.assertEqual(result, 'rbw 600')
        # 'FREQ:RBW:AUTO'
        result = self.functional.convert_scpi_to_usb('FREQ:RBW:AUTO', [])
        self.assertEqual(result, 'rbw auto')
        # 'FREQuency:RBandWidth:AUTO'
        result = self.functional.convert_scpi_to_usb('FREQ:RBW:AUTO', [])
        self.assertEqual(result, 'rbw auto')
        # 'FREQ:DUMP'
        result = self.functional.convert_scpi_to_usb('FREQ:DUMP', [])
        self.assertEqual(result, 'frequencies')
        # 'FREQuency:DUMP'
        result = self.functional.convert_scpi_to_usb('FREQ:DUMP', [])
        self.assertEqual(result, 'frequencies')

    def testConvertSCPItoUSB_LVL(self):
        # 'LVL:ATT 0'
        result = self.functional.convert_scpi_to_usb('LVL:ATT', [0])
        self.assertEqual(result, 'attenuate 0')
        # 'LeVeL:ATTenuation 30'
        result = self.functional.convert_scpi_to_usb('LVL:ATT', [30])
        self.assertEqual(result, 'attenuate 30')
        # 'LVL:ATT:AUTO'
        result = self.functional.convert_scpi_to_usb('LVL:ATT:AUTO', [])
        self.assertEqual(result, 'attenuate auto')
        # 'LeVeL:ATTeunuation:AUTO'
        result = self.functional.convert_scpi_to_usb('LVL:ATT:AUTO', [])
        self.assertEqual(result, 'attenuate auto')
        # 'LVL:REF -100'
        result = self.functional.convert_scpi_to_usb('LVL:REF', [-100])
        self.assertEqual(result, 'trace reflevel -100')
        # 'LeVeL:REFerence 100.33'
        result = self.functional.convert_scpi_to_usb('LVL:REF', [100.33])
        self.assertEqual(result, 'trace reflevel 100.33')
        # 'LVL:REF:AUTO'
        result = self.functional.convert_scpi_to_usb('LVL:REF:AUTO', [])
        self.assertEqual(result, 'trace reflevel auto')
        # 'LeVeL:REFerence:AUTO'
        result = self.functional.convert_scpi_to_usb('LVL:REF:AUTO', [])
        self.assertEqual(result, 'trace reflevel auto')
        # 'LVL:SCAL 1'
        result = self.functional.convert_scpi_to_usb('LVL:SCAL', ['1'])
        self.assertEqual(result, 'trace scale 1')
        # 'LeVeL:SCALe 2'
        result = self.functional.convert_scpi_to_usb('LVL:SCAL', ['2'])
        self.assertEqual(result, 'trace scale 2')
        # 'LVL:SCAL 5'
        result = self.functional.convert_scpi_to_usb('LVL:SCAL', ['5'])
        self.assertEqual(result, 'trace scale 5')
        # 'LeVeL:SCALe 10'
        result = self.functional.convert_scpi_to_usb('LVL:SCAL', ['10'])
        self.assertEqual(result, 'trace scale 10')
        # 'LVL:SCAL 20'
        result = self.functional.convert_scpi_to_usb('LVL:SCAL', ['20'])
        self.assertEqual(result, 'trace scale 20')
        # 'LVL:SCAL:AUTO'
        result = self.functional.convert_scpi_to_usb('LVL:SCAL:AUTO', [])
        self.assertEqual(result, 'trace scale auto')
        # 'LeVeL:SCALe:AUTO'
        result = self.functional.convert_scpi_to_usb('LVL:SCAL:AUTO', [])
        self.assertEqual(result, 'trace scale auto')
        # 'LVL:UNIT dBm'
        result = self.functional.convert_scpi_to_usb('LVL:UNIT', ['dBm'])
        self.assertEqual(result, 'trace dBm')
        # 'LeVeL:UNIT dBmV'
        result = self.functional.convert_scpi_to_usb('LVL:UNIT', ['dBmV'])
        self.assertEqual(result, 'trace dBmV')
        # 'LVL:UNIT dBuV'
        result = self.functional.convert_scpi_to_usb('LVL:UNIT', ['dBuV'])
        self.assertEqual(result, 'trace dBuV')
        # 'LeVeL:UNIT V'
        result = self.functional.convert_scpi_to_usb('LVL:UNIT', ['V'])
        self.assertEqual(result, 'trace V')
        # 'LVL:UNIT W'
        result = self.functional.convert_scpi_to_usb('LVL:UNIT', ['W'])
        self.assertEqual(result, 'trace W')
        # 'LVL:XGAIN 0'
        result = self.functional.convert_scpi_to_usb('LVL:XGAIN', [0])
        self.assertEqual(result, 'ext_gain 0')
        # 'LeVeL:eXtraGAIN 100'
        result = self.functional.convert_scpi_to_usb('LVL:XGAIN', [100])
        self.assertEqual(result, 'ext_gain 100')
        # 'LVL:XGAIN -100'
        result = self.functional.convert_scpi_to_usb('LVL:XGAIN', [-100])
        self.assertEqual(result, 'ext_gain -100')

    def testConvertSCPItoUSB_TRAC(self):
        # 'TRAC:FREZ:ON 1'
        result = self.functional.convert_scpi_to_usb('TRAC:FREZ:ON', [1])
        self.assertEqual(result, 'trace 1 freeze on')
        # 'TRACe:FREeZe:ON 2'
        result = self.functional.convert_scpi_to_usb('TRAC:FREZ:ON', [2])
        self.assertEqual(result, 'trace 2 freeze on')
        # 'TRACe:FREZ:ON 3'
        result = self.functional.convert_scpi_to_usb('TRAC:FREZ:ON', [3])
        self.assertEqual(result, 'trace 3 freeze on')
        # 'TRAC:FREZ:OFF 1'
        result = self.functional.convert_scpi_to_usb('TRAC:FREZ:OFF', [1])
        self.assertEqual(result, 'trace 1 freeze off')
        # 'TRACe:FREeZe:OFF 2'
        result = self.functional.convert_scpi_to_usb('TRAC:FREZ:OFF', [2])
        self.assertEqual(result, 'trace 2 freeze off')
        # 'TRACe:FREZ:OFF 3'
        result = self.functional.convert_scpi_to_usb('TRAC:FREZ:OFF', [3])
        self.assertEqual(result, 'trace 3 freeze off')
        # 'TRAC:VIEW:ON 1'
        result = self.functional.convert_scpi_to_usb('TRAC:VIEW:ON', [1])
        self.assertEqual(result, 'trace 1 view on')
        # 'TRACe:VIEW:ON 2'
        result = self.functional.convert_scpi_to_usb('TRAC:VIEW:ON', [2])
        self.assertEqual(result, 'trace 2 view on')
        # 'TRACe:VIEW:ON 3'
        result = self.functional.convert_scpi_to_usb('TRAC:VIEW:ON', [3])
        self.assertEqual(result, 'trace 3 view on')
        # 'TRAC:VIEW:OFF 1'
        result = self.functional.convert_scpi_to_usb('TRAC:VIEW:OFF', [1])
        self.assertEqual(result, 'trace 1 view off')
        # 'TRACe:VIEW:OFF 2'
        result = self.functional.convert_scpi_to_usb('TRAC:VIEW:OFF', [2])
        self.assertEqual(result, 'trace 2 view off')
        # 'TRACe:VIEW:OFF 3'
        result = self.functional.convert_scpi_to_usb('TRAC:VIEW:OFF', [3])
        self.assertEqual(result, 'trace 3 view off')
        # 'TRAC:VAL  1'
        result = self.functional.convert_scpi_to_usb('TRAC:VAL', [1])
        self.assertEqual(result, 'trace 1 value')
        # 'TRACe:VALue  2'
        result = self.functional.convert_scpi_to_usb('TRAC:VAL', [2])
        self.assertEqual(result, 'trace 2 value')
        # 'TRAC:VALue 3'
        result = self.functional.convert_scpi_to_usb('TRAC:VAL', [3])
        self.assertEqual(result, 'trace 3 value')
        # 'TRAC:COPY  1 1'
        result = self.functional.convert_scpi_to_usb('TRAC:COPY', [1, 1])
        self.assertEqual(result, 'trace 1 copy 1')
        # 'TRACe:COPY 1   3'
        result = self.functional.convert_scpi_to_usb('TRAC:COPY', [1, 3])
        self.assertEqual(result, 'trace 1 copy 3')
        # 'TRAC:COPY 3   1'
        result = self.functional.convert_scpi_to_usb('TRAC:COPY', [3, 1])
        self.assertEqual(result, 'trace 3 copy 1')
        # 'TRAC:COPY 3   3'
        result = self.functional.convert_scpi_to_usb('TRAC:COPY', [3, 3])
        self.assertEqual(result, 'trace 3 copy 3')
        # 'TRAC:SUB  1 1'
        result = self.functional.convert_scpi_to_usb('TRAC:SUB', [1, 1])
        self.assertEqual(result, 'trace 1 subtract 1')
        # 'TRACe:SUB 1   3'
        result = self.functional.convert_scpi_to_usb('TRAC:SUB', [1, 3])
        self.assertEqual(result, 'trace 1 subtract 3')
        # 'TRAC:SUB 3   1'
        result = self.functional.convert_scpi_to_usb('TRAC:SUB', [3, 1])
        self.assertEqual(result, 'trace 3 subtract 1')
        # 'TRAC:SUB 3   3'
        result = self.functional.convert_scpi_to_usb('TRAC:SUB', [3, 3])
        self.assertEqual(result, 'trace 3 subtract 3')
        # 'TRAC:SUB:OFF 1'
        result = self.functional.convert_scpi_to_usb('TRAC:SUB:OFF', [1])
        self.assertEqual(result, 'trace 1 subtract off')
        # 'TRACe:SUBtract:OFF 2'
        result = self.functional.convert_scpi_to_usb('TRAC:SUB:OFF', [2])
        self.assertEqual(result, 'trace 2 subtract off')
        # 'TRAC:SUBtract:OFF   3'
        result = self.functional.convert_scpi_to_usb('TRAC:SUB:OFF', [3])
        self.assertEqual(result, 'trace 3 subtract off')

    def testConvertSCPItoUSB_DISP(self):
        # 'DISP:PAUSE '
        result = self.functional.convert_scpi_to_usb('DISP:PAUSE', [])
        self.assertEqual(result, 'pause')
        # 'DISPlay:PAUSE '
        result = self.functional.convert_scpi_to_usb('DISP:PAUSE', [])
        self.assertEqual(result, 'pause')
        # 'DISP:RESUME '
        result = self.functional.convert_scpi_to_usb('DISP:RESUME', [])
        self.assertEqual(result, 'resume')
        # 'DISPlay:RESUME '
        result = self.functional.convert_scpi_to_usb('DISP:RESUME', [])
        self.assertEqual(result, 'resume')
        # 'DISP:REFRESH '
        result = self.functional.convert_scpi_to_usb('DISP:REFRESH', [])
        self.assertEqual(result, 'resume')
        # 'DISPlay:REFRESH '
        result = self.functional.convert_scpi_to_usb('DISP:REFRESH', [])
        self.assertEqual(result, 'resume')
        # 'DISP:COLOR 0 0x000000'
        result = self.functional.convert_scpi_to_usb('DISP:COLOR', [0, 0x000000])
        self.assertEqual(result, 'color 0 0')
        # 'DISPlay:COLOR 30 0x000000'
        result = self.functional.convert_scpi_to_usb('DISP:COLOR', [30, 0x000000])
        self.assertEqual(result, 'color 30 0')
        # 'DISP:COLOR 0 0xffffff'
        result = self.functional.convert_scpi_to_usb('DISP:COLOR', [0, 0xffffff])
        self.assertEqual(result, 'color 0 16777215')
        # 'DISP:SWEEPTIME 0'
        result = self.functional.convert_scpi_to_usb('DISP:SWEEPTIME', [0])
        self.assertEqual(result, 'sweeptime 0')
        # 'DISPlay:SWEEPTIME 10'
        result = self.functional.convert_scpi_to_usb('DISP:SWEEPTIME', [10])
        self.assertEqual(result, 'sweeptime 10')
        # 'DISPlay:SPUR OFF'
        result = self.functional.convert_scpi_to_usb('DISP:SPUR', [False])
        self.assertEqual(result, 'spur off')
        result = self.functional.convert_scpi_to_usb('DISP:SPUR', [True])
        self.assertEqual(result, 'spur on')

    def testConvertSCPItoUSB_MARK(self):
        # 'MARK:FREQ 1   0'
        result = self.functional.convert_scpi_to_usb('MARK:FREQ', [1, 0])
        self.assertEqual(result, 'marker 1 0')
        # 'MARKer:FREQuency 4 0'
        result = self.functional.convert_scpi_to_usb('MARK:FREQ', [4, 0])
        self.assertEqual(result, 'marker 4 0')
        # 'MARK:FREQ 1      350000000'
        result = self.functional.convert_scpi_to_usb('MARK:FREQ', [1, 350000000])
        self.assertEqual(result, 'marker 1 350000000')
        # 'MARK:FREQ 4      350000000'
        result = self.functional.convert_scpi_to_usb('MARK:FREQ', [4, 350000000])
        self.assertEqual(result, 'marker 4 350000000')
        # 'MARK:DELT 1   1'
        result = self.functional.convert_scpi_to_usb('MARK:DELT', [1, 1])
        self.assertEqual(result, 'marker 1 delta 1')
        # '     MARKer:DELTa 4 1'
        result = self.functional.convert_scpi_to_usb('MARK:DELT', [4, 1])
        self.assertEqual(result, 'marker 4 delta 1')
        # 'MARK:DELT 1      4'
        result = self.functional.convert_scpi_to_usb('MARK:DELT', [1, 4])
        self.assertEqual(result, 'marker 1 delta 4')
        # 'MARK:DELTa 4   4'
        result = self.functional.convert_scpi_to_usb('MARK:DELT', [4, 4])
        self.assertEqual(result, 'marker 4 delta 4')
        # 'MARK:DELT:OFF 1'
        result = self.functional.convert_scpi_to_usb('MARK:DELT:OFF', [1])
        self.assertEqual(result, 'marker 1 delta off')
        # 'MARKer:DELTa:OFF 4'
        result = self.functional.convert_scpi_to_usb('MARK:DELT:OFF', [4])
        self.assertEqual(result, 'marker 4 delta off')
        # 'MARK:NOIS:SET 1'
        result = self.functional.convert_scpi_to_usb('MARK:NOIS:SET', [1])
        self.assertEqual(result, 'marker 1 noise on')
        # 'MARKer:NOISe:SET 4'
        result = self.functional.convert_scpi_to_usb('MARK:NOIS:SET', [4])
        self.assertEqual(result, 'marker 4 noise on')
        # 'MARK:NOIS:OFF 1'
        result = self.functional.convert_scpi_to_usb('MARK:NOIS:OFF', [1])
        self.assertEqual(result, 'marker 1 noise off')
        # 'MARKer:NOISe:OFF 4'
        result = self.functional.convert_scpi_to_usb('MARK:NOIS:OFF', [4])
        self.assertEqual(result, 'marker 4 noise off')
        # 'MARK:TRAK:SET       1'
        result = self.functional.convert_scpi_to_usb('MARK:TRAK:SET', [1])
        self.assertEqual(result, 'marker 1 tracking on')
        # '         MARKer:TRAcKing:SET 4'
        result = self.functional.convert_scpi_to_usb('MARK:TRAK:SET', [4])
        self.assertEqual(result, 'marker 4 tracking on')
        # 'MARK:TRAK:OFF 1'
        result = self.functional.convert_scpi_to_usb('MARK:TRAK:OFF', [1])
        self.assertEqual(result, 'marker 1 tracking off')
        # 'MARKer:TRAcKing:OFF 4'
        result = self.functional.convert_scpi_to_usb('MARK:TRAK:OFF', [4])
        self.assertEqual(result, 'marker 4 tracking off')
        # 'MARK:TRAC 1 1'
        result = self.functional.convert_scpi_to_usb('MARK:TRAC', [1, 1])
        self.assertEqual(result, 'marker 1 trace 1')
        # 'MARKer:TRACe 1 3'
        result = self.functional.convert_scpi_to_usb('MARK:TRAC', [1, 3])
        self.assertEqual(result, 'marker 1 trace 3')
        # 'MARK:TRACe 4 1'
        result = self.functional.convert_scpi_to_usb('MARK:TRAC', [4, 1])
        self.assertEqual(result, 'marker 4 trace 1')
        # 'MARKer:TRAC 4  3'
        result = self.functional.convert_scpi_to_usb('MARK:TRAC', [4, 3])
        self.assertEqual(result, 'marker 4 trace 3')
        # 'MARK:AVER:SET 1'
        result = self.functional.convert_scpi_to_usb('MARK:AVER:SET', [1])
        self.assertEqual(result, 'marker 1 trace_aver on')
        # 'MARKer:AVERage:SET 4'
        result = self.functional.convert_scpi_to_usb('MARK:AVER:SET', [4])
        self.assertEqual(result, 'marker 4 trace_aver on')
        # 'MARK:AVER:OFF 1'
        result = self.functional.convert_scpi_to_usb('MARK:AVER:OFF', [1])
        self.assertEqual(result, 'marker 1 trace_aver off')
        # 'MARKer:AVERage:OFF 4'
        result = self.functional.convert_scpi_to_usb('MARK:AVER:OFF', [4])
        self.assertEqual(result, 'marker 4 trace_aver off')
        result = self.functional.convert_scpi_to_usb('MARK:AVER:OFF', [4])
        self.assertEqual(result, 'marker 4 trace_aver off')

        #TODO: implement the rest of these
        # 'MARK:SRCH:PEAK 1'
        # 'MARKer:SeaRCH:PEAK 4'
        # 'MARK:SRCH:MINR 1'
        # 'MARKer:SeaRCH:MINRight 4'
        # 'MARK:SRCH:MINL 1'
        # 'MARKer:SeaRCH:MINLeft 4'
        #  'MARK:SRCH:MAXR 1'
        #  'MARKer:SeaRCH:MAXRight 4'
        # 'MARK:SRCH:MAXL 1'
        # 'MARKer:SeaRCH:MAXLeft 4'
        # 'MARK:SRCH:FREQ 0 0'
        # 'MARKer:SeaRCH:FREQuency 0 350000000'
        # 'MARK:SRCH:FREQ 350000000 0'
        # 'MARKer:SeaRCH:FREQuency 350000000 350000000'
        # 'MARK:DEL 1'
        # 'MARKer:DELete 4'
        # 'MARK:RST'
        # 'MARKer:ReSeT'
        # 'MARK:DIFF 1 1'
        # 'MARKer:DIFFerence 1 4'
        # 'MARK:DIFFer 4 1'
        # 'MARKer:DIFF 4  4'
        # 'MARK:DIFF:OFF 1'
        # 'MARKer:DIFFerence:OFF 4'
        # 'CONF:CAPT'
        # 'CONFigure:CAPTure'

if __name__ == '__main__':
    unittest.main()
