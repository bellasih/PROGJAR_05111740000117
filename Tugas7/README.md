# TUGAS 7 - PERFORMANCE TEST 

## Berikut adalah hasil keluaran dari performance test untuk server pada tugas 6 

| No. Test | Concurrency Level | Time Taken for Test | Complete request | Failed request | Total Transferred | Request per Second | Time per Request | Time per Request (all concurrent) | Transfer Rate |
| :------: | :---------------: | :-----------------: | :--------------: | :------------: | :---------------: | :----------------: | :--------------: | :-------------------------------: | :-----------: |
| 1  | 1   | 0.030 seconds | 10  | 0 | 4470 bytes  | 337.34 [#/sec]  | 2.964 [ms]  | 2.964 [ms] | 147.26 [Kbytes/sec] |
| 2  | 5   | 0.016 seconds | 10  | 0 | 4470 bytes  | 643.83 [#/sec]  | 7.766 [ms]  | 1.553 [ms] | 281.05 [Kbytes/sec] |
| 3  | 10  | 0.013 seconds | 10  | 0 | 4470 bytes  | 775.31 [#/sec]  | 12.898 [ms] | 1.290 [ms] | 338.44 [Kbytes/sec] |
| 4  | 1   | 0.079 seconds | 50  | 0 | 22350 bytes | 631.58 [#/sec]  | 1.583 [ms]  | 1.583 [ms] | 275.70 [Kbytes/sec] |
| 5  | 10  | 0.078 seconds | 50  | 0 | 22350 bytes | 644.42 [#/sec]  | 15.518 [ms] | 1.552 [ms] | 281.30 [Kbytes/sec] |
| 6  | 30  | 0.044 seconds | 50  | 0 | 22350 bytes | 1138.20 [#/sec] | 26.357 [ms] | 0.879 [ms] | 496.85 [Kbytes/sec] |
| 7  | 50  | 0.041 seconds | 50  | 0 | 22350 bytes | 1224.41 [#/sec] | 40.836 [ms] | 0.817 [ms] | 275.70 [Kbytes/sec] |
| 8  | 1   | 0.166 seconds | 100 | 0 | 44700 bytes | 603.61 [#/sec]  | 1.657 [ms]  | 1.657 [ms] | 263.49 [Kbytes/sec] |
| 9  | 10  | 0.136 seconds | 100 | 0 | 44700 bytes | 735.79 [#/sec]  | 13.591 [ms] | 1.359 [ms] | 321.19 [Kbytes/sec] |
| 10 | 50  | 0.095 seconds | 100 | 0 | 44700 bytes | 1054.35 [#/sec] | 47.422 [ms] | 0.948 [ms] | 460.25 [Kbytes/sec] |
| 11 | 100 | 0.067 seconds | 100 | 0 | 44700 bytes | 1491.14 [#/sec] | 67.063 [ms] | 0.671 [ms] | 650.92 [Kbytes/sec] |

## Berikut adalah hasil keluaran terminal 
1. ab -n 10 -c 1,5,10 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%2010.JPG)

2. ab -n 10 -c 5 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%2010_c%205.JPG)

3. ab -n 10 -c 10 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%2010_c%2010.JPG)

4. ab -n 50 -c 1,10,30,50 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%2050.JPG)

5. ab -n 50 -c 10 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%2050_c%2010.JPG)

6. ab -n 50 -c 30 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%2050_c%2030.JPG)

7. ab -n 50 -c 50 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%2050_c%2050.JPG)

8. ab -n 100 -c 1,30,50,100 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%20100.JPG)

9. ab -n 100 -c 10 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%20100_c%2010.JPG)

10. ab -n 100 -c 50 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%20100_c%2050.JPG)

11. ab -n 100 -c 100 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req%20100_c%20100.JPG)
