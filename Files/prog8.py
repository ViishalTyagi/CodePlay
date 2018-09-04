#Files

inp = input('Enter a File name:')
try:
    fhand = open(inp)
except:
    print('File does not exist:', inp)
    quit()

for lx in fhand:
    ly = lx.rstrip()
    print(ly)
print('End of File')

inp1 = input('Out of for-loop, check another method:')
if inp1 == 'yes':
    fhand = open(inp)
    frd = fhand.read()
    i = frd[ : 500]
    i = i.upper()
    print(i)
    print('End of File.')
else:
    quit()



