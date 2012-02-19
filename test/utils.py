import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) +  '/../src'))
from inversedb.index import MemoryIndex


class TestInverse(unittest.TestCase):

    def setUp(self):
        self.andre = {'age': 42, 'sexe': True, 'location': 'Paris'}
        self.benedicte = {'age': 37, 'sexe': False, 'location': 'Paris'}
        self.casimir = {'age': 74, 'sexe': True, 'location': 'Paris'}
        self.idx = MemoryIndex()
        self.idx.add(self.andre)
        self.idx.add(self.benedicte)
        self.idx.add(self.casimir)

