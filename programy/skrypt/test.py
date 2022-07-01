import socket

aaa = socket.gethostbyaddr('10.148.5.2')

print(aaa[0])


#print(socket.gethostbyaddr(socket.gethostname())[0])
