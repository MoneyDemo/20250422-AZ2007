import os


class Config:
    """
    Configuration for the Flask application.
    """
    # NewsAPI key from environment variable
    NEWSAPI_KEY: str = os.getenv('NEWSAPI_KEY', '')
