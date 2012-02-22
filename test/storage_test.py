import unittest
import sys
import shutil
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) +  '/../src'))

from inversedb.storage import MemoryStorage
from inversedb.storage.dbm import DbmStorage

class TestStorage(unittest.TestCase):

    def test_getset(self):
        try:
            shutil.rmtree('/tmp/inverse')
        except OSError:
            pass
        for storage in [MemoryStorage('test'), DbmStorage('/tmp/inverse', 'test')]:
            storage.set('name', 42, 'Robert')
            self.assertEqual('Robert', storage.get('name', 42))

if __name__ == '__main__':
    unittest.main()
