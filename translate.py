# translate.py

from deep_translator import GoogleTranslator
import os

def translate_text(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        english_text = f.read()

    print("🌐 Deep Translator ашиглан монгол руу орчуулж байна...")

    translated_text = GoogleTranslator(source='en', target='mn').translate(english_text)

    translated_path = transcript_path.replace("_transcript.txt", "_translated.txt")
    with open(translated_path, "w", encoding="utf-8") as f:
        f.write(translated_text)

    print("✅ Орчуулга амжилттай!")
    return translated_path
