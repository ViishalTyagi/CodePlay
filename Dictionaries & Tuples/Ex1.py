fhand = open('romeo.txt')
wrd = fhand.read()
lst = wrd.split()
d = dict()
for i in lst:
    d[i] = ''

inp = input("Enter the String\n")
if inp in d:
    print('True')    
else:
    print("Word does not exist in the text")        

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])