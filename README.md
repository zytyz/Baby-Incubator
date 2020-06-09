# Baby-Incubator
## Introduction
A prototype of a non-contact baby incubator which measures heart rate and body temperature remotely. The temperature is controlled at a certain value, while all the data is shown on an app monitor.
* **Heart rate** is measured through remote PPG.
* **Body temperature** is estimated with heart rate.

## How to run
```
bash run.sh <subject_name> <webcam url> <http ip> <conda env name> <initial temperature>
```
* Webcam url: the ip address of an Android Phone used as an IP Webcam
* Http IP: the ip address of the computer running this program
* Initial temperature: the initial temperature of the subject

For example,
```
bash run.sh zyt http://192.168.0.108:8080/video 192.168.0.102 py37 36.0
```
