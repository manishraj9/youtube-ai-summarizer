# 🎥 YouTube AI Summarizer

> An AI-powered YouTube video summarization application built with **Streamlit, OpenAI Whisper, Google Gemini, yt-dlp, and FFmpeg**.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Whisper](https://img.shields.io/badge/AI-Whisper-green)](https://github.com/openai/whisper)
[![Gemini](https://img.shields.io/badge/AI-Gemini-blue?logo=google)](https://ai.google.dev/)
[![FFmpeg](https://img.shields.io/badge/Audio-FFmpeg-black?logo=ffmpeg)](https://ffmpeg.org/)
[![yt--dlp](https://img.shields.io/badge/YouTube-yt--dlp-red)](https://github.com/yt-dlp/yt-dlp)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌐 Project

**GitHub Repository:**  
https://github.com/manishraj9/youtube-ai-summarizer

**Live Demo:**  
_Add your Streamlit deployment URL here after deployment._

---

# 📌 Overview

YouTube contains an enormous amount of educational, technical, research, and informational content. However, watching a long video just to extract a few important ideas can be time-consuming.

**YouTube AI Summarizer** solves this problem by automatically converting a YouTube video's spoken content into text and then using a Large Language Model to generate a structured summary.

The application combines:

- 🎥 YouTube video processing
- 🎙️ Automatic Speech Recognition
- 🤖 Generative AI
- 📝 Text summarization
- 🧠 Technical concept extraction
- 📜 Transcript generation
- 📥 Downloadable results

Users simply enter a YouTube URL, and the application handles the rest.

---

# ✨ Features

## 🎥 YouTube Video Processing

- Enter any supported YouTube video URL.
- Automatically download the video's audio.
- Extract audio using `yt-dlp`.
- Process audio using FFmpeg.

## 🎙️ AI Transcription

The application uses **OpenAI Whisper** to convert spoken audio into text.

Whisper provides:

- Speech recognition
- Automatic transcription
- Support for different languages
- Local processing

## 🤖 Gemini AI Summarization

The generated transcript is sent to the **Google Gemini API**.

Gemini produces a structured response containing:

### 📝 Summary

A concise explanation of the video's main content.

### 🔑 Key Points

The most important ideas from the video.

### 🧠 Technical Concepts

Important technical terms, technologies, frameworks, and concepts discussed in the video.

### 📚 Detailed Explanation

A more comprehensive explanation designed to make the video easier to understand.

---

# 🏗️ System Architecture

```text
                         🎥 YouTube URL
                                │
                                ▼
                         ┌─────────────┐
                         │    yt-dlp   │
                         └──────┬──────┘
                                │
                                ▼
                         🎵 Audio File
                                │
                                ▼
                         ┌─────────────┐
                         │   FFmpeg    │
                         └──────┬──────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  OpenAI Whisper │
                       └────────┬────────┘
                                │
                                ▼
                         📜 Transcript
                                │
                                ▼
                       ┌─────────────────┐
                       │   Gemini API    │
                       └────────┬────────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
                ▼               ▼               ▼
             Summary       Key Points     Concepts
                │               │               │
                └───────────────┼───────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │    Streamlit    │
                       │       UI        │
                       └─────────────────┘
🔄 Application Workflow

The application follows the following pipeline:

1. User enters YouTube URL
                ↓
2. yt-dlp downloads audio
                ↓
3. FFmpeg processes audio
                ↓
4. Whisper transcribes audio
                ↓
5. Transcript is generated
                ↓
6. Transcript is sent to Gemini
                ↓
7. Gemini analyzes the transcript
                ↓
8. Structured summary is generated
                ↓
9. Results displayed in Streamlit

🛠️ Technology Stack
Programming Language
Python
Frontend / User Interface
Streamlit
Generative AI
Google Gemini API
Speech Recognition
OpenAI Whisper
YouTube Processing
yt-dlp
Audio Processing
FFmpeg
Environment Management
python-dotenv
Deployment
Streamlit Community Cloud
📂 Project Structure
youtube-ai-summarizer/
│
├── app.py
│
├── gemini_test.py
│
├── test_transcription.py
│
├── requirements.txt
│
├── packages.txt
│
├── .gitignore
│
├── .env.example
│
├── README.md
│
└── LICENSE
📄 File Description
File	Description
app.py	Main Streamlit application
gemini_test.py	Script used to test Gemini summarization
test_transcription.py	Script used to test YouTube downloading and Whisper transcription
requirements.txt	Python dependencies
packages.txt	System-level dependencies required during deployment
.env.example	Example environment variable configuration
.gitignore	Prevents secrets, virtual environments, and generated files from being committed
README.md	Project documentation
LICENSE	Project license
🧠 AI Pipeline
1. YouTube Audio Extraction

The application uses yt-dlp to download the audio stream from the supplied YouTube URL.

YouTube URL
     ↓
   yt-dlp
     ↓
Audio
2. Audio Processing

FFmpeg is used to process the downloaded audio so that it can be consumed by Whisper.

Downloaded Audio
       ↓
     FFmpeg
       ↓
Processed Audio
3. Speech-to-Text

OpenAI Whisper converts the audio into a text transcript.

Audio
  ↓
Whisper
  ↓
Transcript

The project currently uses the Whisper base model.

4. Gemini Summarization

The transcript is passed to Gemini with a structured prompt.

The model is instructed to generate:

Summary
    +
Key Points
    +
Technical Concepts
    +
Detailed Explanation
🖥️ User Interface

The application provides a simple interface where the user can enter a YouTube URL.

Example:

🔗 YouTube Video URL

https://www.youtube.com/watch?v=XXXXXXXXXXX

              🚀 Summarize Video

During processing, the application provides status information:

📥 Downloading YouTube audio...
        ↓
🎙️ Transcribing with Whisper...
        ↓
🤖 Generating AI summary...
        ↓
🎉 Video processed successfully!
📊 Output

After processing, the application displays the results in an organized interface.

🎥 Video

The original YouTube video is embedded directly in the application.

🤖 AI Summary

The generated Gemini response is displayed containing:

📝 Summary

🔑 Key Points

🧠 Technical Concepts

📚 Detailed Explanation
📜 Transcript

The complete Whisper transcript can be expanded and viewed.

📥 Downloads

Users can download:

📄 Transcript

as:

transcript.txt

and:

📝 Summary

as:

summary.md
⚙️ Requirements

Before running the project locally, make sure you have:

Python 3.10+
FFmpeg
Internet connection
Google Gemini API key
🚀 Installation
Step 1 — Clone the Repository
git clone https://github.com/manishraj9/youtube-ai-summarizer.git

Move into the project directory:

cd youtube-ai-summarizer
🐍 Step 2 — Create a Virtual Environment
Windows
python -m venv .venv

Activate:

.venv\Scripts\Activate.ps1

If PowerShell blocks the activation script:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then:

.venv\Scripts\Activate.ps1
📦 Step 3 — Install Python Dependencies
pip install -r requirements.txt
🎵 Step 4 — Install FFmpeg

FFmpeg is required for audio processing.

Verify that FFmpeg is available:

ffmpeg -version

If the command returns the FFmpeg version, the installation is working.

🔐 Step 5 — Configure Gemini API

Create a file named:

.env

inside the project root.

Add:

GEMINI_API_KEY=your_gemini_api_key_here

Replace the placeholder with your actual Gemini API key.

⚠️ Security

Never commit your .env file to GitHub.

The project .gitignore should contain:

.env
.venv/
__pycache__/
*.pyc
*.mp3
*.wav
*.webm
transcript.txt
▶️ Step 6 — Run the Application

Start Streamlit:

streamlit run app.py

The application will open in your browser.

Usually Streamlit runs at:

http://localhost:8501
🧪 Testing

The project was tested component-by-component before integrating everything.

Test 1 — YouTube Download

The application successfully downloaded audio from a YouTube video using yt-dlp.

YouTube
   ↓
yt-dlp
   ↓
Audio
Test 2 — FFmpeg

FFmpeg was successfully verified for audio processing.

ffmpeg -version

returned a valid FFmpeg installation.

Test 3 — Whisper

Whisper successfully loaded and transcribed a YouTube video.

The resulting transcript contained the spoken content of the video.

Audio
 ↓
Whisper
 ↓
Transcript
Test 4 — Gemini

The transcript was successfully sent to Gemini.

Gemini generated:

Summary
Key points
Technical concepts
Detailed explanation
Test 5 — End-to-End Application

The final Streamlit application successfully performed:

YouTube URL
     ↓
yt-dlp
     ↓
FFmpeg
     ↓
Whisper
     ↓
Transcript
     ↓
Gemini
     ↓
Structured Summary
     ↓
Streamlit UI
☁️ Streamlit Deployment

The project is configured for deployment on Streamlit Community Cloud.

Deployment Files

The repository contains:

packages.txt

with:

ffmpeg

This allows the deployment environment to install FFmpeg.

Deploying

Go to:

https://share.streamlit.io/

Connect your GitHub account and select:

Repository:
manishraj9/youtube-ai-summarizer

Branch:
main

Main file:
app.py

Then deploy the application.

🔑 Streamlit Secrets

For deployment, don't upload .env.

Instead, add the Gemini API key through Streamlit's Secrets configuration.

Use:

GEMINI_API_KEY = "your_gemini_api_key_here"

The application can then access the secret securely.

🛡️ Security

This project follows basic API key security practices.

Never commit:
.env
Never hard-code:
GEMINI_API_KEY = "..."
Use environment variables locally:
GEMINI_API_KEY=your_key
Use Streamlit Secrets in production.
⚡ Performance

The application currently performs Whisper transcription locally.

For CPU environments, transcription time depends on:

Video duration
CPU performance
Whisper model size
Audio quality

The application uses:

Whisper Base

which provides a balance between speed and transcription quality.

🧩 Why Whisper + Gemini?

The project separates the speech recognition and language understanding tasks.

Whisper
   ↓
Speech → Text

Gemini
   ↓
Text → Understanding → Summary

This modular architecture makes it possible to replace either component independently.

For example:

Whisper
   ↓
Another Speech Model

or:

Gemini
   ↓
Another LLM

without redesigning the entire application.

🎯 Use Cases

This application can be useful for:

🎓 Students

Quickly summarize long educational lectures.

💻 Developers

Extract technical concepts from programming tutorials.

📚 Researchers

Quickly understand long informational videos.

🧑‍💼 Professionals

Extract important information from webinars and presentations.

🎥 Content Creators

Analyze video content and generate notes.

🌐 Online Learners

Convert lengthy video lessons into structured study material.

💡 Example

Suppose the user enters:

https://www.youtube.com/watch?v=XXXXXXXXXXX

The application processes the video:

Downloading...
     ↓
Transcribing...
     ↓
Analyzing...
     ↓
Generating summary...

The final result might contain:

## 📝 Summary

The video explains...

## 🔑 Key Points

- Important concept 1
- Important concept 2
- Important concept 3
- Important concept 4
- Important concept 5

## 🧠 Technical Concepts

- RAG
- Vector Database
- Chunking
- LLM
- Embeddings

## 📚 Detailed Explanation

...
🔮 Future Enhancements

The current project provides the core YouTube summarization pipeline.

Future versions can introduce additional AI capabilities.

💬 1. Chat With the Video

Allow users to ask questions about the video.

User:
What is RAG?

        ↓

AI:
Answer based on the video transcript.
❓ 2. Question Answering

Users could ask:

What was the main topic?

What tools were mentioned?

What did the speaker recommend?

Explain the concept in simple language.
⏱️ 3. Timestamp-Based Summaries

Generate summaries for different sections of a video.

00:00 Introduction
02:15 Main Concept
07:30 Technical Explanation
15:20 Conclusion
📚 4. Study Mode

Automatically generate:

Study notes
Flashcards
Questions
Answers
Important definitions
📝 5. AI Quiz Generation

Generate quizzes from the transcript:

Question:
What is Retrieval-Augmented Generation?

A. ...
B. ...
C. ...
D. ...

Correct Answer:
B
🌍 6. Multi-Language Support

Generate summaries in different languages.

For example:

English
Hindi
Spanish
French
German
🧠 7. RAG-Based Video Assistant

A future version could use:

Transcript
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Semantic Retrieval
    ↓
Gemini

This would allow the user to ask questions about very long videos without sending the entire transcript to the model each time.

🧠 Future RAG Architecture
                    YouTube Video
                         │
                         ▼
                      Whisper
                         │
                         ▼
                     Transcript
                         │
                         ▼
                      Chunking
                         │
                         ▼
                    Embeddings
                         │
                         ▼
                   Vector Database
                         │
                         ▼
                    User Question
                         │
                         ▼
                 Relevant Chunks
                         │
                         ▼
                     Gemini
                         │
                         ▼
                    AI Answer

This would transform the project from a simple summarization application into a more complete YouTube AI Learning Assistant.

📈 Project Development Progress
YouTube Processing          ✅
Audio Extraction            ✅
FFmpeg Integration          ✅
Whisper Transcription       ✅
Gemini Integration          ✅
AI Summarization            ✅
Key Point Extraction        ✅
Technical Concepts          ✅
Detailed Explanation        ✅
Transcript Viewer           ✅
Transcript Download         ✅
Summary Download            ✅
Streamlit UI                ✅
Deployment Configuration    ✅

Chat With Video             🔜
RAG                         🔜
Quiz Generation             🔜
Timestamp Summaries         🔜
Multi-language Support      🔜
📜 License

This project is distributed under the license included in this repository.

See:

LICENSE

for details.

👨‍💻 Author
Manish Raj

Computer Science & Engineering

GitHub:

https://github.com/manishraj9

Project Repository:

https://github.com/manishraj9/youtube-ai-summarizer

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.



