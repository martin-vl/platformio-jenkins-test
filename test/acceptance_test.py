#!/usr/bin/env python

import unittest
import serial

class AcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.dutSerial=serial.Serial('/dev/ttyUSB0',115200,timeout=1)

    def tearDown(self):
        self.dutSerial.close()

    def testHelloOnSerial(self):
        line = self.dutSerial.readline()
        self.assertEqual(line,'Hallo!!\r\n')

if __name__ == '__main__':
    unittest.main()
