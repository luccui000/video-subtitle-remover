import os
import sys
import backend.main
import concurrent.futures
from threading import Thread
from moviepy.editor import VideoFileClip, concatenate_videoclips

DURATION = 3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

video_path = "3231473987169980134.mp4"
subtitle_area = (779, 828, 309, 567)


def split_video(input_video):
    clips = []
    file_paths = []
    video_clip = VideoFileClip(input_video)
    chunk_size = int(video_clip.duration // DURATION) + 1
    for i in range(0, chunk_size):
        start_time = i * DURATION
        end_time = (i + 1) * DURATION
        if i == chunk_size - 1:
            end_duration = video_clip.duration - start_time
            end_time = start_time + end_duration
        clips.append(video_clip.subclip(start_time, end_time))

    for i, clip in enumerate(clips):
        filepath = f"temp/output_{i:03d}.mp4"
        clip.write_videofile(filepath)
        file_paths.append(filepath)

    return file_paths


def task(v_path):
    if subtitle_area is not None:
        sr = backend.main.SubtitleRemover(v_path, subtitle_area, True)
        sr.run()



def main():
    try:
        # clips = split_video(video_path)
        num_threads = os.cpu_count()
        clips = ['temp/output_000.mp4', 'temp/output_001.mp4', 'temp/output_002.mp4', 'temp/output_003.mp4', 'temp/output_004.mp4', 'temp/output_005.mp4', 'temp/output_006.mp4']
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            executor.map(task, clips)

        # print("Combine videos...")
        # combine_clips(clips)
    except Exception as e:
        pass


main()
