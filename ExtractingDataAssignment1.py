#sum of digits from the file regex_sum_42.txt
import re

fileName = 'regex_sum_42.txt'
fileHandle = open(fileName)
count = 0
sum = 0
listOfNumbers = list()
for line in fileHandle:
    line=line.rstrip()
    if re.findall('[0-9.]+', line):
        num = re.findall('([0-9]+)', line)
        #print num
        for numbers in num:
            listOfNumbers.append(float(numbers))
for iterator in listOfNumbers:
    sum = sum + iterator
print 'Sum of digits is: ' + str(sum)