from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    YOUTUBE_API_KEY: str
    HF_API_TOKEN: str

    class Config:
        env_file = ".env"

settings = Settings()