# voiceover.py

from gtts import gTTS
import os

def generate_mongolian_voice(translated_text_path, output_dir="output/"):
    os.makedirs(output_dir, exist_ok=True)

    # Орчуулагдсан монгол текстийг унших
    with open(translated_text_path, "r", encoding="utf-8") as f:
        text = f.read()

    print("🎤 gTTS ашиглан монгол яриа үүсгэж байна...")

    # gTTS дуу үүсгэх (lang='mn' → монгол хэл)
    tts = gTTS(text=text, lang='mn')

    # Хадгалах зам
    audio_output_path = os.path.join(
        output_dir,
        os.path.basename(translated_text_path).replace("_translated.txt", "_voice.mp3")
    )

    # MP3 файл болгож хадгалах
    tts.save(audio_output_path)

    print(f"✅ Монгол яриа хадгалагдлаа: {audio_output_path}")
    return audio_output_path
