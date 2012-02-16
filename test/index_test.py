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

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.andre = DummyDocument(42, True, 'Paris')
        self.benedicte = DummyDocument(37, False, 'Paris')

    def test_memory(self):
        idx = MemoryIndex()
        idx.add(self.andre)
        idx.add(self.benedicte)
        self.assertEqual([], list(idx.find('location', 'Strasbourg')))
        self.assertEqual(2, len(list(idx.find('location', 'Paris'))))
        def more_than(x):
            return x > 37
        self.assertEqual(42, list(idx.find('age', more_than))[0].age)

if __name__ == '__main__':
    unittest.main()
