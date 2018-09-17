import socket

inp = input('Enter URL -\t')

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
host = inp.split('/')

try:
    ms.connect((host[2], 80))
except:
    print("Invalid URL, Try Again!")
    quit()

gt_url = 'GET' " " +inp+ " " 'HTTP/1.0\r\n\r\n'
cmd = gt_url.encode()
ms.send(cmd)

while True:
    data = ms.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end  =" ")

ms.close()