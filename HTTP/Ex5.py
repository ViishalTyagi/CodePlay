import socket

inp = input("Enter Url:\t")
url = inp.split('/')[2]
ms = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    ms.connect((url,80))
except:
    print("Invalid Url")
    quit()

gt = 'GET' " "+inp+ " "'HTTP/1.0\r\n\r\n'
cmd = gt.encode()
ms.send(cmd)
    
lst = list()
while True:
    data = ms.recv(512)
    if len(data) < 1:
        break
    lst.append(data.decode())

ms.close()

st = str()
j= 0 
while j < len(lst):
    st += lst[j]  
    j += 1  

fnd = st.find('\r\n\r\n')

print (st[fnd+1:])