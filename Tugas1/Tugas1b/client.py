import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 30001)
sock.connect(server_address)

try:
    message = '/home/bella/PROGJAR_05111740000117/Tugas1/test.txt'
    print('sending filename : ' + message)
    sock.sendall(message.encode())
    
    filename = 'client_conn_%s.txt' % (server_address,)
    file = open(filename,'wb')

    while True:
        data = sock.recv(1024).decode()
        print('received ' + data)
        if data:
            file.write(data)
        else:
            print('no more data from %s' % (server_address,))
            file.close()
            break

finally:
    print('closing socket')
    sock.close()