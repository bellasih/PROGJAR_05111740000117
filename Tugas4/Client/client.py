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
        os.chdir('../')
        path = os.getcwd() + '/Data_Test/'

        print('Input filename in directory Data_Test')
        filename =  input()

        file = path + filename
        with open(file, 'rb') as fdata:
            contents = fdata.read()
            contents_base64 = codecs.encode(contents,'base64')
        fdata.close()

        file_content = contents_base64.decode('utf-8')
        data = 'upload ' + filename + ' ' + file_content
        sock.sendall(data.encode())

        response = ''
        while True:
            data = sock.recv(1024)
            response = response + data.decode()
            if len(data) < 1024:
                break
        print(response)
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    kirim_data()
