from utils import TestInverse
import unittest

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

if __name__ == '__main__':
    unittest.main()
