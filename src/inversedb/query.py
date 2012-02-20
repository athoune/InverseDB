
def equal(column, value):
    return lambda index : index.find(column, value)

def more_than(column, value):
    return lambda index : index.find(column, lambda key: int(key) > value)
