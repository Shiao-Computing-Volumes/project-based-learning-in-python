from matplotlib.animation import FFMpegWriter

from studio.settings.frames import FPS, BITRATE, VIDEO_AUTHOR


def frames_writer(animation, outfile):
    writer = FFMpegWriter(
        fps=FPS,
        metadata=dict(artist=VIDEO_AUTHOR),
        bitrate=BITRATE
    )
    animation.save(outfile, writer=writer)
    print("INFO: video saved at {}.".format(outfile))
