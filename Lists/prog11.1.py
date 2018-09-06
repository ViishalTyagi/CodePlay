def chop(lst):
    del lst[(len(lst)-1)]
    del lst[0]

def middle(t):
    ln = len(t) - 1
    t = t[1:ln] 
    return print(t)

num = [1,3,8,10]
num1 = [7,77,777,7777]
chop(num)
print (num)
middle(num1)

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    words = line.split()
# print ('Debug:', words)
    if len(words) == 0 or words[0] != 'From': 
        continue
    print(words[2])