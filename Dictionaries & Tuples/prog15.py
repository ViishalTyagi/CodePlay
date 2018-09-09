inp = input('Enter the file name:')
try:
    fhand = open(inp)
except:
    print('File does not exist:', inp)
    quit()

lst = list()
time = list()
tlist = list()
dt = dict()
for i in fhand:
    if i.startswith('From') and not i.startswith('From:'):
        gt = i.split()
        lst.append(gt[5])

for j in lst:
    st = j.split(':')
    time.append(st[0])

for hour in time:
    dt[hour] = dt.get(hour,0) + 1

tlist = list(dt.items())
#for hour,count in dt.items():
 #   tlist.append( (hour,count) )

#tlist = sorted(tlist)
tlist.sort()
for i,j in tlist:
    print(i, ':', j)