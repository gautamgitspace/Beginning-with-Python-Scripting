#Lists are mutable in python. Strings are not.
friends = ['Joy', 'Roy', 'Toy']
print range(len(friends))
friends = ['Joy', 'Roy', 'Toy', 'Boy']
print range(len(friends))
#tale of two loops
for friend in friends:
    print 'Have a good one', friend
for i in range(len(friends)):
    friend=friends[i]
    print 'have a nice one', friend
#concat lists
enemies = [1,2,3,4]
result = enemies + friends
print result
#slice lists
print enemies[1:3]
print friends[0:4]
x = list()
print type(x)
print 'what all I can do with a list? Uncomment below and see: '
#print dir(x)
#search a list by building it from scratch
x = list()
x.append('1')
x.append('hello')
x.append('kitty')
print x
isThere = 'hello' in x
print isThere
isThere = 'jello' not in x
print isThere
#sort lists
print 'before sort: ', friends
friends.sort()
print 'after sort: ', friends
#built in functions
list = list()
i=0
print "Enter numbers and i'll calculate the max, min, avg for you. Type 'done' when you are actually done"
while True:
    try:
        number = raw_input('number: ')
        if number=='done':
            break
        else:
            n=float(number)
            list.append(n)
    except:
        print 'INVALID INPUT FOOL'
count=len(list)
total=sum(list)
if len(list)!=0:
    print 'MAX: ', max(list)
    print 'MIN: ', min(list)
    avg=total/count
    print 'avg is: ', avg
#split: python does the hard work of finding the spaces. many spaces = 1 space
abc = 'hello I am Wayne'
splitter = abc.split()
print splitter
xyz = 'itemName; itemID; itemPrice; itemAisle'
splitter2 = xyz.split(';')
print  splitter2