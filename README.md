# YOLODatasetCreator
Makes a dataset prepped for YOLO, using a "frames" and "labels" folder. Also makes a yaml file.



## How to prepare the data?
You need to make a folder with all of the frames of the video/images and a folder with all of the labels of the frames.
There also needs to be a file with classes in the "labels" folder.
The file names of the images and labels need to be the same to be associated with each other, which is already done if you use the LabelImg program.

## How do I use the program?
You MUST put the exe at the same directory as the "frames" and "labels" folder.
Once you execute the program, a terminal will show up, asking for the dataset name, folder names, training/validation ratio, then ask if you want to delete the two folders once it's done.

## Where do i place the dataset then?
Normally, you can put it at any folder. You'll just need to remember to enter the directory with the dataset in command prompt when you want to train the model.
You place the yaml file in the dataset config folder, found in the yolo program directory. Since I downloaded yolo with Anaconda, mine is found at "C:\Users\*******\anaconda3\envs\main\Lib\site-packages\ultralytics\cfg\datasets", the folder is filled with yaml files.

## Will there be any updates?
If there will be any issues, yes. But I won't be very active when it comes to adding new stuff to the dataset creator.
