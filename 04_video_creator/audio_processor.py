import ffmpeg

if __name__ == '__main__':
    videofile = "./_outputs/test.mp4"
    audiofile = "./data/Divertimento_K131.mp3"
    finalfile = "./_outputs/final.mp4"

    # input
    videox = ffmpeg.input(videofile)
    audiox = ffmpeg.input(audiofile)

    # trim video and audio
    video = (videox.video.trim(start=0, end=10).setpts('PTS-STARTPTS'))
    audio = (audiox.audio.filter_('atrim', start=0, end=10)
                          .filter_('asetpts', 'PTS-STARTPTS'))

    # concat
    joined = ffmpeg.concat(video, audio, v=1, a=1).node
    final_video = joined[0]
    # audio fade out
    final_audio = (joined[1].filter('volume', 0.8)
                           .filter('afade', type='out', start_time=8, duration=1))

    # output
    out = ffmpeg.output(final_video, final_audio, finalfile)
    out.run()
