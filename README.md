# YouTube Sentiment Analysis API

A machine learning project that analyzes sentiment of YouTube comments using:

- FastAPI
- Hugging Face NLP
- YouTube Data API
- Streamlit dashboard

## Architecture

User → Streamlit Dashboard → FastAPI API → YouTube API → HuggingFace Model → Sentiment Results

## Features

- Fetch YouTube comments
- Perform sentiment analysis using HuggingFace
- FastAPI REST API
- Streamlit dashboard visualization
- Docker container support

## Environment Variables
YOUTUBE_API_KEY=your_youtube_key
HF_API_TOKEN=your_huggingface_token