print 'hello. I will echo everything until you write "done"'
print "hello. I will accept more input if your input begins with a pound sign and I won't echo"
while True:
    line = raw_input('>')
    if line[0]=='#':
        continue
    elif line=='done':
        break
    print line
print 'execution complete!'
print 'bye'