import sys
import socket
import threading

def PortHandler(port):
    host = 'localhost'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    sock.bind((host,port))
    sock.listen(1)

    while True:
        print('waiting for connection')
        conn, client_addr = sock.accept()
        print('connection from %s' % (client_addr,))
        filename = 'server_data_%s.txt' % (client_addr,)
        file = open(filename,'wb')
        while True:
            data = conn.recv(1024).decode()
            print('received ' + data)
            if data:
                file.write(data)
                print('sending back all data')
                data = '-->' + data
                conn.sendall(data.encode())
            else:
                print('no more data from %s' % (client_addr,))
                break
        file.close()
        conn.close()

def Main():  
    threads = []
    port = [31000, 31001, 31002]

    for p in port:
        t = threading.Thread(target= PortHandler, args=[p])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    Main()