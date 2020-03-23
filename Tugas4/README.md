# TUGAS 4 - PROTOKOL 

## Fitur Protokol

Fitur yang disediakan oleh protokol adalah sebagai berikut :

**1. Fitur Meletakkan File ke Server (Upload)** <br>
     * Fitur ini digunakan untuk mengunggah file yang terletak pada direktori Data_Test ke Server. <br>
     * Format agar fitur protokol dapat berjalan tanpa eror adalah :
       ```
       upload [nama_file] [isi_file]
       ```
     <br>* Berikut adalah potongan kode *script* untuk melakukan fitur *upload* : <br>
     
       if (command=='upload'):
                        logging.warning("upload")
                        filename = cstring[1].strip()
                        string_to_process[0] = cstring[2].strip()
                        file_content = string_to_process

                        file = "".join(file_content)
                        p.upload_file(filename, file_content)

                        response = "successfully uploaded"
                        content = file
      
 **2. Fitur Mengambil File dari Server (Download)** <br>
      * Fitur ini digunakan untuk mengunduh file dari server dan disimpan dalam direktori Client/Data. <br>
      * Format agar fitur protokol dapat berjalan tanpa eror adalah :
      ```
      download [nama_file]
      ```
      <br>* Berikut adalah potongan kode *script* untuk melakukan fitur *download* : <br>
     
      elif (command=='download'):
           logging.warning("download")
           filename = cstring[1].strip()
           hasil = p.download_file(filename)

           response = "successfully downloaded"
           content = hasil
           
**3. Fitur Melakukan List File pada Direktori**<br>
      * Fitur ini digunakan untuk melakukan list nama file dari sebuah direktori <br>
      * Format agar fitur protokol dapat berjalan tanpa eror adalah :
      ```
      list [nama_direktori]
      ```
      <br>* Berikut adalah potongan kode *script* untuk melakukan fitur *download* : <br>
      
      elif (command=='list'):
                logging.warning("list")
                directory_name = cstring[1].strip()
                hasil = p.list_file(directory_name)

                response = "successfully listed all files of directory " + directory_name
                content = hasil
                
                
                
## Respon yang Didapat Client
Respon yang didapat oleh *client* dari *server* berupa **respon : gagal/sukses** dan **content : None/isi_file** dalam format **json**. Berikut adalah format umum untuk *dictionary* untuk respon: <br>
```
{
  "response": "[successfull/error]",
  "content": "[None/[isi_file]"
}
```

**1. Respon untuk Fitur Meletakkan File (Upload)**<br>
Berikut adalah contoh hasil respon yang didapat oleh *client* setelah melakukan fitur *upload* :
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas4/Screenshot/terminal_upload_to_server.png)


**2. Respon untuk Fitur Mengambil File (Download)**<br>
Berikut adalah contoh hasil respon yang didapat oleh *client* setelah melakukan fitur *download* :
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas4/Screenshot/terminal_download_from_server.png)


**3. Respon untuk Fitur Melakukan List File Direktori (List)**<br>
Berikut adalah contoh hasil respon yang didapat oleh *client* setelah melakukan fitur *list* :
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas4/Screenshot/terminal_list_directory.png)

      
      
