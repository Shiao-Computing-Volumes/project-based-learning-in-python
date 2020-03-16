import cv2
import numpy as np

from video import Video

def draw_frames(video, width, height):
    radius = 150
    paint_h = int(height/2)
    for paint_x in range(-radius, width+radius, 6):
        frame = np.random.randint(0, 256, 
                              (height, width, 3), 
                              dtype=np.uint8)
        cv2.circle(frame, (paint_x, paint_h), radius, (0, 0, 0), -1)
        video.write(frame)
    return video

if __name__ == '__main__':
    width = 1280
    height = 720
    filename = "./_outputs/test.mp4"
    video = Video(filename, width, height).get_video()
    video = draw_frames(video, width, height)
    video.release()
