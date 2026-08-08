import subprocess
import whisper

YOUTUBE_URL = "https://www.youtube.com/watch?v=h5id4erwD4s"

print("Downloading YouTube audio...")

subprocess.run([
    "yt-dlp",
    "-x",
    "--audio-format", "mp3",
    "-o", "test_audio.%(ext)s",
    YOUTUBE_URL
], check=True)

print("Audio downloaded.")

print("Loading Whisper model...")
model = whisper.load_model("base")

print("Transcribing...")
result = model.transcribe("test_audio.mp3")

transcript = result["text"]

print("\n========== TRANSCRIPT ==========\n")
print(transcript)

with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(transcript)

print("\nTranscript saved to transcript.txt")