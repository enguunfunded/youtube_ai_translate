# transcribe.py

import os
import yt_dlp
import whisper

def download_youtube_audio(youtube_url, output_dir="input/"):
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_dir}%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        video_id = info_dict.get("id", None)
        title = info_dict.get("title", None)
        filename = os.path.join(output_dir, f"{video_id}.mp3")
        return filename, title

def transcribe_audio(youtube_url):
    print("🎧 Аудио татаж байна...")
    audio_path, title = download_youtube_audio(youtube_url)

    print("🧠 Whisper ашиглан транскрипт гаргаж байна...")
    model = whisper.load_model("base")  # base | small | medium | large
    result = model.transcribe(audio_path)

    text = result['text']
    print("📄 Текст амжилттай гарлаа:")
    print(text[:200], "...")  # эхний 200 тэмдэгт харуулна

    # Text-г файл болгож хадгална
    transcript_path = audio_path.replace(".mp3", "_transcript.txt")
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(text)

    return transcript_path, audio_path
