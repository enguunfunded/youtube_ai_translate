# subtitle.py

import os

def generate_srt(translated_text_path, output_dir="output/"):
    os.makedirs(output_dir, exist_ok=True)

    with open(translated_text_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Энгийн хуваалт: өгүүлбэр бүрийг нэг subtitle гэж үзнэ
    sentences = text.strip().split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    srt_lines = []
    start_time = 0.0
    duration = 3.5  # нэг өгүүлбэрийг 3.5 секунд гэж тооцно

    for i, sentence in enumerate(sentences, 1):
        end_time = start_time + duration

        start_timestamp = seconds_to_srt_time(start_time)
        end_timestamp = seconds_to_srt_time(end_time)

        srt_lines.append(f"{i}")
        srt_lines.append(f"{start_timestamp} --> {end_timestamp}")
        srt_lines.append(sentence + ".")
        srt_lines.append("")  # хоосон мөр

        start_time = end_time

    # SRT файл хадгалах
    srt_path = os.path.join(
        output_dir,
        os.path.basename(translated_text_path).replace("_translated.txt", ".srt")
    )

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    print(f"✅ Subtitle файл үүсгэлээ: {srt_path}")
    return srt_path


def seconds_to_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"
