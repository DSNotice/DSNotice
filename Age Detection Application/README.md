# Description
In the study, younger than 40 years old was labeled as "young", and older than 40 years old was labeled as "old" and binary classification training was carried out with Tensorflow Object Detection API.

# Deep Learning with Tensorflow
TensorFlow library is a library by Google that focuses on deep learning and machine learning as open source as of November 9, 2015, and provides a development framework for researchers by making numerical calculations using data flow charts.

## TensorFlow Object Detection API
Object detection training was carried out using the TensorFlow Object Detection API for the age detection application added to the announcement screen designed within the scope of the project. The TensorFlow Object Detection API is an open-source framework built on TensorFlow that aims to facilitate the creation, training and deployment of object detection models. [17] API provides training with many pre-trained models.

## Model Training with SSD Mobilenet COCO
A deep learning training from scratch takes time and big data to perform. These problems can be solved by training on pre-trained models. Due to the higher accuracy rate, the use of the Single Shot Detector (SSD) algorithm was preferred in the project. SSD is capable of detecting multiple objects in single shot.
In this training, SSD Mobilenet COCO (ssd_mobilenet_v1_coco) model, which is compatible with all kinds of devices, is small in size and has high object recognition speed, containing 90 different objects, is used. SSD_mobilenet_v1_coco has 21 mean Average Precision (mAP) values reported on COCO datasets [15]. The model has been configured based on the supported configuration file, ssd_mobilenet_coco.config.

### Installation
* [Install](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)

# Preperation of Training
* Download [models](https://github.com/tensorflow/models)<br>

Save followings in models/research/object_detection/legacy<br/>
* Create a dataset positive and negative images in new created images file
* [ssd_mobilenet_v1_coco.config](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz)
* [xml_to_csv.py](https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py)
* [generate_tfrecord.py](https://github.com/datitran/raccoon_dataset/blob/master/generate_tfrecord.py)
* Create a new folder named training
* Create a new folder named data

Save following in models/research/object_detection/legacy/training<br/>
* [ssd_mobilenet_v1_coco.config](https://github.com/tensorflow/models/blob/master/research/object_detection/samples/configs/ssd_mobilenet_v1_coco.config)

Firstly, the training model and identify the objects, a dataset will be create using the images obtained from Google Images. The data set must be selected in different environments and from different angles. 10% of the collected data is stored in the test and 90% in the train folders. These test and train folders will be save in images folder.

After preparing Dataset, objects should be labeled with LabelImg and XML files should be created for each data. LabelImg.py must be downloaded for this. XML files are saved in folders with pictures.
```bash
$ pip install labelImg
```

Then, in order for TFRecord files to be created, they must be saved in a csv file with xml files. Csv files should be saved in the data folder.

Change following commands in xml_to_csv.py
```bash
def main():
    for directory in ['train','test']:
        image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')
```
Create csv files
```bash
$ cd /content/gdrive/My Drive/age_det/models/research/object_detection/legacy
$ python3 xml_to_csv.py
```
TFRecord records using the .csv files are created. Classes must be created for tags used when creating TFRecord records.
Change following commands
```bash
def class_text_to_int(row_label):
    if row_label == 'old':
        return 1
    if row_label == 'young':    
        return 2
    else:
        None
```
Then, create TFRecords
```bash
$ python3 generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=data/test.record  --image_dir=images/test
$ python3 generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=data/train.record  --image_dir=images/train
```
Label Map shows the model which ID has which class. For this reason, a Label Map file is a text graph definition file must be created by entering the class and ID information in order to conduct the training. This .pbtxt file must be saved in data file.
```bash
item{
  id: 1
  name: 'old'
}

item{
  id: 2
  name: 'young'
}
```

Change commands in ssd_mobilenet_v1_coco.config
```bash
num_classes: 2
```
```bash
fine_tune_checkpoint: "ssd_mobilenet_v1_coco_11_06_2017/model.ckpt"
```
```bash
train_input_reader: {
tf_record_input_reader {
input_path: "data/train.record"
}
label_map_path: "data/object-detection.pbtxt"
}
```
```bash
eval_input_reader: {
tf_record_input_reader {
input_path: "data/test.record"
}
label_map_path: "data/object-detection.pbtxt"
shuffle: false
num_readers: 1
}
```


Start the training
```bash
$ python3 train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1_coco.config
```

If the training is taking place, you will get an output like the one below.
```bash
INFO:tensorflow:global step 1: loss = 1.1345 (1.034 sec/step)
I0412 20:24:31.416356 140287646844800 learning.py:507] global step 1: loss = 1.1345 (1.034 sec/step)
```

Training should be continued until the given loss value drops below 1. Then training is stopped. Graphics obtained as a result of the training should be exported.
```bash
$ python export_inference_graph.py \
$ --input_type image_tensor \
$ --pipeline_config_path legacy/training/ssd_mobilenet_v1_coco.config \
$ --trained_checkpoint_prefix legacy/training/model.ckpt-21149 \
$ --output_directory age_det_graph/
```

## Tracking of Educational Outcomes with TensorBoard

Load the TensorBoard notebook extension
```bash
$ pip3 install -q tf-nightly-2.0-preview
$ load_ext tensorboard
```

Tracking of educational outcomes
```bash
$ tensorboard --logdir "/content/gdrive/My Drive/age_det/models/research/object_detection/legacy/training/"
```

# Links
Click [here](https://drive.google.com/drive/folders/1DdI4VZHquhSapG-GfEj29izST2MLIciJ?usp=sharing) to access the dataset.<br/>
Click [here](https://drive.google.com/drive/folders/1AY3w1vdhwrl_sIPLvc-bUMj2eq5mCC9c?usp=sharing) to access the trained Age Detection model.
