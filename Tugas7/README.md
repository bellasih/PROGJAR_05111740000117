# TUGAS 7 - PERFORMANCE TEST 

## Berikut adalah hasil keluaran dari performance test untuk server pada tugas 6 

| No. Test | Concurrency Level | Time Taken for Test | Complete request | Failed request | Total Transferred | Request per Second | Time per Request | Transfer Rate |
| :------: | :---------------: | :-----------------: | :--------------: | :------------: | :---------------: | :----------------: | :--------------: | :-----------: |
| 1 | 1 | 1 | 0.030 seconds | 10  | 0 | 4470 bytes  | 337.34 [#/sec] | 2.964 [ms] | 147.26 [Kbytes/sec] |
| 2 | 1 | 1 | 0.079 seconds | 50  | 0 | 22350 bytes | 631.58 [#/sec] | 1.583 [ms] | 275.70 [Kbytes/sec] |
| 3 | 1 | 1 | 0.166 seconds | 100 | 0 | 44700 bytes | 603.61 [#/sec] | 1.657 [ms] | 263.49 [Kbytes/sec] |

## Berikut adalah hasil keluaran terminal 
1. ab -n 10 -c 1,5,10 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req 10.JPG)

2. ab -n 50 -c 1,10,30,50 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req 50.JPG)

3. ab -n 100 -c 1,30,50,100 http://127.0.0.1:10001
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas7/screenshot/req 100.JPG)
