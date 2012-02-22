class Storage(object):

    def __init__(self, name):
        self.columns = {}
        self.name = name

    def set(self, column, key, value):
        if column not in self.columns:
            self.columns[column] = self.new_db(column)
        self.columns[column][str(key)] = value

    def get(self, column, key):
        return self.columns[column][str(key)]

class MemoryStorage(Storage):

    def new_db(self, column):
        return {}
