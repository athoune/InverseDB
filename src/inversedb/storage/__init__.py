from inversedb.column import Column

class Storage(object):

    def __init__(self, name, column = None):
        self.columns = {}
        self.name = name
        if column == None:
            column = Column()
        self.column = column

    def set(self, column, key, value):
        if column not in self.columns:
            self.columns[column] = self.new_db(column)
        self.columns[column][str(key)] = self.column.dehydrate(value)

    def get(self, column, key):
        return self.column.hydrate(self.columns[column][str(key)])

    def has_column(self, column):
        return self.columns.has_key(column)

    def has_key(self, column, key):
        if not self.columns.has_key(column):
            return False
        return self.columns[column].has_key(str(key))

    def keys(self, column):
        for key in self.columns[column].keys():
            yield key

class MemoryStorage(Storage):

    def new_db(self, column):
        return {}
