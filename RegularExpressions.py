#RegularExpressions
import re
fineHandle = open('mbox.txt')
count=0
for line in fineHandle:
    line=line.rstrip()
    if re.search('^X.+:', line):
        count=count+1
        print line
print 'COUNT: ', count

#findall gives back a python list
x = 'My shoe size is 9 (US) which is 8 (UK). Sometimes 10 (US) also fits.'
f = 'From: agautam2@buffalo.edu To: ubwins.cse@buffalo.edu'
y = re.findall('[0-9]+', x)
g = re.findall('[AEIOU]', x)
r = re.findall('^F.+:',f)
b = re.findall('^F.+?:',f)
print 'Here you go! all the numbers returned in the form of a python list: ', y
print 'Here you go! all the caps vowels returned in the form of a python list: ', g
print 'Greedy approach(longest match): ', r
print 'Non Greedy approach(short match): ', b

# finding everything to the left and right of '@'
# can also be done by double split

fileHandle2 = open ('mbox.txt')
for line in fileHandle2:
    line=line.rstrip()
    if re.search('^From.*', line):
        s = line
        g = re.findall('\S+@\S+', s)
        data = g[0]
        atpos = data.find('@')
        spacepos = data.find(' ', atpos)
        #using string slicing now to get the hostname
        hostname = data[atpos+1: spacepos]
        print 'using regex and slicing:', hostname

# doing the same using the NOT operator
fileHandle = open('mbox.txt')
for line in fileHandle:
    line = line.rstrip()
    if re.findall('^From .*@([^ ]*)', line):
        y = re.findall('^From .*@([^ ]*)', line)
        print 'using ^ operator:', y

# printing the largest float in the lines resembling: 'X-DSPAM-Confidence: some float value"
listOfIntegers = list()
fileHandle3 = open('mbox.txt')
for line in fileHandle3:
    line = line.rstrip()
    if re.findall('^X-DSPAM-Confidence:.*', line):
        h = re.findall('^X-DSPAM-Confidence:.*', line)
        #print h[0]
        splitter = h[0].split(':')
        a = float(splitter[1])
        listOfIntegers.append(a)
print '\nmax of all float values: ', max(listOfIntegers)





