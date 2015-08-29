****************************************************************************
* README file for 142 * 4500 * 64 time-aware Web service QoS dataset
* Last updated: 2015/08/29
****************************************************************************

This dataset describes real-world QoS evaluation results from 142 users on 
4,500 Web services over 64 different time slices (at 15-minute interval). 
The dataset is available for downloading at: 
http://wsdream.github.io/dataset/wsrec_dataset2

****************************************************************************
List of contents of the dataset
****************************************************************************

rtdata.txt  - response-time values of 4,500 Web services when invoked by 142 
              service users over 64 time slices. Data format:
              User ID | Service ID | Time Slice ID | Response Time (sec)
              e.g.: 98    4352    33    0.311
tpdata.txt  - throughput values of 4,500 Web services when invoked by 142 
              service users in 64 time slices. Data format:
              User ID | Service ID | Time Slice ID | Throughput (kbps)
              e.g.: 91    1196    62    32.88
readme.txt  - descriptions of the dataset

****************************************************************************
Reference paper
****************************************************************************

Please refer to the following paper for the detailed descriptions of this 
dataset:

- Yilei Zhang, Zibin Zheng, and Michael R. Lyu, "WSPred: A Time-Aware 
  Personalized QoS Prediction Framework for Web Services", in Proceedings of 
  the 22th IEEE Symposium on Software Reliability Engineering (ISSRE 2011).

IF YOU USE THIS DATASET IN PUBLISHED RESEARCH, PLEASE CITE THE ABOVE PAPER. 
THANKS!

****************************************************************************
License
****************************************************************************

The MIT License (MIT)

Copyright (c) 2015, WS-DREAM, CUHK (https://wsdream.github.io)

