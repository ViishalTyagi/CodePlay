#String Manipulations

word = ' Hello You  '
print('Given String is:', word)
ab = word[2:4]
print(ab)

if 'el' in word:
    print("Found el")
else:
    print("Not found!")

rep = word.replace('ll','LL')
print(rep)

print(word.lstrip())
print(word.rstrip())
print(word.strip())
