# Object-Detection-in-an-Urban-Environment

# Project overview
1. When Self driving car is running on the road, it is necessary for car to sense object in 3D environment. Object detection is the basis of sense and help to classify object and give instruction on planning and prediction. So object detection takes important role in self driving car system.
2. In this project, A CNN model is trained to classify objects such as cyclists, pedestrians and vehicles using data from Waymo. And then we will classify objects by the trained model in test images with lower loss. 
# Dataset analysis
1. About 10% data are in dark environment. Others are in bright. 

Night      

![night](https://user-images.githubusercontent.com/99339837/153398084-f9d3ddea-5d23-44f4-bda9-aaa1ecb37c4f.jpg)

Day

![day](https://user-images.githubusercontent.com/99339837/153398017-5336c4ed-6d45-4736-8794-613f0b237ad0.jpg)


       
2. Traffic intensity is different. About 80% data has high intensity.

High intensity

![high intensity](https://user-images.githubusercontent.com/99339837/153402604-ca183133-97df-4386-9f42-277638035cb9.jpg)


Low intensity

 ![low intensity](https://user-images.githubusercontent.com/99339837/153401309-a31dcabd-1ea9-4e8b-9369-0fe7c12421c6.jpg)
      

3. Data’s clearance is different.

Clear 


![clear](https://user-images.githubusercontent.com/99339837/153400726-d0c76308-8ca9-4922-a7f9-b5c0b63b4109.jpg)

Not clear
 
 
![unclear](https://user-images.githubusercontent.com/99339837/153401355-c5291b1b-4469-4ad1-9685-22329ea45f43.jpg)

# Cross validation
To train the model, data is split into three parts: training, validation and testing. By the dataset analysis and learning in lesson, dataset is split 0.8 for training, 0.1 for validation and 0.1 for testing. 
Training

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

