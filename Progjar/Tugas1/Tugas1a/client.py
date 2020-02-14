import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 30002)
sock.connect(server_address)

try:
    msg = open('/home/bella/Progjar/Tugas1/test.txt','rb')

    message = msg.read(1024)
    sock.sendall(message.encode())

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(1024).decode()
        amount_received += len(data)
        print('received data')

finally:
    print('closing socket')
    sock.close()