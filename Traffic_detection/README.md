# Traffic Detection and Tracking

## Overview

This project, titled "Traffic Detection and Tracking," implements a complete pipeline for detecting and tracking traffic-related objects (e.g. bicycle, car, motorcycle, bus, truck) in videos. It uses YOLOv8 to process simulated traffic scenes and addresses challenges posed by low-quality, dynamic driver-perspective footage that includes curved roads, intersections, and variable traffic conditions.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pantulwars/DesignLab_IITKGP
cd TrafficDetection
```

### 2. Install Dependencies

```bash
pip install ultralytics opencv-python numpy pandas torch torchvision torchaudio matplotlib labelImg
```

### 3. Download YOLOv8 Model

The repository already contains `yolov8n.pt` or you can download it from [Ultralytics]

## Dataset Preparation

### 1. Extract Frames

- Run the frame extraction script to extract frames from your CARLA simulation videos:

```bash
python frame-generation.py
```

- Frames will be saved in `datasets/dataset/images/all`.

### 2. Annotation with LabelImg

#### Installing and Launching LabelImg

LabelImg is required for creating labeled datasets for object detection. It allows you to draw bounding boxes around objects in images and assign class labels.

To install LabelImg (if not already installed):
```bash
pip install labelImg
```

To launch LabelImg:
```bash
labelImg
```

#### Setting Up LabelImg for YOLO Format

1. After launching LabelImg, go to **View → Auto Save mode** and enable it
2. Go to **View → YOLOv5** to switch to YOLO format (this works for YOLOv8 as well)
3. Open the directory containing your images by clicking **Open Dir** and navigating to `datasets/dataset/images/all`
4. Set the same directory as your save location by clicking **Change Save Dir**

#### Creating a Predefined Classes File

Create a text file `predefined_classes.txt` in your project directory with the following classes:

```
car
motorcycle
bus
truck
traffic light
```

From the LabelImg menu, select "File → Load predefined Classes" and select this file.

#### Annotation Process

1. **Basic Controls**:
   - **W**: Create a rectangle box
   - **D**: Next image
   - **A**: Previous image
   - **Del**: Delete selected box
   - **Ctrl+S**: Save
   - **Space**: Flag the current image as verified

2. **Creating Annotations**:
   - Press `W` or click "Create\nRectBox" in the toolbar
   - Draw a rectangle around an object by clicking and dragging
   - When you release the mouse, select the appropriate class from the dropdown menu
   - Repeat for all objects in the image

3. **Saving and Moving On**:
   - Press `Ctrl+S` to save the annotation (or it will save automatically with Auto Save)
   - Press `D` to move to the next image

4. **YOLO Format Explained**:
   For each image, a corresponding `.txt` file will be created with each line representing one object:
   ```
   <class_id> <center_x> <center_y> <width> <height>
   ```
   All values are normalized between 0 and 1.

#### Tips for Traffic Detection Annotation

- Be consistent in drawing bounding boxes around vehicles (include mirrors)
- Pay special attention to different vehicle types, traffic signs, and pedestrians
- For partially occluded objects, draw the box around the visible part if occlusion is significant
- Select frames that represent diverse scenarios (different lighting, angles, road conditions)

### 3. Organize Dataset

Run the script to split images and labels into train and validation folders:

```bash
python organize-dataset.py
```

This script moves images and corresponding annotation files into `datasets/dataset/images/train`, `datasets/dataset/images/val`, and their respective labels folders.

### 4. Update data.yaml

Ensure your `data.yaml` file has the correct paths and class names:

```yaml
train: dataset/images/train
val: dataset/images/val
nc: 14
names:
  - random
  - car
  - truck
  - bus
  - motorcycle
  - traffic light
  - fire hydrant
  - person
  - bicycle
  - airplane
  - train
  - boat
  - stop sign
  - parking meter
```

## Training

### 1. Run YOLOv8 Training

```bash
yolo train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640
```

### 2. Monitor

- Logs and checkpoints will appear in `runs/detect/<run_name>`.
- You can monitor training progress through the terminal or by checking the logs.

## Inference & Tracking

### 1. Open TrafficDetection.ipynb

- Adjust paths (e.g., `input_video`, `output_video`).
- Run all cells to perform detection and tracking on a video.

### 2. Results

- The processed video with bounding boxes will be saved in `result/` or your specified output path.
- A CSV file (e.g., `vehicle_counts.csv`) may be generated with counts of detected vehicles.
- The notebook processes the video (optimally one frame per second), applies detection, and uses a heuristic-based tracker to annotate vehicle tracks.

## Customization

- Adjust YOLOv8 confidence thresholds in the notebook for different detection sensitivities.


## Additional Resources

- [Ultralytics YOLOv8 Documentation](https://docs.ultralytics.com/)
- [LabelImg GitHub Repository](https://github.com/tzutalin/labelImg)
