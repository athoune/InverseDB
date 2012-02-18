from utils import TestInverse
import unittest
from inversedb.index.dbm import DbmIndex

class TestDbmIndex(TestInverse):

    def test_merge(self):
        k = DbmIndex('/tmp/')
        k.merge(self.idx)

if __name__ == '__main__':
    unittest.main()

