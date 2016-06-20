#collections part 2 - dictionaries
#uses - 1. How often we see something? Dictionar, the best datastructure to keep a simultaneous count.
#how often do we see a Dodge, Chevy or a Ford
count = dict()
name = list()
names = ['Chevy', 'Dodge', 'Ford', 'Chevy', 'Ford', 'Ford', 'Dodge', 'Ford']
for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1
print count
#how to do the above in one single line?
for name in names:
    count[name]=count.get(name,0)+1
print count