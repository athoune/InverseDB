import anydbm
import os
import cPickle as pickle

from inversedb.index import Index

class DbmIndex(Index):

    def __init__(self, path):
        self.path = path
        Index.__init__(self)

    def new_db(self, name):
        return anydbm.open(os.path.join(self.path, name),'c')

    def serialize_document(self, document):
        return pickle.dumps(document)

    def unserialize_document(self, serialized):
        return pickle.loads(serialized)
