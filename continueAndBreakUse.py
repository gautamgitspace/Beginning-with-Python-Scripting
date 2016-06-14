print 'hello. I will echo everything until you write "done" >_'
while True:
    line = raw_input('> ')
    if line[0]=='#':
        continue
    elif line=='done':
        break
    print line
print 'execution complete!'
print 'bye'