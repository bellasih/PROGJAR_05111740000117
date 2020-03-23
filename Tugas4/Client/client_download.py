import sys
import socket
import logging
import codecs
import os
import json

path_client = '/home/bella/PROGJAR_05111740000117/Tugas4/Client/Data/'

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('0.0.0.0', 1689)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        print('Input filename in directory Server/Data')
        filename =  input()
        data = 'download ' + filename
        sock.sendall(data.encode())

        buffer_arr = []
        response = ''
        while True:
            recv_content = sock.recv(1024)
            content = recv_content.decode()
            response = response + content
            if len(content) < 1024:
                break
        print(response)

        arr = json.loads(response)
        contents = arr['content']
        coba = contents.encode('utf-8')
        path_receive = path_client + filename 

        with open(path_receive, 'wb+') as datas:
            datas.write(codecs.decode(coba,'base64'))
        datas.close()

    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    kirim_data()
