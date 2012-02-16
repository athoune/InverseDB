import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) +  '/../src'))
from inversedb.index import MemoryIndex
from inversedb.document import Document

class DummyDocument(Document):
    def __init__(self, age, sexe, location):
        self.age = age
        self.sexe = sexe
        self.location = location

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.andre = DummyDocument(42, True, 'Paris')
        self.benedicte = DummyDocument(37, False, 'Paris')

    def test_memory(self):
        idx = MemoryIndex()
        idx.add(self.andre)
        idx.add(self.benedicte)
        print idx.values

if __name__ == '__main__':
    unittest.main()
