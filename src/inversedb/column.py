import struct
from intbitset import intbitset

class Column(object):

    def __init__(self, inversed = False):
        self.inversed = inversed

    def dehydrate(self, data):
        return data

    def hydrate(self, data):
        return data

class IntColumn(Column):

    def dehydrate(self, data):
        return struct.pack("<i", data)

    def hydrate(self, data):
        return struct.unpack("<i", data)[0]

class InversedColumn(Column):

    def dehydrate(self, data):
        return data.fastdump()

    def hydrate(self, data):
        bitset = intbitset()
        bitset.fastload(data)
        return bitset
