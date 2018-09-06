#just a funny program
inp = input('Enter a file name:')
if inp == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk''d!')
else:
    try:
        fhand = open(inp)
    except:
        print('File does not exist:',inp)
        quit()
    count = 0
    for i in fhand:
        if not i.startswith('Subject'):
            continue
        else:
            count += 1
    print("There were", count, "subject lines in", inp)
