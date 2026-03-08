# 📊 YouTube Comment Sentiment Analysis

A full-stack Machine Learning application that analyzes sentiment from YouTube video comments using a Transformer-based NLP model.

The system fetches comments using the YouTube Data API, processes them using a HuggingFace sentiment analysis model, and visualizes the results in an interactive Streamlit dashboard.

---

# 🚀 Features

- Extract comments from any YouTube video
- Perform sentiment analysis using NLP (Transformers)
- FastAPI backend for processing
- Interactive Streamlit dashboard
- Sentiment distribution visualization
- Summary metrics for quick insights
- Overall video sentiment detection
- Top positive and negative comments

---

# 🧠 Tech Stack

| Component | Technology |
|--------|-------------|
| Backend API | FastAPI |
| Frontend Dashboard | Streamlit |
| NLP Model | HuggingFace Transformers |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| External API | YouTube Data API |
| Deployment Ready | Docker |

---

# 🏗 Project Architecture

```
Streamlit Dashboard
        ↓
FastAPI Backend
        ↓
YouTube Data API
        ↓
Transformer Sentiment Model
```

---

# 📂 Project Structure

```
youtube-comment-sentiment
│
├── app
│   ├── api
│   │   └── routes.py
│   │
│   ├── services
│   │   ├── youtube_service.py
│   │   └── sentiment_service.py
│   │
│   ├── models
│   │   └── schemas.py
│   │
│   ├── core
│   │   ├── config.py
│   │   └── logger.py
│   │
│   └── main.py
│
├── frontend
│   └── dashboard.py
│
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```


# 📈 Example Output

The dashboard displays:

- Comment sentiment table
- Sentiment distribution charts
- Sentiment percentage visualization
- Summary metrics
- Overall video sentiment
- Top positive comments
- Top negative comments

# 🌐 Important Links

FastAPI  
https://fastapi.tiangolo.com/

Streamlit  
https://streamlit.io/

HuggingFace Transformers  
https://huggingface.co/docs/transformers/index

YouTube Data API  
https://developers.google.com/youtube/v3

Python Requests  
https://requests.readthedocs.io/

---

# 🔮 Future Improvements

- Multilingual sentiment model
- Emoji sentiment detection
- WordCloud visualization
- Comment filtering
- Video comparison analytics

