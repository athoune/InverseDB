import anydbm
import os
from inversedb.storage import Storage

class DbmStorage(Storage):

    def __init__(self, path, name):
        Storage.__init__(self, name)
        self.path = path

    def new_db(self, column):
        os.makedirs(os.path.join(self.path, self.name))
        return anydbm.open(os.path.join(self.path, self.name, column), 'c')
