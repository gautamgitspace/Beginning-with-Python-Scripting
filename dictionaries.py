#collections part 2 - dictionaries
#uses - 1. How often we see something? Dictionar, the best datastructure to keep a simultaneous count.
#how often do we see a Dodge, Chevy or a Ford
count = dict()
name = list()
names = ['Chevy', 'Dodge', 'Ford', 'Chevy', 'Ford', 'Ford', 'Dodge', 'Ford']
for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1
print count
#how to do the above in one single line?
for name in names:
    count[name]=count.get(name,0)+1
print count
#most common word in a document
counter = dict()
line2=''
words=''
bigWord = None
bigCount = None
fileName = raw_input('Enter the name of the file: ')
try:
    fileHandle = open(fileName)
    for line in fileHandle:
        line2=line2+line
    words=line2.split()
    #split() splits a string and produces a list *IMP*
    for word in words:
        counter[word]=counter.get(word,0)+1
        #print word + ':' + str(counter[word])
    for key,value in counter.items():
        print key, value
        if bigCount is None or value>bigCount:
            bigCount=value
            bigWord=key
    print bigWord + ' appears ' + str(bigCount) + ' times'
except:
    print 'The file you are trying to open does not exist'
#Lists of keys and values
print '\n'
print counter
print 'dict converted into LIST: ', list(counter)
print 'This will give a LIST of KEYS in the dictionary: ', counter.keys()
print 'This will give a LIST of VALUES in the dictionary: ', counter.values()
print 'This will give a LIST of ITEMS in the dictionary', counter.items()
stuff = dict()
print stuff.get('candy',-1)