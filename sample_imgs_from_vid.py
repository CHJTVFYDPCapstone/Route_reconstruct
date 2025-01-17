import cv2
import os
import sys

def sample_frames(video_path, output_folder, frames_per_second):
    """
    Samples frames from a video at a specified rate and saves them as JPEGs.

    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder to save the JPEG frames.
        frames_per_second (int): Number of frames to sample per second.
    """

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Open video file
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    # Get video properties
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    print("---")
    print(fps)
    print(fps//frames_per_second)
    frame_interval = max(1, fps // frames_per_second)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break  # End of video

        # Save frame if it's at the specified interval
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1

    video_capture.release()
    print(f"Saved {saved_count} frames to {output_folder}")

if __name__ == "__main__":

    #cli impl:
    if len(sys.argv) < 4:
        print("Bad useage, wrong number of args")
        print("Args are : video path, output folder, frames per second")
    else:

        video_path = str(sys.argv[1])  # Replace with your video file path
        output_folder = str(sys.argv[2])  # Replace with your desired output folder
        frames_per_second = int(sys.argv[3])   # Number of frames to sample per second

        sample_frames(video_path, output_folder, frames_per_second)
