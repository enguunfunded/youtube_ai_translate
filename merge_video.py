# merge_video.py

from moviepy.editor import VideoFileClip, AudioFileClip
import os
import subprocess

def merge_all(video_path, voice_path, srt_path, output_dir="output/"):
    os.makedirs(output_dir, exist_ok=True)

    print("🎞️ Видео + Voice + Subtitle нэгтгэж байна...")

    # Видео болон аудио файлуудыг moviepy ашиглан унших
    video = VideoFileClip(video_path)
    audio = AudioFileClip(voice_path)

    # Аудио-г видеонд тохируулж суулгана
    final_video = video.set_audio(audio)

    # Түр хугацааны файл
    temp_output = os.path.join(output_dir, "temp_no_sub.mp4")
    final_output = os.path.join(output_dir, "final_output_with_sub.mp4")

    # Voice-тэй видеог түр хадгалах
    final_video.write_videofile(temp_output, codec="libx264", audio_codec="aac")

    # Subtitle-ыг ffmpeg ашиглан видеонд шатаах
    command = [
        "ffmpeg",
        "-i", temp_output,
        "-vf", f"subtitles={srt_path}",
        "-c:a", "copy",
        final_output
    ]

    subprocess.run(command, check=True)

    # Түр файл устгах (хэрвээ хүсвэл хадгалж үлдээж б
