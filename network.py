#code to open a tcp connection to a server listening on a port
#run assignment1 in server mode on port 3369 first

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

# import urllib
# d=dict()
# m=list()
# bigWord = None
# bigCount = None
# pageHandle = urllib.urlopen('http://www.py4inf.com/code/words.txt')
# for line in pageHandle:
#     line=line.strip()
#     words=line.split()
#     for word in words:
#         d[word]=d.get(word,0)+1
#         for key, value in d.items():
#             #print key, value
#             if bigWord is None or value > bigCount:
#                 bigCount=value
#                 bigWord=key
# print bigWord, bigCount
