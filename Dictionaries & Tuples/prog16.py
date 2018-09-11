import string

count = 0
dt =dict()
lt = list()

inp = input('Enter the file name:')
try:
    fh = open(inp)
except:
    print('File does not exist:', inp)
    quit()

for line in fh:
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    gt = line.split()
    for word in gt:
        for letter in word:
            count += 1
            dt[letter] = dt.get(letter,0) + 1

for i,j in dt.items():
    lt.append((j/count,i))

lt = sorted(lt, reverse=True)

for fr,ltr in lt:
    print(fr,ltr)