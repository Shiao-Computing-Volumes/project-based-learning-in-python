import cv2
from cv2 import VideoWriter, VideoWriter_fourcc


class Video(object):

    def __init__(self, filename,
                       width=1280,
                       height=720,
                       fps=24, seconds=10,
                       videotype='AVC1'):

        self._width = width
        self._height = height
        self._fps = fps
        self._seconds = seconds

        fourcc = VideoWriter_fourcc(*videotype)
        self._video = VideoWriter(filename,
                                  fourcc,
                                  float(self._fps),
                                  (self._width, self._height))

    def get_video(self):
        return self._video
