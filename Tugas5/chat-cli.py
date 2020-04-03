import socket
import os
import json
import getpass

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889

class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP,TARGET_PORT)
        self.sock.connect(self.server_address)
        self.tokenid=""

    def proses(self,cmdline):
        j=cmdline.split(" ")
        try:
            command=j[0].strip()
            if (command=='auth'):
                username = input('Username : ')
                password = getpass.getpass()
                return self.login(username,password)
            elif (command=='send'):
                usernameto = j[1].strip()
                message=""
                for w in j[2:]:
                   message="{} {}" . format(message,w)
                return self.sendmessage(usernameto,message)
            elif (command=='inbox'):
                return self.inbox()
            elif (command=='logout'):
                return self.logout()
            elif (command=='get_all_users'):
                return self.get_all_users()
            elif (command=='get_online_users'):
                return self.get_online_users()
            else:
                return "*Sorry, the command is not correct"
        except IndexError:
                return "-Sorry, the command is not correct"

    def sendstring(self,string):
        try:
            self.sock.sendall(string.encode())
            receivemsg = ""
            while True:
                data = self.sock.recv(64)
                print("receive from server",data)
                if (data):
                    receivemsg = "{}{}" . format(receivemsg,data.decode())  
                    if receivemsg[-4:]=='\r\n\r\n':
                        print("end of string")
                        return json.loads(receivemsg)
        except:
            self.sock.close()
            return { 'status' : 'ERROR', 'message' : 'Failed'}

    def login(self,username,password):
        string="auth {} {} \r\n" . format(username,password)
        result = self.sendstring(string)
        if result['status']=='OK':
            self.tokenid=result['tokenid']
            return "username {} logged in, token {} \n" .format(username,self.tokenid)
        else:
            return "Error, {} \n" . format(result['message'])

    def logout(self):
        string = "logout {} \r\n" .format(self.tokenid)
        result = self.sendstring(string)
        if result['status']=='OK':
            msg="logout {} successfully \n" .format(self.tokenid)
            self.tokenid = ""
        else:
            msg="failed for logout, please try again \n"
        
        return msg

    def sendmessage(self,usernameto="xxx",message="xxx"):
        if (self.tokenid==""):
            return "Error, not authorized"
        string="send {} {} {} \r\n" . format(self.tokenid,usernameto,message)
        print(string)
        result = self.sendstring(string)
        if result['status']=='OK':
            return "message sent to {} \n" . format(usernameto)
        else:
            return "Error, {}" . format(result['message'])

    def inbox(self):
        if (self.tokenid==""):
            return "Error, not authorized"
        string="inbox {} \r\n" . format(self.tokenid)
        result = self.sendstring(string)
        if result['status']=='OK':
            return "{} \n" . format(json.dumps(result['messages']))
        else:
            return "Error, {} \n" . format(result['message'])

    def get_all_users(self):
        if (self.tokenid==""):
            return "Error, not authorized"
        string = "get_all_users {} \r\n" .format(self.tokenid)
        result = self.sendstring(string)
        if result['status']=='OK':
            return "all users : {} \n" . format(json.dumps(result['message']))
        else:
            return "Error, {}" . format(result['message'])
    
    def get_online_users(self):
        if (self.tokenid==""):
            return "Error, not authorized"
        string = "get_online_users {} \r\n" .format(self.tokenid)
        result = self.sendstring(string)
        if result['status']=='OK':
            return "online users : {} \n" . format(json.dumps(result['message']))
        else:
            return "Error, {}" . format(result['message'])

if __name__=="__main__":
    cc = ChatClient()
    print("Instruction :\n1. Command authentication : auth\n2.Command send message : send [username receiver] [content of message]\n" +
          "3. Command Logout: logout\n4.Command list all users : get_all_users\n5.Command list online users : get_online_users\n")
    while True:
        cmdline = input("Command {}:" . format(cc.tokenid))
        print(cc.proses(cmdline))
