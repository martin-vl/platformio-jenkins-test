#!/usr/bin/env python

import unittest

class AcceptanceTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
