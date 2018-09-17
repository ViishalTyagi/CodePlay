import socket

inp = input("Enter URL -\t")
host = inp.split('/')
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ms.connect((host[2],80))
except:
    print("Invalid URL")
    quit()

gt_url = 'GET' " " +inp+ " " 'HTTP/1.0\r\n\r\n'
cmd = gt_url.encode()
ms.send(cmd)
count = 0
while True:
    data = ms.recv(512)
    count += len(data)
    if len(data) < 1:
        break
    elif count < 3001:
        print(data.decode(), end =" ")
    
ms.close()


print("Number of Characters:\t",count)
