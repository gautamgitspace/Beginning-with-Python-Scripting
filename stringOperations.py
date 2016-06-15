#string operations and text parsing examples. covers - string slicing, converting, looping through strings, string search, replace,
str=raw_input('Enter a string with some repeating words: ')
print 'string in uppercase is: ', str.upper()
str2=raw_input('Enter a word and I will let you how many times it occurs in your string: ')
pos = str.find(str2)
if str2 in str:
	substr_count = str.count(str2,0,45)
	print 'FOUND', str2, substr_count, 'times in the string you entered. First occurence is at: ', pos
else:
	print 'NOT FOUND'
s3=raw_input('Enter a word to be replaced: ')
s4=raw_input('Enter a word to be replaced with: ')
str3=str.replace(s3,s4)
print 'Here is your new string: ', str3
s5=raw_input('Enter your email followed by your last name and first name ')
posOfAt = s5.find('@')
posOfSpace = s5.find(' ')
print 'your username is: ', s5[0:posOfAt]
print 'your host server is: ', s5[posOfAt+1:posOfSpace]
s2=raw_input('Enter a number and I will print its multiplication table for you: ')
multiple = int(s2)
count=0
print 'Printing table for', multiple
for i in 'university':
	count=count+1
	print count*multiple