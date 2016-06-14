# covers user input, lists, loops and finds count, sum, average, search, detect, smallest, largest in a set of numbers
array_of_numbers = list()
number =  raw_input('Enter the number of elements you want in the array: ')
for i in range (int(number)):
	n = raw_input('number: ')
	array_of_numbers.append(int(n))
print 'Here is your array: ', array_of_numbers
count=0
sum=0
for iterator in array_of_numbers:
    sum=sum+iterator
    count=count+1
print 'Count of elements is: ', count
print 'Sum is: ', sum
print 'Average is: ', sum/count
search_critera = raw_input('Search numbers greater than ? ')
n = int(search_critera)
none_found=True
for i in array_of_numbers:
    if i>n:
        print i, 'is greater than', n
        none_found=False
if none_found==True:
        print 'none found'
found = False
search_critera_2 = raw_input('Check if a number exists in the array. Tell me what to find? ')
n = int(search_critera_2)
for i in array_of_numbers:
    if i==n:
        print 'Found', i, '.'
        found=True
        break
if found==False:
        print 'Not found'