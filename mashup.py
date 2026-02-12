import os
import shutil
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def create_mashup(singer, num_videos, duration, output_file):

    # Clean old folder
    if os.path.exists("audios"):
        shutil.rmtree("audios")

    os.makedirs("audios", exist_ok=True)

    print("⬇️ Downloading audio from YouTube...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audios/%(title)s.%(ext)s',
        'noplaylist': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': False
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"scsearch{num_videos}:{singer} songs"])

    print("✂️ Trimming audio...")

    trimmed_files = []

    for file in os.listdir("audios"):
        if file.endswith(".mp3"):
            path = os.path.join("audios", file)
            audio = AudioSegment.from_mp3(path)

            if len(audio) < duration * 1000:
                continue

            clip = audio[:duration * 1000]
            new_path = os.path.join("audios", "trim_" + file)
            clip.export(new_path, format="mp3")
            trimmed_files.append(new_path)

    print("🔗 Merging files...")

    final = AudioSegment.empty()

    for f in trimmed_files:
        final += AudioSegment.from_mp3(f)

    final.export(output_file, format="mp3")

    print("✅ Mashup created:", output_file)

    return output_file
