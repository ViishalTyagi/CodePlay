#Lists

fget = open('romeo.txt')
fhand = fget.read()
get = fhand.split()
print(get)
get.sort()
print(get)

name = list()
count = 0
inp = input('Enter the file name:')
try:
    fh = open(inp)
except:
    print('File does not exist:',inp)
    quit()

for i in fh:
    if i.startswith('From'):
        name.append(i)
    else:
        continue
count = len(name)
print('There were', count, 'lines in the',inp,'file with From as the first word')

nl = list()
while True:
    num = input('Enter a Number:')
    if num == 'done':
        break
    else:
        val = int(num)
        nl.append(val)
print(nl)
print('Maximum:', max(nl))
print('Minimum', min(nl))