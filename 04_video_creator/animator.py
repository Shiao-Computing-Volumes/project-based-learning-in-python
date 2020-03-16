import numpy as np
import matplotlib.pyplot as plt

from moviepy.editor import VideoClip, AudioFileClip
from moviepy.video.io.bindings import mplfig_to_npimage


x = np.linspace(-2, 2, 200)

fig, ax = plt.subplots()
def make_frame(t):
    ax.clear()
    ax.plot(x, np.sinc(x**2) + np.sin(x + 2*np.pi/duration * t), lw=3)
    ax.set_ylim(-1.5, 2.5)
    return mplfig_to_npimage(fig)


if __name__ == '__main__':
    duration = 2
    animation = VideoClip(make_frame, duration=duration)
    
    audioclip = AudioFileClip("./data/piano.mp3")
    animation = animation.set_audio(audioclip) 
    animation.write_videofile('./_outputs/animation.mp4', fps=20)
    # animation.write_gif('./_outputs/animation.gif', fps=20)
