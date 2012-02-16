class MemoryIndex(object):
    values = {}
    idx = 0

    def add(self, document):
        document._idx = self.idx
        for k in vars(document):
            v = document.__getattribute__(k)
            if not self.values.has_key(k):
                self.values[k] = {}
            if not self.values[k].has_key(v):
                self.values[k][v] = []
            self.values[k][v].append(self.idx)
        self.idx += 1
