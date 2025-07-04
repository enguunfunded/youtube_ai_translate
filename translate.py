# translate.py

from googletrans import Translator
import os

def translate_text(transcript_path):
    translator = Translator()

    with open(transcript_path, "r", encoding="utf-8") as f:
        english_text = f.read()

    print("🌐 Google Translate ашиглан орчуулж байна...")
    result = translator.translate(english_text, src='en', dest='mn')

    translated_text = result.text

    # Хадгалах
    translated_path = transcript_path.replace("_transcript.txt", "_translated.txt")
    with open(translated_path, "w", encoding="utf-8") as f:
        f.write(translated_text)

    print("✅ Орчуулга амжилттай!")
    return translated_path
