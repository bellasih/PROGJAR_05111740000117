import sys
import socket
import logging
import codecs
import os

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('0.0.0.0', 1689)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        print('Input directory name for listing all files')
        directory_name =  input()
        data = 'list ' + directory_name
        sock.sendall(data.encode())

        response = ''
        while True:
            datas = sock.recv(1024)
            response = response + datas.decode()
            if len(datas) < 1024:
                break
        print(response)

    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    kirim_data()
