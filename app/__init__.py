from flask import Flask
from dotenv import load_dotenv
from app.config import Config


def create_app():
    """
    Create and configure the Flask application.
    """
    # Load environment variables from .env
    load_dotenv()
    app = Flask(__name__, template_folder='templates', static_folder='static')
    # Load configuration
    app.config.from_object(Config)
    # Register blueprints
    from app.routes.news import news_bp
    app.register_blueprint(news_bp)
    return app
