# main.py
from transcribe import transcribe_audio
from translate import translate_text
from voiceover import generate_mongolian_voice
from subtitle import generate_srt
from merge_video import merge_all

def main(youtube_link):
    print("🔽 Видеог татаж байна...")
    audio_path, video_path = transcribe_audio(youtube_link)

    print("📝 Англи текст → Монгол текст рүү хөрвүүлж байна...")
    translated_text = translate_text(audio_path)

    print("🔊 Монгол дуу хоолой үүсгэж байна...")
    voice_path = generate_mongolian_voice(translated_text)

    print("📄 Subtitle (SRT) файл үүсгэж байна...")
    srt_path = generate_srt(translated_text)

    print("🎬 Эцсийн видео нэгтгэж байна...")
    output_path = merge_all(video_path, voice_path, srt_path)

    print(f"✅ Дууслаа! Файл: {output_path}")

if __name__ == "__main__":
    # Та видео линкээ энд өгнө
    youtube_link = input("YouTube линк оруулна уу: ")
    main(youtube_link)
