from socket import *

port1 = 60000
port2 = 65000

clientSock1 = socket(AF_INET, SOCK_STREAM)
clientSock1.connect(('localhost', port1))

recvData = clientSock1.recv(1024).decode('utf-8')
print("[Client] Received " + str(recvData))

clientSock1.send("300".encode("utf-8"))
print("[Client] Sent " + str(300))

clientSock2 = socket(AF_INET, SOCK_STREAM)
clientSock2.connect(('localhost', port2))

print('접속 완료')
