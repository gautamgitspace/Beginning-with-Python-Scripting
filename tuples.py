#tuples are like lists but are immutables like strings
#things you can't do to tuples: modify, sort, append, reverse
#tuples are comparable
tupA=tuple
print dir(tupA)
x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print y
tupA = (0,1,2)
tupB = (0,1,2)
print tupB
if tupA < tupB:
    print 'true'
else:
    print 'false'
#sorting list of tuples: key sorted

d = dict()
m = list()
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

#print top 10 most common words in romeo.txt
d=dict()
l=list()
fileName = raw_input('Enter the name of the file: ')
fileHandle = open(fileName)
for line in fileHandle:
    words=line.rstrip()
    l=words.split()
    for iterator in l:
        d[iterator]=d.get(iterator,0)+1
    for key, value in d.items():
        l.append((value,key))
l.sort(reverse=True)
for value, key in l[:10]:
        print key, value
#shorter version:
print sorted([(value, key) for key, value in d.items()])