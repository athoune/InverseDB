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
                self.values[k][v] = []
            self.values[k][v].append(self.idx)
        self.idx += 1
        return document

    def __getitem__(self, key):
        return self.store[key]

    def find(self, column, value):
        if not self.values.has_key(column):
            return None
        if not self.values[column].has_key(value):
            return None
        return [self.__getitem__(i) for i in self.values[column][value]]
