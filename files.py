#file processing, text processing in files
fname=raw_input('Enter the file name with extension ')
try:
    fileHandle = open(fname)
except:
    print 'bad file name or file does not exist in the pwd'
    exit()
input=fileHandle.read()
print input[0:17]
count=0
fileHandle = open(fname)
for line in fileHandle:
    count=count+1
print 'FILE PROPERTIES: Line count: ', count, 'char count: ', len(input)
print '----------------------------------------------------------------------'
print 'This file contains lines starting with @, # and $. You can mention one\nof the special character and i will fetch those lines for you: '
print '----------------------------------------------------------------------'
filter=raw_input()
no_match = False
print 'Filter Criteria: '+ filter
print 'OK HERE YOU GO\n.\n.\n.\n.'
fileHandle = open('words.txt')
for line in fileHandle:
    line = line.rstrip()
    if line.startswith(filter):
        print line
