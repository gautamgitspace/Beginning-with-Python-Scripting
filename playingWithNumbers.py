# covers user input, lists, loops and finds count, sum, average, search, detect, smallest, largest in a set of numbers
array_of_numbers = list()
number =  raw_input('Enter the number of elements you want in the array: ')
try:
    for i in range (int(number)):
        n = raw_input('number: ')
        array_of_numbers.append(int(n))
except:
    print 'INVALID INPUT. MUST BE A NUMERIC'
    exit()
print 'Here is your array: ', array_of_numbers
count=0
sum=0
largest=-1
smallest=None
for iterator in array_of_numbers:
    sum=sum+iterator
    count=count+1
    if iterator>largest:
        largest=iterator
    if smallest is None:
        smallest=iterator
    elif iterator<smallest:
        smallest=iterator
print 'Count of elements is: ', count
print 'Sum is: ', sum
print 'Average is: ', sum/count
print 'Largest element is: ', largest
print 'Smallest element is: ', smallest
search_critera = raw_input('Search numbers greater than ? ')
try:
    n = int(search_critera)
    none_found=True
    for i in array_of_numbers:
        if i>n:
            print i, 'is greater than', n
            none_found=False
    if none_found==True:
        print 'none found'
except:
    print 'INVALID INPUT. MUST BE A NUMERIC'
    exit()
found = False
search_critera_2 = raw_input('Check if a number exists in the array. Tell me what to find? ')
try:
    n = int(search_critera_2)
    for i in array_of_numbers:
        if i==n:
            print 'Found', i
            found=True
            break
    if found==False:
        print 'Not found'
except:
    print 'INVALID INPUT. MUST BE A NUMERIC'