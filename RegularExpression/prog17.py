#Regular Expression
import re

inp = input('Enter the file:')
try:
    fhand = open(inp)
except:
    print('File can''t be opened:',inp)
    quit()

count = 0
total = 0
for line in fhand:
    if not re.search('^New', line):
        continue
    else:
        gt = re.findall('^N.*:\s([0-9]+)', line)  
        #('[0-9]+',line) or (':\s([0-9]+)',line) or ('^New .*:\s([0-9]+)', line)
        num = int(gt[0])
        count += 1
        total += num

print('Average:',total/count)
    