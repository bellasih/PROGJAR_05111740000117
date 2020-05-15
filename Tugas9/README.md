# TUGAS 9 

## Berikut adalah hasil keluaran dari performance test untuk server pada tugas 9 
1. Performance Test Asynchronus Server

| No. Test | Concurrency Level | Time Taken for Test | Complete request | Failed request | Total Transferred | Request per Second | Time per Request | Time per Request (all concurrent) | Transfer Rate |
| :------: | :---------------: | :-----------------: | :--------------: | :------------: | :---------------: | :----------------: | :--------------: | :-------------------------------: | :-----------: |
| 1  | 1   | 2.093 seconds | 1000  | 0 | 122000 bytes  | 477.80 [#/sec]  | 2.093 [ms]  | 2.093 [ms] | 59.92 [Kbytes/sec] |
| 2  | 5   | 1.895 seconds | 1000  | 0 | 122000 bytes  | 527.71 [#/sec]  | 9.475 [ms]  | 1.895 [ms] | 62.87 [Kbytes/sec] |
| 3  | 10  | 2.184 seconds | 1000  | 0 | 122000 bytes  | 457.82 [#/sec]  | 21.843 [ms] | 2.184 [ms] | 54.54 [Kbytes/sec] |
| 4  | 30  | 1.887 seconds | 1000  | 0 | 122000 bytes  | 529.97 [#/sec]  | 56.607 [ms] | 1.887 [ms] | 63.14 [Kbytes/sec] |
| 5  | 50  | 1.830 seconds | 1000  | 0 | 122000 bytes  | 546.33 [#/sec]  | 91.519 [ms] | 1.830 [ms] | 65.09 [Kbytes/sec] |
| 6  | 100 | 1.833 seconds | 1000  | 0 | 122000 bytes  | 543.43 [#/sec]  | 183.341 [ms]| 1.833 [ms] | 64.98 [Kbytes/sec] |

2. Performance Test Threaded Server

| No. Test | Concurrency Level | Time Taken for Test | Complete request | Failed request | Total Transferred | Request per Second | Time per Request | Time per Request (all concurrent) | Transfer Rate |
| :------: | :---------------: | :-----------------: | :--------------: | :------------: | :---------------: | :----------------: | :--------------: | :-------------------------------: | :-----------: |
| 1  | 1   | 13.292 seconds| 1000  | 0 | 122000 bytes | 75.23 [#/sec]  | 13.292 [ms]  | 13.292 [ms] | 8.96 [Kbytes/sec] |
| 2  | 5   | 4.602 seconds | 1000  | 0 | 122000 bytes | 217.29 [#/sec] | 23.010 [ms]  | 4.602 [ms] | 25.89 [Kbytes/sec] |
| 3  | 10  | 5.044 seconds | 1000  | 0 | 122000 bytes | 198.25 [#/sec] | 50.441 [ms]  | 5.044 [ms] | 23.62 [Kbytes/sec] |
| 4  | 30  | 6.559 seconds | 1000  | 0 | 122000 bytes | 152.47 [#/sec] | 196.765 [ms] | 6.559 [ms] | 18.16 [Kbytes/sec] |
| 5  | 50  | 4.942 seconds | 1000  | 0 | 122000 bytes | 202.33 [#/sec] | 247.120 [ms] | 4.942 [ms] | 24.11 [Kbytes/sec] |
| 6  | 100 | 4.609 seconds | 1000  | 0 | 122000 bytes | 216.95 [#/sec] | 460.931 [ms] | 4.609 [ms] | 25.85 [Kbytes/sec] |

## Berikut adalah hasil keluaran terminal 
1. ab -n 1000 -c 1 http://127.0.0.1:45000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Async/r1000_c1.PNG)

2. ab -n 1000 -c 5 http://127.0.0.1:45000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Async/r1000_c5.PNG)

3. ab -n 1000 -c 10 http://127.0.0.1:45000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Async/r1000_c10.PNG)

4. ab -n 1000 -c 30 http://127.0.0.1:45000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Async/r1000_c30.PNG)

5. ab -n 1000 -c 50 http://127.0.0.1:45000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Async/r1000_c50.PNG)

6. ab -n 1000 -c 100 http://127.0.0.1:45000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Async/r1000_c100.PNG)

7. ab -n 1000 -c 1 http://127.0.0.1:46000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Thread/r1000_c1.PNG)

8. ab -n 1000 -c 5 http://127.0.0.1:46000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Thread/r1000_c5.PNG)

9. ab -n 1000 -c 10 http://127.0.0.1:46000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Thread/r1000_c10.PNG)

10. ab -n 1000 -c 30 http://127.0.0.1:46000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Thread/r1000_c30.PNG)

11. ab -n 1000 -c 50 http://127.0.0.1:46000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Thread/r1000_c50.PNG)

12. ab -n 1000 -c 100 http://127.0.0.1:46000/
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas9/Screenshot/Thread/r1000_c100.PNG)
