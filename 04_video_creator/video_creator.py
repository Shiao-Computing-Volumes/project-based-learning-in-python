import cv2
import numpy as np

from video import Video

def draw_frames(video, width, height):
    radius = 10
    coordx_mid = int(width/2)
    coordy_mid = int(height/2)
    for coordx in range(-radius, width+radius, 6):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.circle(frame, (coordx, coordy_mid), radius, (255, 255, 255), -1)
        video.write(frame)
    return video

if __name__ == '__main__':
    width = 1280
    height = 720
    filename = "./_outputs/test.mp4"
    video = Video(filename, width, height).get_video()
    video = draw_frames(video, width, height)
    video.release()
