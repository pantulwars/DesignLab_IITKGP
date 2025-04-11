import os
import shutil
import random

all_images = os.listdir("datasets/dataset/images/all")
all_images = [f for f in all_images if f.endswith(".jpg")]
random.shuffle(all_images)

split_index = int(0.8 * len(all_images))
train_images = all_images[:split_index]
val_images = all_images[split_index:]

# Create directories
os.makedirs("datasets/dataset/images/train", exist_ok=True)
os.makedirs("datasets/dataset/images/val", exist_ok=True)
os.makedirs("datasets/dataset/labels/train", exist_ok=True)
os.makedirs("datasets/dataset/labels/val", exist_ok=True)

# Move images and corresponding annotation files
for img in train_images:
    shutil.move(os.path.join("datasets/dataset/images/all", img), "datasets/dataset/images/train")
    # Move the annotation file if it exists
    label_file = img.replace(".jpg", ".txt")
    if os.path.exists(os.path.join("datasets/dataset/images/all", label_file)):
        shutil.move(os.path.join("datasets/dataset/images/all", label_file), "datasets/dataset/labels/train")

for img in val_images:
    shutil.move(os.path.join("datasets/dataset/images/all", img), "datasets/dataset/images/val")
    label_file = img.replace(".jpg", ".txt")
    if os.path.exists(os.path.join("datasets/dataset/images/all", label_file)):
        shutil.move(os.path.join("datasets/dataset/images/all", label_file), "datasets/dataset/labels/val")