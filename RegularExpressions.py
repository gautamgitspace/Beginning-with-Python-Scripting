#RegularExpressions
import re
fineHandle = open('mbox.txt')
count=0
for line in fineHandle:
    line=line.rstrip()
    if re.search('^X.*', line):
        count=count+1
        print line
print 'COUNT: ', count

#findall gives back a python list
x = 'My shoe size is 9 (US) which is 8 (UK). Sometimes 10 (US) also fits.'
y = re.findall('[0-9]+', x)
print 'Here you go, all the numbers returned in the form of a python list: ', y