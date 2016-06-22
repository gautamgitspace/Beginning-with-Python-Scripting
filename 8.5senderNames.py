fileName = raw_input('Enter the file you want to open: ')
fileHandle = open(fileName)
t = list()
count =0
for line in fileHandle:
    l=line.rstrip()
    if l.startswith('From '):
        t=l.split()
        print t[1]
        count = count + 1
print 'There were '+ str(count) + ' lines in the file with From as the first word'
