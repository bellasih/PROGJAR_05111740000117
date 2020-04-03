import sys
import os
import json
import uuid
import logging
from queue import  Queue

class Chat:
	def __init__(self):
		self.sessions={}
		self.users = {}
		self.users['messi']={ 'nama': 'Lionel Messi', 'negara': 'Argentina', 'password': 'surabaya', 'incoming' : {}, 'outgoing': {}}
		self.users['henderson']={ 'nama': 'Jordan Henderson', 'negara': 'Inggris', 'password': 'surabaya', 'incoming': {}, 'outgoing': {}}
		self.users['lineker']={ 'nama': 'Gary Lineker', 'negara': 'Inggris', 'password': 'surabaya','incoming': {}, 'outgoing':{}}

	def proses(self,data):
		j=data.split(" ")
		try:
			command=j[0].strip()
			if (command=='auth'):
				username=j[1].strip()
				password=j[2].strip()
				logging.warning("AUTH: auth {} {}" . format(username,password))
				return self.autentikasi_user(username,password)
			elif (command=='send'):
				sessionid = j[1].strip()
				usernameto = j[2].strip()
				message=""
				for w in j[3:]:
					message="{} {}" . format(message,w)
				usernamefrom = self.sessions[sessionid]['username']
				logging.warning("SEND: session {} send message from {} to {}" . format(sessionid, usernamefrom,usernameto))
				return self.send_message(sessionid,usernamefrom,usernameto,message)
			elif (command=='inbox'):
				sessionid = j[1].strip()
				username = self.sessions[sessionid]['username']
				logging.warning("INBOX: {}" . format(sessionid))
				return self.get_inbox(username)
			elif (command=='logout'):
				tokenid = j[1].strip()
				logging.warning("LOGOUT: process for logout this account")
				return self.get_logout(tokenid)
			elif (command=='get_all_users'):
				tokenid = j[1].strip()
				logging.warning("GET_ALL_USERS: process for listing all users")
				return self.get_all_users(tokenid)
			elif (command=='get_online_users'):
				tokenid = j[1].strip()
				logging.warning("GET_ONLINE_USERS: process for listing online users")
				return self.get_online_users(tokenid)
			else:
				return {'status': 'ERROR', 'message': '**Protocol is not correct'}
		except KeyError:
			return { 'status': 'ERROR', 'message' : 'Information not found'}
		except IndexError:
			return {'status': 'ERROR', 'message': '--Protocol is not correct'}

	def autentikasi_user(self,username,password):
		if (username not in self.users):
			return { 'status': 'ERROR', 'message': 'User not found' }
		if (self.users[username]['password']!= password):
			return { 'status': 'ERROR', 'message': 'Wrong Password' }
		tokenid = str(uuid.uuid4()) 
		self.sessions[tokenid]={ 'username': username, 'userdetail':self.users[username]}
		return { 'status': 'OK', 'tokenid': tokenid }

	def get_user(self,username):
		if (username not in self.users):
			return False
		return self.users[username]

	def get_inbox(self,username):
		s_fr = self.get_user(username)
		incoming = s_fr['incoming']
		msgs={}
		for users in incoming:
			msgs[users]=[]
			while not incoming[users].empty():
				msgs[users].append(s_fr['incoming'][users].get_nowait())
			
		return {'status': 'OK', 'messages': msgs}

	def get_logout(self,tokenid):
		del self.sessions[tokenid]
		return {'status': 'OK', 'message': 'processing for logout'}

	def get_all_users(self,sessionid):
		if (sessionid not in self.sessions):
			return {'status': 'ERROR', 'message': 'Session not found'}
		users = " ".join(self.users.keys())
		return {'status': 'OK', 'message': '{}' .format(users)}		

	def get_online_users(self,sessionid):
		if (sessionid not in self.sessions):
			return {'status': 'ERROR', 'message': 'Session not found'}
		tokens = " ".join(self.sessions.keys())
		tokens_arr = tokens.split(" ")
		users = ""
		for i in tokens_arr:
			users = users + self.sessions[i]['username'] + " "
		return {'status': 'OK', 'message': '{}' .format(users)}	

	def send_message(self,sessionid,username_from,username_dest,message):
		if (sessionid not in self.sessions):
			return {'status': 'ERROR', 'message': 'Session not found'}
		s_fr = self.get_user(username_from)
		s_to = self.get_user(username_dest)
		
		if (s_fr==False or s_to==False):
			return {'status': 'ERROR', 'message': 'User not found'}

		message = { 'msg_from': s_fr['nama'], 'msg_to': s_to['nama'], 'msg': message }
		outqueue_sender = s_fr['outgoing']
		inqueue_receiver = s_to['incoming']
		try:	
			outqueue_sender[username_from].put(message)
		except KeyError:
			outqueue_sender[username_from]=Queue()
			outqueue_sender[username_from].put(message)
		try:
			inqueue_receiver[username_from].put(message)
		except KeyError:
			inqueue_receiver[username_from]=Queue()
			inqueue_receiver[username_from].put(message)
		return {'status': 'OK', 'message': 'Message Sent'}

if __name__=="__main__":
	pass
















