inp = input('Enter a file name:')
try:
    fhand = open(inp)
except:
    print('File does not exist:',inp)
    quit()

count = 0
total =  0
for i in fhand:
    if 'X-DSPAM-Confidence:' in i:
        count += 1
        fnd = i.find(':')
        val = i[ fnd+1: ]
        num = float(val)
        total += num
    else:
        continue

print('Average spam confidence:', total/count)