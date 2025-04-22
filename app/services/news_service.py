import requests
from typing import Dict, Any


class NewsAPIClient:
    """
    Client for interacting with the NewsAPI service.
    """

    def __init__(self, api_key: str):
        """
        Initialize the NewsAPI client.

        :param api_key: API key for authenticating with NewsAPI
        """
        # API key for NewsAPI
        self.api_key: str = api_key
        # Base URL for NewsAPI endpoints
        self.base_url: str = 'https://newsapi.org/v2'

    def get_top_headlines(self, category: str, country: str = 'us', page_size: int = 20) -> Dict[str, Any]:
        """
        Retrieve top headlines from NewsAPI for a specified category.

        :param category: News category (e.g., 'business', 'entertainment', 'sports')
        :param country: Two-letter country code for news source (default 'us')
        :param page_size: Number of articles to return (default 20)
        :return: Parsed JSON response containing articles and metadata
        :raises HTTPError: If the HTTP request returned an unsuccessful status code
        """
        url: str = f"{self.base_url}/top-headlines"
        # Request parameters
        params: Dict[str, Any] = {
            'apiKey': self.api_key,
            'category': category,
            'country': country,
            'pageSize': page_size
        }
        response = requests.get(url, params=params)
        # Raise error for bad status codes
        response.raise_for_status()
        # Return JSON payload
        return response.json()

    def cache_headlines(self, category: str, articles: list) -> None:
        """
        Cache articles list for later retrieval.

        :param category: News category
        :param articles: List of article dicts
        """
        # In-memory cache of headlines by category
        self._cache.setdefault('headlines', {})[category] = articles

    def get_article_by_index(self, category: str, index: int) -> Dict[str, Any]:
        """
        Retrieve a cached article by category and index.

        :param category: News category
        :param index: Index of the article in the cached list
        :return: Article dictionary
        """
        return self._cache.get('headlines', {}).get(category, [])[index]

    # Initialize internal cache storage
    _cache: Dict[str, Dict[str, Any]] = {}
