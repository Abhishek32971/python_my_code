from socket import *

soc = socket(AF_INET,SOCK_STREAM)
soc.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
soc.send(cmd)

while True:
   data = soc.recv(512)
   if(len(data)<1):
      break
   print(data.decode())
soc.close()