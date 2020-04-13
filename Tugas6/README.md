# TUGAS 5 - HTTP Protocol (Web Server)

## Deskripsi Tugas

Buatlah <br>
1. Sebuah multihtread server, buka pada port 10001 di ip address 127.0.0.1
2. Dapat melayani request dalam bentuk string seperti ini 
   ```
   GET spasi / spasi HTTP/1.0
   ```
3. Tanda berakhir request adalah "\r\n\r\n"
4. Jika tanda akhir request diterima, maka balaslah dengan string 
   ```
   "<h1>SERVER HTTP</h1>"
   ```
5. Cobalah dengan telnet port 10001 dengan cara mengirimkan string 
   ```
   GET(spasi)/(spasi)HTTP/1.0(enter)(enter).
   ```
   <br>Hasil yang didapat adalah sebagai berikut :<br>
   * Untuk telnet<br>
   ![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas6/screenshot/telnet.JPG)
   
   * Untuk server thread
   ![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas6/screenshot/server_thread.JPG)

6. Bukalah chrome web browser, aktifkan developer mode, bagian network
7. Bukalah alamat http://127.0.0.1:10001
8. Berikut adalah hasil screenshotnya :
   ![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas6/screenshot/web-html.JPG)

