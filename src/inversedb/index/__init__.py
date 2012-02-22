from intbitset import intbitset
from inversedb.storage import MemoryStorage

class Index(object):

    def __init__(self):
        self.storage = MemoryStorage
        self.idx = 0
        self.store = self.storage('store')
        self.inverse = self.storage('inverse')

    def nextId(self):
        #[FIXME] Mock
        self.idx += 1
        return self.idx

    def find(self, column, value):
        if self.inverse.has_column(column):
            if hasattr(value, '__call__'):
                result = intbitset()
                for k in self.inverse.keys(column):
                    if value(k):
                        result.union_update(self.inverse.get(column, k))
                return result
            else:
                if self.inverse.has_key(column, value):
                    return self.inverse.get(column, value)
        return intbitset()

    def fetch(self, column, keys):
        for key in keys:
            yield self.unserialize_document(self.store.get(column, key))

    def serialize_document(self, document):
        return document

    def unserialize_document(self, serialized):
        return serialized

    def add_document(self, document):
        document['_id'] = self.nextId() #FIXME if _id doesn't already exist
        for column in document:
            values = document[column]
            self.add(document['_id'], column, values)
            self.add_inverse(document['_id'], column, values)
        return document

    def add(self, id_, column, values):
        self.store.set(column, id_,  self.serialize_document(values))

    def add_inverse(self, id_, column, values):
        if type(values) is not list:
            values = [values]
        for value in values:
            if not self.inverse.has_key(column, value):
                temp = intbitset()
            else:
                temp = self.inverse.get(column, value)
            temp.add(id_)
            self.inverse.set(column, value, temp)

    def merge(self, index):
        for column in index.store.columns():
            for key in index.store.keys(column):
                self.store.set(column, key, index.store.get(column, key))
        for column in index.inverse.columns():
            for key in index.inverse.keys(column):
                if not self.inverse.has_key(column, key):
                    self.inverse.set(column, key, index.inverse.get(column, key))
                else:
                    me = intbitset()
                    me.fastload(self.inverse.get(column, key))
                    other = intbitset()
                    other.fastload(index.inverse.get(column, key))
                    me.union_update(other)
                    self.inverse.set(column, key, me)

class MemoryIndex(Index):

    def new_db(self, name):
        return {}

