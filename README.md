# Object-Detection-in-an-Urban-Environment

## Project overview
In this project, Data from the Waymo Open dataset is used to create a convolutional neural network to detect and classify objects. This is done by following steps such as data acquisition and processing, Exploratory data analysis(EDA) , cross validation, Data augmentation and creation of animations.

## Instructions
### Data
<br> Data from the Waymo Open dataset has already been downloaded in the classroom workspace. You can find the downloaded and processed files within the /data/waymo/ directory (note that this is different than the /home/workspace/data you'll use for splitting )
### Exploratory Data Analysis
<br> * Open the Exploratory Data Analysis notebook and implement a display_instances function to display images and annotations using matplotlib.  
<br> * Exploring the data and report findings. Report anything relevant about the dataset in the writeup.
### Create the splits
<br> Create the different splits: training, validation and testing. implement the split_data function in the create_splits.py file. Once you have implemented this function, run it using:
<br> python create_splits.py --data_dir /home/workspace/data/
### Edit the config file
<br> *Download the pretrained model and move it to training/pretrained-models/.
<br> *Edit the config files to change the location of the training and validation files, as well as the location of the label_map file, pretrained weights. also need to adjust the batch size. To do so, run the following:
<br> python edit_config.py --train_dir /home/workspace/data/train/ --eval_dir /home/workspace/data/val/ --batch_size 4 --checkpoint ./training/pretrained-models/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/checkpoint/ckpt-0 --label_map label_map.pbtxt
A new config file has been created, pipeline_new.config.
### Training
<br> Launch very first experiment with the Tensorflow object detection API. Create a folder training/reference. Move the pipeline_new.config to this folder. You will now have to launch two processes:
#### a training process:
<br> * python model_main_tf2.py --model_dir=training/reference/ --pipeline_config_path=training/reference/pipeline_new.config
#### an evaluation process:
<br> * python model_main_tf2.py --model_dir=training/reference/ --pipeline_config_path=training/reference/pipeline_new.config --checkpoint_dir=training/reference/
### Improve the performances
<br> Try different data augmentation combinations and select the one you think is optimal for our dataset. Justify your choices in the writeup.
### Creating an animation
<br> Export the trained model and create a video of your model's inferences for any tf record file. 

## Dataset analysis
Following analysis are made after exploring the dataset
<br> * Some images are taken in town,highway. There are vehicles, pedestrians and a cyclist. But not all the images have all the class objects. Most of images only have cars, pedestrians. 
<br> * Some Images are taken during the day, some at night.
<br> * Some images are very clear but some other images are dark,blured by fog.

![night](https://user-images.githubusercontent.com/99339837/153398084-f9d3ddea-5d23-44f4-bda9-aaa1ecb37c4f.jpg)
![day](https://user-images.githubusercontent.com/99339837/153398017-5336c4ed-6d45-4736-8794-613f0b237ad0.jpg)
![high intensity](https://user-images.githubusercontent.com/99339837/153402604-ca183133-97df-4386-9f42-277638035cb9.jpg)
![low intensity](https://user-images.githubusercontent.com/99339837/153401309-a31dcabd-1ea9-4e8b-9369-0fe7c12421c6.jpg)
![clear](https://user-images.githubusercontent.com/99339837/153400726-d0c76308-8ca9-4922-a7f9-b5c0b63b4109.jpg)
![unclear](https://user-images.githubusercontent.com/99339837/153401355-c5291b1b-4469-4ad1-9685-22329ea45f43.jpg)
![1006](https://user-images.githubusercontent.com/99339837/170037858-bec2b546-da51-43f3-a261-a123ab2bce36.jpg)

This chart is for the object distribution. 
1000 images are taken randomly from dataset and volume of class objects are summarized. It shows that vehicle has the biggest number.  Pedestrians are much but less than vehicle. Cyclists have the least number. So the distribution is not balanced.
We can see from these charts that the images contain a higer number of vehicles that pedestrians and cyclists, where cyclists are the least numerous objects.

![class distribution](https://user-images.githubusercontent.com/99339837/170052524-5ace906c-2d1a-42b4-b9ab-d40d1fcfc9e8.jpg)

## Cross validation
<br> * In this program, Cross validation strategy is to randomly split the dataset into three parts as traing,testing and evaluation. The ratio is 8:1:1. Because the training need large number of data so that the model can be well trained. From the analysis, cylicst has very small number. if the training data is not much, cyclist maybe not recognized.
<br> *The dataset is randomly splitted in order to make sure that images are evenly distributed amongs the train, eval and test.

## Training
Reference experiment




![before](https://user-images.githubusercontent.com/99339837/153402771-86d8fe5d-a29e-4088-b4d9-7673caa91896.jpg)





With pre-trained model, the loss is descended. But after 2.5k, the loss is still about 4.26. it means gap between prediction and actual is not good. Object is not be classified correctly.



# Improve on the reference
Compared with reference experiment, below strategies are added.
1. Random_rgb_to_gray. Set the probability to 0.2.
2. Random_adjust_contrast. Set the min_delta as 0.5 and max_delta as 1.0.
3. Random_adjust_brightness. Set the max_delta as 0.4.
After these augmentation are implemented, total loss train and eval are reduced to 0.8548 and 0.9018 respectively.

 ![after](https://user-images.githubusercontent.com/99339837/153401113-f6b3fadf-cd3b-452e-a02f-448c7e5a752d.jpg)


DetectionBoxes_Precision/mAP: 0.1103
DetectionBoxes_Recall/AR@1: 0.0266
Total_loss Train: 0.8548
Total_loss eval:  0.9018

