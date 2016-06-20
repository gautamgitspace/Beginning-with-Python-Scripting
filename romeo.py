#Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words
# using the split() method. The program should build
# a list of words. For each word on each line check
# to see if the word is already in the list and if not
#  append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.

fileName = raw_input('Enter the name of the file: ')
bigString = list()
result = list()
try:
    fileHandle = open(fileName)
    for line in fileHandle:
        line.rsplit()
        splitter=line.split()
        #print splitter
        bigString=bigString+splitter
    print 'Consolidated List: ', bigString
    for eachWord in bigString:
        if eachWord not in result:
            result.append(eachWord)
    print 'Unique list: ', result
    result.sort()
    print 'Sorted List: ', result


except:
    print 'The file you are trying to access does not exist'