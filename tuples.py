#tuples are like lists but are immutables like strings
#things you can't do to tuples: modify, sort, append, reverse
#tuples are comparable
tupA = (0,1,2)
tupB = (0,1,2)
if tupA < tupB:
    print 'true'
else:
    print 'false'
#sorting list of tuples: key sorted

d = dict()
m=list()
d = {'z': 10, 'b': 20, 'a': 4}
print '\nKey Value Pairs in dict: '
for k, v in d.items():
    print k, v
print '\nKey Sorted Order: '
for k, v in sorted(d.items()):
    print k, v

#sorting list of tuples: value sorted
for k,v in d.items():
    m.append((v,k))
print ('\nValue Sorted Order: ')
print 'unsorted: ', m
m.sort(reverse=True)
print 'sorted: ', m