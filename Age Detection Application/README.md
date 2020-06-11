# Deep Learning with Tensorflow
TensorFlow library is a library by Google that focuses on deep learning and machine learning as open source as of November 9, 2015, and provides a development framework for researchers by making numerical calculations using data flow charts.

## TensorFlow Object Detection API
Object detection training was carried out using the TensorFlow Object Detection API for the age detection application added to the announcement screen designed within the scope of the project. The TensorFlow Object Detection API is an open-source framework built on TensorFlow that aims to facilitate the creation, training and deployment of object detection models. [17] API provides training with many pre-trained models.

### Installation
* [Install](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)

# Preperation of Training
* Download [models](https://github.com/tensorflow/models)
* Clone this repo.
* 


## Model Training with SSD Mobilenet COCO
A deep learning training from scratch takes time and big data to perform. These problems can be solved by training on pre-trained models. Due to the higher accuracy rate, the use of the Single Shot Detector (SSD) algorithm was preferred in the project. SSD is capable of detecting multiple objects in single shot.
In this training, SSD Mobilenet COCO (ssd_mobilenet_v1_coco) model, which is compatible with all kinds of devices, is small in size and has high object recognition speed, containing 90 different objects, is used. SSD_mobilenet_v1_coco has 21 mean Average Precision (mAP) values reported on COCO datasets [15]. The model has been configured based on the supported configuration file, ssd_mobilenet_coco.config.
