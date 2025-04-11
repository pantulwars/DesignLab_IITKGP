import cv2
import os

# Directory containing your videos
video_dir = "./frames"  # Update this path to your folder with videos

# Output directory to store all extracted frames
output_dir = "datasets/dataset/images/all"
os.makedirs(output_dir, exist_ok=True)

# Get a list of all video files (adjust extensions as needed)
video_files = [f for f in os.listdir(video_dir) if f.lower().endswith(('.mp4', '.avi', '.mov'))]

for video_file in video_files:
    video_path = os.path.join(video_dir, video_file)
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_idx = 0
    print(f"Processing video: {video_file} (FPS: {fps})")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Process one frame per second
        if frame_idx % ( fps * 10 ) == 0:
            # Construct output filename with video name as prefix
            output_filename = f"{os.path.splitext(video_file)[0]}_frame_{frame_idx}.jpg"
            cv2.imwrite(os.path.join(output_dir, output_filename), frame)
        frame_idx += 1

    cap.release()

print("Finished processing all videos.")
