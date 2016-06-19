#7.2 coursera - python data structures
fileName = raw_input('Enter file name to open: ')
try:
    fhandle = open(fileName)
except:
    print 'invalid file name'
count = 0
sum_of_trimmed_data = 0
avg_of_trimmed_data = 0
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        count=count+1
        line2=line.rstrip()
        #print line2
        pos=line2.find('0')
        s=float(line2[pos:pos+6])
        #print s
        sum_of_trimmed_data=sum_of_trimmed_data+s
        avg_of_trimmed_data=sum_of_trimmed_data/count
print avg_of_trimmed_data
