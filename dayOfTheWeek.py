#find the day of the week on which mail was received
#double split
import os
fileName = raw_input('enter the name of the file with extension:')
print fileName
print os.path.exists('mbox.txt')
try:
    print 'here'
    fileHandle = open(fileName)
    for line in fileHandle:
        l=line.rstrip()
        if not l.startswith('From '):
            continue
        else:
            splitter=l.split()
            splitter2=splitter[1].split('@')
            print 'Received a mail from : '+splitter2[0]+' AT '+splitter2[1]+' on ' +splitter[2]
except:
    print 'The file you are looking for does not exist - ',
