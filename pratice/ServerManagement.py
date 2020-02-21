from socket import *


class ServerManagement(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run():
        while True:
            try:
                server_massage = input("Input command: ")
                if server_massage == 'stop':
                    return 0
                elif server_massage == "userlist":
                    check_user_list()
            except:
                pass
            
    def check_user_list(self):
        for client in message_user_list:
            print(client.getpeername())