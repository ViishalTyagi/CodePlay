#dictionaries

dt = dict()
mdt = dict()
lst = list()
mlst = list()

inp = input('Enter the file name:')
try:
    fhand = open(inp)
except:
    print('File does not exist:', inp)
    quit()

for line in fhand:
    if line.startswith("From") and not line.startswith("From:"):
        gt = line.split()
        lst.append(gt[2])
        mlst.append(gt[1])

for day in lst:
        dt[day] = dt.get(day,0) + 1

print(dt)

for mail in mlst:
    mdt[mail] = mdt.get(mail,0) + 1
print()
print(mdt)

name = None
count = None
for mail,num in mdt.items():
    if count is None or count < num:
        count = num
        name = mail

print(name,':', count)

ilt = list()
nlst = list()
dct = dict()
"""
for i,j in mdt.items():
    ilt = i.split('@')
    while j != 0:
        nlst.append(ilt[1])
        j -= 1
"""
for k in mlst:
    ilt = k.split('@')
    nlst.append(ilt[1])
    
for domain in nlst:
    dct[domain] = dct.get(domain,0) + 1

print(dct)

