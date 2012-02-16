from intbitset import intbitset

class Index(object):
    def add(self, document):
        pass

class MemoryIndex(Index):
    values = {}
    store = {}
    idx = 0

    def add(self, document):
        document._idx = self.idx
        self.store[self.idx] = document
        for k in vars(document):
            v = document.__getattribute__(k)
            if not self.values.has_key(k):
                self.values[k] = {}
            if not self.values[k].has_key(v):
                self.values[k][v] = intbitset()
            self.values[k][v].add(self.idx)
        self.idx += 1
        return document

    def __getitem__(self, key):
        return self.store[key]

    def find(self, column, value):
        if self.values.has_key(column):
            if hasattr(value, '__call__'):
                for k in self.values[column].keys():
                    if value(k):
                        for d in self.values[column][k]:
                            print d
                            yield self.__getitem__(d)
            elif self.values[column].has_key(value):
                for i in self.values[column][value]:
                    yield self.__getitem__(i)
