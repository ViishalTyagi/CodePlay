import urllib.request

inp = input("Enter the Url:\t")
try:
    fhand = urllib.request.urlopen(inp)
except:
    print("Invalid Url")
    quit()

count = 0
for line in fhand:
    line = line.decode().strip()
    count += len(line)
    if count < 3001:
        print(line)

print(count)