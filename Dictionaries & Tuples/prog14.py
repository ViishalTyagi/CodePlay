inp = input('Enter the file name:')
try:
    fhand = open(inp)
except:
    print('File does not exist:', inp)
    quit()

lst = list()
dt = dict()
tmp =list()

for i in fhand:
    if i.startswith('From') and not i.startswith('From:'):
        gt = i.split()
        lst.append(gt[1])

for day in lst:
    dt[day] = dt.get(day,0) + 1

name = None
count = None
tups = dt.items()
for mail,num in tups:
    tmp.append( (num,mail) )
tmp = sorted(tmp, reverse = True)

for i,j in tmp[0]:
    print(j,':',i)
