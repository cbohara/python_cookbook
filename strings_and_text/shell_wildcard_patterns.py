# match text using unix shell commands
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
# True

print(fnmatch('foo.txt', '?oo.txt'))
# True

print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
# True

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
filtered = [name for name in names if fnmatch(name, 'Dat*.csv')]

# ex: create a list of just the addresses ending in street
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

streets_only = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(streets_only)
