from socket import *

port = 60000

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('localhost', port))

print('접속 완료')

#recvData = clientSock.recv(1024)

#if recvData.decode('utf-8') == '1'

while True:
        sendData = input(">>>")
        clientSock.send(sendData.encode('utf-8'))

        recvData = clientSock.recv(1024)
        print('상대방: ', recvData.decode('utf-8'))
'''
else:
    while True:
        recvData = clientSock.recv(1024)
        print('상대방: ', recvData.decode('utf-8'))

        sendData = input(">>>")
        clientSock.send(sendData.encode('utf-8'))
        '''
