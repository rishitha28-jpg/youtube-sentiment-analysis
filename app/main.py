from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

# Create FastAPI application
app = FastAPI(
    title="YouTube Sentiment Analysis API",
    description="Analyze YouTube comments using HuggingFace NLP",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS (for frontend apps like Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api/v1", tags=["Sentiment Analysis"])

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "YouTube Sentiment Analysis API Running",
        "docs": "/docs"
    }

# Health check endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "youtube-sentiment-api"
    }