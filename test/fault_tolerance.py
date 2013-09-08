#! /usr/bin/env python

'''Test broken connection handling'''

import os
import unittest
import pyreBloom


class CrashTest(unittest.TestCase):
    def setUp(self):
        os.system('sudo service redis-server start')
        self.bloom = pyreBloom.pyreBloom('pyreBloomTesting', 10000, 0.1)
        self.bloom.delete()

    def tearDown(self):
        self.setUp()

    def test_broken_connection_raises_exception(self):
        '''Broken connection should result in pyreBloomException'''
        os.system('sudo service redis-server stop')
        
        operations = [
            lambda: self.bloom.add('hello'),
            lambda: self.bloom.extend(['hello', 'world']),
            lambda: self.bloom.contains('hello'),
            self.bloom.delete,
        ]

        for operation in operations:
            self.assertRaises(pyreBloom.pyreBloomException, operation)


if __name__ == '__main__':
    unittest.main()
