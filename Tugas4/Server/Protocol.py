from ProsesCommand import ProsesCommad
import json
import logging
import codecs

p = ProsesCommad()

class Protocol:
    def proses(self,string_to_process):
        s = string_to_process[0]
        cstring = s.split(" ")

        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                filename = cstring[1].strip()
                string_to_process[0] = cstring[2].strip()
                file_content = string_to_process

                file = "".join(file_content)
                p.upload_file(filename, file_content)

                response = "successfully uploaded"
                content = file
            elif (command=='download'):
                logging.warning("download")
                filename = cstring[1].strip()
                hasil = p.download_file(filename)

                response = "successfully downloaded"
                content = hasil
            elif (command=='list'):
                logging.warning("list")
                directory_name = cstring[1].strip()
                hasil = p.list_file(directory_name)

                response = "successfully listed all files of directory " + directory_name
                content = hasil
            else:
                  response= "ERRCMD"
                  content= "None"
        except:
          response = "ERROR"
          content = "None"
        
        data = dict(response=response,content=content)
        return json.dumps(data)


if __name__=='__main__':
    pass