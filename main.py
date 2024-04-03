import os
from time import sleep
import random

datasetname = input("Dataset name : ")

labels_dir = input("Enter name of labels folder (default: labels) : ")
frames_dir = input("Enter name of frames folder (default: frames) : ")
labels_dir = labels_dir if labels_dir != "" else "labels"
frames_dir = frames_dir if frames_dir != "" else "frames"

## List of every labels and frames
files_labels = [f for f in os.listdir(labels_dir) if os.path.isfile(os.path.join(labels_dir, f))]
files_frames = [f for f in os.listdir(frames_dir) if os.path.isfile(os.path.join(frames_dir, f))]
files_labels.remove("classes.txt") if "classes.txt" in files_labels else None

## Classes will be useful
classes_file = open(os.path.join(labels_dir, "classes.txt"), "r")
classes = classes_file.read().split("\n")
classes_file.close()

if classes[-1] == "":
	del classes[-1]

## Make the dataset folder
os.mkdir(datasetname)

## Make images/labels directories
os.mkdir(f"{datasetname}\\images")
os.mkdir(f"{datasetname}\\labels")

## Variables of train/val directories
img_train = f"{datasetname}\\images\\train"
img_val = f"{datasetname}\\images\\val"
lbl_train = f"{datasetname}\\labels\\train"
lbl_val = f"{datasetname}\\labels\\val"

## Make train/val directories
os.mkdir(img_train)
os.mkdir(img_val)
os.mkdir(lbl_train)
os.mkdir(lbl_val)

## Ask train/validation split
train_val_ratio = input("Enter the ratio of training/validation sets (default: 0.80) : ")
train_val_ratio = float(train_val_ratio) if train_val_ratio != "" else 0.8

## Tell the user the dataset is now being made
print("The dataset is now being built...")

## This is to check if there is unnecessary frame files
files_labels_filename = [label.split(".")[0] for label in files_labels]
for frame in files_frames:
	frame_filename = frame.split(".")[0]
	if not frame_filename in files_labels_filename:
		os.remove(os.path.join(frames_dir, frame))


## Shuffle
random.shuffle(files_labels)
files_frames = []
for label in files_labels:
	files_frames.append(label.split(".")[0] + ".jpg")


## Split the data into train/validation sets
files_frames_1, files_frames_2 = files_frames[:int(len(files_frames) * train_val_ratio)], files_frames[int(len(files_frames) * train_val_ratio):]
files_labels_1, files_labels_2 = files_labels[:int(len(files_frames) * train_val_ratio)], files_labels[int(len(files_frames) * train_val_ratio):]

## Move the files to the respective directories
for img in files_frames_1:
	os.rename(os.path.join(frames_dir, img), os.path.join(img_train, img))

for img in files_frames_2:
	os.rename(os.path.join(frames_dir, img), os.path.join(img_val, img))

for lbl in files_labels_1:
	os.rename(os.path.join(labels_dir, lbl), os.path.join(lbl_train, lbl))

for lbl in files_labels_2:
	os.rename(os.path.join(labels_dir, lbl), os.path.join(lbl_val, lbl))


print(f"Successfully built the dataset! Now building {datasetname}.yaml...")

## Write the .yaml file
file_content = f"""path: ../datasets/{datasetname}
train: images/train
val: images/val

names:"""

for i, v in enumerate(classes):
	file_content += f"\n  {i}: {v}"

with open(f"{datasetname}.yaml", "w") as yaml:
	yaml.write(file_content)
	yaml.close()


## Ask the user if deleting the frames and labels folder is necessary
is_delete_folders = input(f"Success! Do you want to delete \"{frames_dir}\" and \"{labels_dir}\"? (y/n) : ")
while is_delete_folders != "y" and is_delete_folders != "n":
	is_delete_folders = input("Please type (y/n)")


if is_delete_folders == "y":
	os.rmdir(frames_dir)
	os.rmdir(labels_dir)
