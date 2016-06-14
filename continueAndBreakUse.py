print 'hello. I will echo everything until you write "done" >_'
print 'hello. I will accept more input if your input begins with a pound sign'
while True:
    line = raw_input('> ')
    if line[0]=='#':
        continue
    elif line=='done':
        break
    print line
print 'execution complete!'
print 'bye'