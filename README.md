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
idx.add_document(andre)
idx.add_document(berenice)

# It's an index, I can find by key
in_paris = idx.find('location', 'Paris')
male = idx.find('sexe', True)

# Results are set, wich handle binary operation
male_in_paris = in_paris & male

# Search can be more dynamic
def more_than(x):
    return int(x) > 27 #key is a string
idx.find('age', more_than)

# JSON like query syntax
# the sum of age of all men :
q = query.query(self.idx, {
    'sum':['age', {
        'equal': ['sexe', True]
        }]
    })

```

Technical implementation
------------------------

InverseDb is a pedagogical projet.
It try to show how inversed index works and RDBMS are not "one size fits all" tools.
Inversedb use the same inversed pattern of [Lucene](http://lucene.apache.org/core/).

Persistance is done with simple key-value storage.
For now, ram and gdbm storage are provided, and soon [KyotoCabinet](http://fallabs.com/kyotocabinet/) and [LevelDB](http://code.google.com/p/leveldb/).

InverseDb actions are easy to parralelized, and will fit well with multicore and multiserver architecture.

Licence
-------

MIT ©Mathieu Lecarme 2012
