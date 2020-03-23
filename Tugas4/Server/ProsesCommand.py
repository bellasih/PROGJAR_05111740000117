import shelve
import uuid
import codecs
import os

path_server = '/home/bella/PROGJAR_05111740000117/Tugas4/Server/Data/'

class ProsesCommad:
    def __init__(self):
        self.data = shelve.open('mydata.dat')

    def upload_file(self,filename=None,file_content=None):
        if (filename is None or file_content is None):
            return False
        path_receive = path_server + filename 
        print(path_receive)
        contents = ''.join(file_content)
        coba = contents.encode('utf-8')
        with open(path_receive, 'wb+') as datas:
            datas.write(codecs.decode(coba,'base64'))
        datas.close()
        return True

    def download_file(self,filename=None):
        if (filename is None):
            return False
        path = path_server + filename
        with open(path, 'rb') as fdata:
            contents = fdata.read()
            contents_base64 = codecs.encode(contents,'base64')
        fdata.close()

        file_content = contents_base64.decode('utf-8')
        print(file_content)
        return file_content

    def list_file(self,directory_name):
        if (directory_name is None):
            return False

        arr_files = os.listdir(directory_name)
        data = str(arr_files)
        return data

if __name__=='__main__':
    pass
