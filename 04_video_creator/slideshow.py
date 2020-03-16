from os.path import isfile, join

import cv2

from video import Video
 

def slideshow(video, images, images_dir, fps):
    for index in range(len(images)):
        image = cv2.imread(images_dir + images[i])
        video.write(image)
    return video

 
if __name__=="__main__":
    fps = 25.0
    image_dir = "./data/"
    outfile = "./_outputs/slideshow.mp4"

    images = [image for image in os.listdir(image_dir) if isfile(join(image_dir, image))]
    # sorting files by name
    images.sort(key=lambda x: int(x[5:-4]))

    video = Video(outfile, width, height, fps=fps).get_video()
    video = slideshow(video, images, images_dir, fps)
    video.release()
