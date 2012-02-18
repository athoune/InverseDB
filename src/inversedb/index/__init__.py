from intbitset import intbitset

class Index(object):

    def __init__(self):
        self.store = self.new_db('store')
        self.idx = 0
        self.values = {}

    def new_db(self, name):
        pass

    def nextId(self):
        #[FIXME] Mock
        self.idx += 1
        return self.idx

    def __getitem__(self, key):
        return self.unserialize_document(self.store[self.serialize(key)])

    def find(self, column, value):
        if self.values.has_key(column):
            if hasattr(value, '__call__'):
                result = intbitset()
                for k in self.values[column]:
                    if value(k):
                        result.union_update(self.values[column][k])
                return result
            else:
                value = self.serialize(value)
                if self.values[column].has_key(value):
                    return self.values[column][value]
        return intbitset()

    def fetch(self, keys):
        for key in keys:
            yield self.__getitem__(key)

    def serialize(self, value):
        return str(value)

    def serialize_document(self, document):
        return document

    def unserialize_document(self, serialized):
        return serialized

    def add(self, document):
        document._id = self.nextId() #FIXME if _id doesn't already exist
        self.store[self.serialize(document._id)] = self.serialize_document(document)
        for column in vars(document):
            value = self.serialize(document.__getattribute__(column))
            if not self.values.has_key(column):
                self.values[column] = self.new_db(column)
            if not self.values[column].has_key(value):
                self.values[column][value] = intbitset()
            self.values[column][value].add(document._id)
        return document

    def merge(self, index):
        for _id in index.store:
            self.store[_id] = self.serialize_document(index[_id])
        for column in index.values:
            if column not in ['_id']:
                if not self.values.has_key(column):
                    self.values[column] = self.new_db(column)
                for value in index.values[column]:
                    old = intbitset()
                    if self.values[column].has_key(value):
                        old.fastload(self.values[column][value])
                    old.union_update(index.values[column][value])
                    self.values[column][value] = old.fastdump()

class MemoryIndex(Index):

    def new_db(self, name):
        return {}

