import intbitset
import anydbm
import os

from inversedb.index import Index

class DbmIndex(Index):

    def __init__(self, path):
        self.path = path
        self.store = anydbm.open(os.path.join(path, 'store'),'c')
        self.dbs = {}

    def merge(self, index):
        #TODO copy store
        for column in index.values.keys():
            if column not in ['_id']:
                if not self.dbs.has_key(column):
                    self.dbs[column] = anydbm.open(os.path.join(self.path, column),'c')
                for value in index.values[column]:
                    serialized = str(value) #FIXME better serialisation
                    if self.dbs[column].has_key(serialized):
                        old = intbitset.intbitset().fastload(self.dbs[column][serialized])
                    else:
                        old = intbitset.intbitset([])
                    old.union_update(index.values[column][value])
                    self.dbs[column][serialized] = old.fastdump()
