from flask import Blueprint, render_template, current_app, abort
from app.services.news_service import NewsAPIClient
from app.services.sentiment_service import SentimentService
from typing import Dict, Any

# Blueprint for news routes
news_bp = Blueprint('news', __name__)

# Mapping of user-facing categories to NewsAPI parameters and labels
CATEGORY_MAP: Dict[str, Dict[str, Any]] = {
    'domestic': {'country': 'tw', 'category': None, 'label': '國內新聞'},
    'international': {'country': 'us', 'category': None, 'label': '國際新聞'},
    'sports': {'country': 'us', 'category': 'sports', 'label': '體育新聞'},
    'entertainment': {'country': 'us', 'category': 'entertainment', 'label': '娛樂新聞'},
}

# Icon mapping for categories
ICON_MAP = {
    'domestic': 'fa-house',
    'international': 'fa-globe',
    'sports': 'fa-futbol',
    'entertainment': 'fa-film'
}

@news_bp.route('/')
def index():
    """
    Home page: display the available news categories.
    """
    # Render the index template with category mappings and icons
    return render_template('index.html', categories=CATEGORY_MAP, icons=ICON_MAP)

@news_bp.route('/<string:cat>')
def show_category(cat: str):
    """
    Display top headlines for a given category.

    :param cat: Category key from URL path
    """
    # Validate category
    if cat not in CATEGORY_MAP:
        abort(404)
    settings = CATEGORY_MAP[cat]
    # Initialize NewsAPI client with API key from config
    api_key = current_app.config.get('NEWSAPI_KEY', '')
    client = NewsAPIClient(api_key)
    # Fetch top headlines
    # Pass empty string if category is None
    category_param = settings['category'] or ''
    data = client.get_top_headlines(category=category_param, country=settings['country'])
    articles = data.get('articles', [])
    # Cache fetched headlines for detail view
    client.cache_headlines(cat, articles)
    # Render category template
    return render_template('category.html', category=cat, label=settings['label'], articles=articles)

@news_bp.route('/<string:cat>/article/<int:index>')
def article_detail(cat: str, index: int):
    """
    Show detailed view for a specific article.

    :param cat: Category key from URL path
    :param index: Index of the article in cached list
    """
    # Validate category
    if cat not in CATEGORY_MAP:
        abort(404)
    # Initialize NewsAPI client
    api_key = current_app.config.get('NEWSAPI_KEY', '')
    client = NewsAPIClient(api_key)
    try:
        # Retrieve article from cache by index
        article = client.get_article_by_index(cat, index)
    except (IndexError, KeyError):
        abort(404)
    # Analyze sentiment of article content
    analyzer = SentimentService()
    content_text = article.get('content') or article.get('description', '')
    sentiment = analyzer.analyze(content_text)
    # Render detail template with sentiment analysis results
    return render_template('detail.html', article=article, sentiment=sentiment)
