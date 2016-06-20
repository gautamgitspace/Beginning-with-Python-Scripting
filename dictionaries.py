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
#most common word in a documentFord
counter = dict()
line2=''
words=''
fileName = raw_input('Enter the name of the file: ')
try:
    fileHandle = open(fileName)
    for line in fileHandle:
        line2=line2+line
    words=line2.split()
    #split() splits a string and produces a list *IMP*
    print words
    for word in words:
        counter[word]=counter.get(word,0)+1
        #print word + ':' + str(counter[word])
    print counter
    print max(counter) + ' appears the most in the file'
except:
    print 'The file you are trying to open does not exist'