def equal(column, value):
    return lambda index : index.find(column, value)

def more_than(column, value):
    return lambda index : index.find(column, lambda key: int(key) > value)

def and_(a, b):
    return lambda idx : query(idx, a) & query(idx, b)

def or_(a, b):
    return lambda idx : query(idx, a) | query(idx, b)

def not_(a):
    return lambda idx : not query(idx, a)

def fetch(column, a):
    return lambda idx : idx.fetch(column, query(idx, a))

def sum_(column, a):
    return lambda idx : sum(idx.fetch(column, query(idx, a)))

mapping = {
    'equal': equal,
    'more_than': more_than,
    'and': and_,
    'or': or_,
    'not': not_,
    'sum': sum_,
    'fetch': fetch
    }

def query(index, q):
    action = q.keys()[0]
    args = q[action]
    return mapping[action](*args)(index)
