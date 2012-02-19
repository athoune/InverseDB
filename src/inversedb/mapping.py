def mapping(document):
    "Simple mapping, each object's attribute becomes a key"
    r = {}
    for column in vars(document):
        value = document.__getattribute__(column)
        r[column] = value
    return r
