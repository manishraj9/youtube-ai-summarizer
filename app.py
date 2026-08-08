import os
import subprocess
import tempfile
from pathlib import Path

import streamlit as st
import whisper
from dotenv import load_dotenv
from google import genai


# --------------------------------------------------
# Configuration
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY is missing. Add it to your .env file.")
    st.stop()

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.6-flash"


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="YouTube AI Summarizer",
    page_icon="🎥",
    layout="wide"
)


# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 5px;
        }

        .subtitle {
            text-align: center;
            color: #888;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .section-title {
            font-size: 25px;
            font-weight: 600;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Load Whisper
# --------------------------------------------------

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")


# --------------------------------------------------
# Download YouTube audio
# --------------------------------------------------

def download_audio(url, output_dir):

    output_template = str(
        Path(output_dir) / "audio.%(ext)s"
    )

    command = [
        "yt-dlp",
        "-x",
        "--audio-format",
        "mp3",
        "-o",
        output_template,
        url
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    audio_file = Path(output_dir) / "audio.mp3"

    if not audio_file.exists():
        raise FileNotFoundError(
            "Audio file was not created."
        )

    return str(audio_file)


# --------------------------------------------------
# Transcribe audio
# --------------------------------------------------

def transcribe_audio(audio_path):

    model = load_whisper_model()

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"]


# --------------------------------------------------
# Generate Gemini summary
# --------------------------------------------------

def generate_summary(transcript):

    prompt = f"""
You are an expert YouTube video summarization assistant.

Analyze the following transcript and produce a useful,
accurate summary.

Use exactly this structure:

## 📝 Summary

Write a clear and concise summary in 2-4 paragraphs.

## 🔑 Key Points

Provide 5-8 important points as bullet points.

## 🧠 Technical Concepts

List the important technical concepts discussed.

## 📚 Detailed Explanation

Explain the important ideas from the video in a
beginner-friendly way.

Do not invent information that is not present
in the transcript.

Transcript:

{transcript}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# --------------------------------------------------
# Main UI
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎥 YouTube AI Summarizer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Transcribe YouTube videos with Whisper and summarize '
    'them using Gemini AI'
    '</div>',
    unsafe_allow_html=True
)


youtube_url = st.text_input(
    "🔗 YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)


if st.button(
    "🚀 Summarize Video",
    type="primary",
    use_container_width=True
):

    if not youtube_url.strip():

        st.warning("Please enter a YouTube URL.")

        st.stop()

    try:

        # ------------------------------------------
        # Temporary directory
        # ------------------------------------------

        with tempfile.TemporaryDirectory() as temp_dir:

            # --------------------------------------
            # Download
            # --------------------------------------

            with st.status(
                "📥 Downloading YouTube audio...",
                expanded=True
            ):

                audio_path = download_audio(
                    youtube_url,
                    temp_dir
                )

                st.write("✅ Audio downloaded.")

            # --------------------------------------
            # Transcription
            # --------------------------------------

            with st.status(
                "🎙️ Transcribing with Whisper...",
                expanded=True
            ):

                transcript = transcribe_audio(
                    audio_path
                )

                st.write("✅ Transcription completed.")

            # --------------------------------------
            # Gemini
            # --------------------------------------

            with st.status(
                "🤖 Generating AI summary...",
                expanded=True
            ):

                summary = generate_summary(
                    transcript
                )

                st.write("✅ Summary generated.")

        # ------------------------------------------
        # Results
        # ------------------------------------------

        st.success("🎉 Video processed successfully!")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                '<div class="section-title">▶️ Video</div>',
                unsafe_allow_html=True
            )

            st.video(youtube_url)

        with col2:

            st.markdown(
                '<div class="section-title">🤖 AI Summary</div>',
                unsafe_allow_html=True
            )

            st.markdown(summary)

        # ------------------------------------------
        # Transcript
        # ------------------------------------------

        st.divider()

        st.markdown(
            '<div class="section-title">📜 Transcript</div>',
            unsafe_allow_html=True
        )

        with st.expander(
            "Show full transcript"
        ):

            st.write(transcript)

        # ------------------------------------------
        # Downloads
        # ------------------------------------------

        st.divider()

        st.markdown(
            '<div class="section-title">📥 Downloads</div>',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                "📄 Download Transcript",
                transcript,
                file_name="transcript.txt",
                mime="text/plain"
            )

        with col2:

            st.download_button(
                "📝 Download Summary",
                summary,
                file_name="summary.md",
                mime="text/markdown"
            )

    except Exception as e:

        st.error(
            "❌ Something went wrong while processing "
            "the video."
        )

        st.exception(e)