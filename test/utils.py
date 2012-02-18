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

    def __repr__(self):
        return "<Doc %i %s %s>" % (self.age, self.sexe, self.location)

class TestInverse(unittest.TestCase):

    def setUp(self):
        self.andre = DummyDocument(42, True, 'Paris')
        self.benedicte = DummyDocument(37, False, 'Paris')
        self.casimir = DummyDocument(74, True, 'Paris')
        self.idx = MemoryIndex()
        self.idx.add(self.andre)
        self.idx.add(self.benedicte)
        self.idx.add(self.casimir)

