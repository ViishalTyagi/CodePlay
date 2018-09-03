def count(word, ltr):
    count = 0
    for chr in word:
        if chr == ltr:
            count += 1
    print(ltr, "occurs", count,  "times in", word)

wrd = input("Enter the string\n")
letter = input("Enter the character\n",)

count(wrd,letter)