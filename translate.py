# translate.py

from transformers import MarianMTModel, MarianTokenizer

# HuggingFace дээрх англи ➝ монгол загвар
MODEL_NAME = "Helsinki-NLP/opus-mt-en-mn"

# Загвар болон tokenizer ачааллах
tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

def translate_text(transcript_path):
    # Текст файлыг уншина
    with open(transcript_path, "r", encoding="utf-8") as f:
        original_text = f.read()

    # Хэт урт бол хэсэгчилнэ
    sentences = original_text.strip().split(". ")
    translated_chunks = []

    print("🌐 Орчуулга хийж байна...")

    for sentence in sentences:
        if sentence.strip() == "":
            continue
        inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        translated = model.generate(**inputs)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        translated_chunks.append(translated_text)

    full_translation = ". ".join(translated_chunks)

    # Орчуулсан текстийг файлд хадгална
    translated_path = transcript_path.replace("_transcript.txt", "_translated.txt")
    with open(translated_path, "w", encoding="utf-8") as f:
        f.write(full_translation)

    print("✅ Орчуулга амжилттай боллоо!")
    return translated_path
