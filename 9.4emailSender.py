#assignment 9.4 @ Coursera
#Write a program to read through the mbox-short.txt
# and figure out who has the sent the greatest number
# of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person
# who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

x = list()
s = list()
sender = dict()
prolificCommitter=None
prolificCommitterCount=None
fileName = 'mbox.txt'
fileHandle = open(fileName)
for line in fileHandle:
    l=line.rstrip()
    if l.startswith('From '):
        x = l.split()
        s.append(x[1])
#print s
for name in s:
    sender[name]=sender.get(name,0)+1
for key,value in sender.items():
    #print key, value
    if prolificCommitter is None or value > prolificCommitterCount:
        prolificCommitterCount=value
        prolificCommitter=key
print prolificCommitter, prolificCommitterCount
