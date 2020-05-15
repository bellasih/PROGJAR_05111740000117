# TUGAS 10

## Tampilan http://localhost:44444/page.html
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas10/Screenshot/localhost_p44444.PNG)

## Tampilan LOG loadbalancer
![alt text](https://github.com/bellasih/PROGJAR_05111740000117/blob/master/Tugas10/Screenshot/loadbalancer.PNG)

## Berikut adalah hasil keluaran dari performance test untuk server pada tugas 10 
1. Performance Test Asynchronus Server

| No. Test | Concurrency Level | Time Taken for Test | Complete request | Failed request | Total Transferred | Request per Second | Time per Request | Time per Request (all concurrent) | Transfer Rate |
| :------: | :---------------: | :-----------------: | :--------------: | :------------: | :---------------: | :----------------: | :--------------: | :-------------------------------: | :-----------: |
| 1  | 1   | 3.184 seconds | 1000  | 0 | 122000 bytes  | 314.07 [#/sec]  | 3.184 [ms]    | 3.184 [ms] | 37.42 [Kbytes/sec] |
| 2  | 5   | 2.038 seconds | 1000  | 0 | 122000 bytes  | 490.58 [#/sec]  | 10.192 [ms]   | 2.038 [ms] | 58.45 [Kbytes/sec] |
| 3  | 10  | 2.295 seconds | 1000  | 0 | 122000 bytes  | 435.70 [#/sec]  | 22.952 [ms]   | 2.295 [ms] | 51.91 [Kbytes/sec] |
| 4  | 30  | 3.552 seconds | 1000  | 0 | 122000 bytes  | 281.54 [#/sec]  | 106.558 [ms]  | 3.552 [ms] | 33.54 [Kbytes/sec] |
| 5  | 50  | 2.222 seconds | 1000  | 0 | 122000 bytes  | 450.07 [#/sec]  | 111.095 [ms]  | 2.222 [ms] | 53.62 [Kbytes/sec] |
| 6  | 100 | 6.143 seconds | 1000  | 0 | 122000 bytes  | 162.78 [#/sec]  | 614.321 [ms]  | 6.143 [ms] | 19.39 [Kbytes/sec] |

2. Performance Test Threaded Server

| No. Test | Concurrency Level | Time Taken for Test | Complete request | Failed request | Total Transferred | Request per Second | Time per Request | Time per Request (all concurrent) | Transfer Rate |
| :------: | :---------------: | :-----------------: | :--------------: | :------------: | :---------------: | :----------------: | :--------------: | :-------------------------------: | :-----------: |
| 1  | 1   | 3.360 seconds | 1000  | 0 | 122000 bytes  | 297.60 [#/sec]  | 3.360 [ms]   | 3.360 [ms] | 35.46 [Kbytes/sec] |
| 2  | 5   | 2.242 seconds | 1000  | 0 | 122000 bytes  | 445.96 [#/sec]  | 11.212 [ms]  | 2.242 [ms] | 53.13 [Kbytes/sec] |
| 3  | 10  | 2.757 seconds | 1000  | 0 | 122000 bytes  | 362.71 [#/sec]  | 27.571 [ms]  | 2.757 [ms] | 43.21 [Kbytes/sec] |
| 4  | 30  | 2.387 seconds | 1000  | 0 | 122000 bytes  | 418.90 [#/sec]  | 71.617 [ms]  | 2.387 [ms] | 49.41 [Kbytes/sec] |
| 5  | 50  | 2.911 seconds | 1000  | 0 | 122000 bytes  | 343.54 [#/sec]  | 145.543 [ms] | 2.911 [ms] | 40.93 [Kbytes/sec] |
| 6  | 100 | 2.773 seconds | 1000  | 0 | 122000 bytes  | 360.56 [#/sec]  | 277.349 [ms] | 2.773 [ms] | 42.96 [Kbytes/sec] |