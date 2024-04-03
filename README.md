# YOLODatasetCreator
Makes a dataset prepped for YOLO, using a "frames" and "labels" folder.

## How to prepare the data?
You need to make a folder with all of the frames of the video/images and a folder with all of the labels of the frames.
The file names of the images and labels need to be the same to be associated with each other, which is already done if you use the LabelImg program.

## How do I use the program?
Once you execute the program, a terminal will show up, asking for the dataset name, folder names, training/validation ratio, then ask if you want to delete the "frames" and "labels" folder once it's done.

## Where do i place the dataset then?
Normally, you can put it at any folder. You'll just need to remember to enter the directory with the dataset in command prompt when you want to train the model.
