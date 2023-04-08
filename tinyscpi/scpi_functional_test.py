import unittest
from tinyscpi.scpi_functional import SCPI_functional
from tinyscpi.scpi_parser import SCPI_Parser
class FunctionalTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.functional = SCPI_functional()
        self.parser = SCPI_Parser()
    def testConvertSCPItoUSB(self):
        self.assertEqual(True)
        #TODO: Unimplemented Method Stub

    def testSend(self):
        self.assertEqual(True)
        #TODO: Unimplemented Method Stub

if __name__ == '__main__':
    unittest.main()
