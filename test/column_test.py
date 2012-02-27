import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) +  '/../src'))

from inversedb.column import IntColumn, InversedColumn
from intbitset import intbitset

class TestColumn(unittest.TestCase):

    def test_bitset(self):
        c = InversedColumn()
        value = intbitset([1, 2, 3])
        hydrated = c.dehydrate(value)
        self.assertEqual(value, c.hydrate(hydrated))

    def test_int(self):
        c = IntColumn()
        value = 42
        hydrated = c.dehydrate(value)
        self.assertEqual(value, c.hydrate(hydrated))

if __name__ == '__main__':
    unittest.main()
