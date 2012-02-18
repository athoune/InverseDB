import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) +  '/../src'))
from inversedb.index import MemoryIndex
from inversedb.index.dbm import DbmIndex
from inversedb.document import Document

class DummyDocument(Document):
    def __init__(self, age, sexe, location):
        self.age = age
        self.sexe = sexe
        self.location = location

    def __repr__(self):
        return "<Doc %i %s %s>" % (self.age, self.sexe, self.location)

class TestDbmIndex(unittest.TestCase):

    def setUp(self):
        self.andre = DummyDocument(42, True, 'Paris')
        self.benedicte = DummyDocument(37, False, 'Paris')
        self.casimir = DummyDocument(74, True, 'Paris')

    def test_merge(self):
        idx = MemoryIndex()
        idx.add(self.andre)
        idx.add(self.benedicte)
        idx.add(self.casimir)
        k = DbmIndex('/tmp/')
        k.merge(idx)

if __name__ == '__main__':
    unittest.main()

