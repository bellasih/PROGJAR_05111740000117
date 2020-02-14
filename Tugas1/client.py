import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 30002)
sock.connect(server_address)

try:
    message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print('sending data ' + message)
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