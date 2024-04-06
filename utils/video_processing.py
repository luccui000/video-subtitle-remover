from moviepy.editor import VideoFileClip, concatenate_videoclips

DURATION = 3


def split_video(input_video):
    clips = []
    video_clip = VideoFileClip(input_video)
    chunk_size = int(video_clip.duration // DURATION) + 1
    for i in range(0, chunk_size):
        start_time = i * DURATION
        end_time = (i + 1) * DURATION
        if i == chunk_size - 1:
            end_duration = video_clip.duration - start_time
            end_time = start_time + end_duration
        clips.append(video_clip.subclip(start_time, end_time))

    files = []
    for i, clip in enumerate(clips):
        filepath = f"temp/output_{i:03d}.mp4"
        files.append(filepath)
        clip.write_videofile(filepath)

    return files


def combine_clips(clips, folder="temp"):
    try:
        video_files = [VideoFileClip(f"{folder}/output_{i:03d}.mp4") for i in range(len(clips))]
        print(video_files)
        final_video = concatenate_videoclips(video_files)
        final_video.write_videofile(f"{folder}/output.mp4")
    except Exception as e:
        pass

