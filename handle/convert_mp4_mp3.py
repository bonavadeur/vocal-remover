import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("file.mp4"))
video.audio.write_audiofile(os.path.join("file.mp3"))
