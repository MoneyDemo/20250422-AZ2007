import pytest
from app.services.sentiment_service import SentimentService


def test_analyze_positive_sentiment():
    """Test that analyze() returns positive polarity for positive text."""
    service = SentimentService()
    result = service.analyze("I love sunny days and beautiful weather.")
    assert result['polarity'] > 0
    assert 0 <= result['subjectivity'] <= 1


def test_analyze_negative_sentiment():
    """Test that analyze() returns negative polarity for negative text."""
    service = SentimentService()
    result = service.analyze("I hate rainy days and gloomy weather.")
    assert result['polarity'] < 0
    assert 0 <= result['subjectivity'] <= 1


def test_analyze_neutral_sentiment():
    """Test that analyze() returns near zero polarity for neutral text."""
    service = SentimentService()
    result = service.analyze("It is a book.")
    assert abs(result['polarity']) < 0.1
    assert 0 <= result['subjectivity'] <= 1
