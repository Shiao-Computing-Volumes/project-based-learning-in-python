import moviepy.editor as mp


if __name__ == '__main__':
    infile = "./_outputs/normal.mp4"
    outfile = "./_outputs/viz_distributions.mp4"
    logo_cs = "./data/logo_cs.JPG"
    
    video = mp.VideoFileClip(infile)

    logo = (mp.ImageClip(logo_cs)
              .set_duration(video.duration)
              .resize(height=50) # if you need to resize...
              .margin(left=8, top=8, opacity=0) # (optional) logo-border padding
              .set_pos(("left","top")))
    final = mp.CompositeVideoClip([video, logo])
    final.write_videofile(outfile)
