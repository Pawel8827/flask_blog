import getpass, socket
import platform
ip = '10.148.5.2'

bcc = socket.gethostbyaddr(ip)
print(bcc[0])
print(bcc[2])
abc = socket.gethostbyname(str(bcc[0]))
print(abc)


