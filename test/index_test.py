import unittest
from intbitset import intbitset
from utils import TestInverse
import inversedb.query as query

class TestIndex(TestInverse):

    def test_memory(self):
        self.assertEqual(0, len(list(self.idx.find('location', 'Strasbourg'))))
        self.assertEqual(3, len(list(self.idx.find('location', 'Paris'))))
        def more_than(x):
            return int(x) > 37
        self.assertEqual([42, 74], [a['age'] for a in self.idx.fetch(self.idx.find('age', more_than))])
        males_in_Paris = self.idx.fetch(self.idx.find('sexe', True) & self.idx.find('location', 'Paris'))
        self.assertEqual(2, len(list(males_in_Paris)))
        beer_drinker = self.idx.find('fanof', 'beer')
        self.assertEqual(2, len(list(beer_drinker)))

    def test_query(self):
        parisians = query.equal('location', 'Paris')(self.idx)
        self.assertEqual(intbitset([1,2,3]), parisians)
        older = query.more_than('age', 37)(self.idx)
        self.assertEqual(intbitset([1, 3]), older)

    def test_parsing(self):
        q = query.query(self.idx, {
            'and': [
                {'equal': ['location', 'Paris']},
                {'more_than': ['age', 37]}
            ]})
        self.assertEqual(intbitset([1, 3]), q)

if __name__ == '__main__':
    unittest.main()
