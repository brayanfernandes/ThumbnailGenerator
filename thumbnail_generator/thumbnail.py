import subprocess
import os


VIDEO_PATH = "C:\\xampp\\htdocs\\videos\\vids\\"
IMG_PATH = "C:\\xampp\\htdocs\\videos\\thumbnail\\"
files = os.listdir(VIDEO_PATH)


for file in files:
    video_input_path = VIDEO_PATH + file
    img_output_path = IMG_PATH + (os.path.splitext(file)[0]) + ".jpg"
    subprocess.call(['ffmpeg', '-y', '-i', video_input_path, '-ss', '00:00:04.000','-vframes', '1',img_output_path])


