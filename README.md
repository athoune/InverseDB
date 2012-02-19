InverseDB
=========

Column oriented storage for python.

Install
-------

    sudo pip install intbitset

Example
-------

```python
# Document are dictionnaries
andre = {'age': 37, 'sexe': True, 'location': 'Paris'}
berenice = {'age': 27, 'sexe': False, 'location': 'Paris'}

idx = MemoryIndex()
idx.add(andre)
idx.add(berenice)

# It's an index, I can find by key
in_paris = idx.find('location', 'Paris')
male = idx.find('sexe', True)

# Results are set, wich handle binary operation
male_in_paris = in_paris & male

# Document are also stored
print list(idx.fetch(male_in_paris))

# Search can be more dynamic
def more_than(x):
    return int(x) > 27 #key is a string
idx.find('age', more_than)
```

Licence
-------

MIT ©Mathieu Lecarme 2012
