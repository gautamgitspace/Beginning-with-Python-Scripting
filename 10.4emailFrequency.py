#10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the
# 'From ' line by finding the time and then splitting the
# string a second time using a colon.

fileName = raw_input('Enter the file you want to open: ')
fileHandle = open(fileName)
t = list()
m = list()
d = dict()
u = list()
for line in fileHandle:
    l=line.rstrip()
    if l.startswith('From '):
        t=l.split()
        m=t[5].split(':')
        u.append(m[0])
for iterator in u:
    d[iterator]=d.get(iterator,0)+1
for hour, emailCount in sorted(d.items()):
    print hour, emailCount








