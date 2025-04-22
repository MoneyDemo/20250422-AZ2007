# ADR 002: Integration of TextBlob for Sentiment Analysis

Date: 2025-04-22

## Status
Accepted

## Context
We need a simple yet effective library to perform sentiment analysis on news article content. The library should be easy to integrate and support English text processing.

## Decision
We choose to integrate TextBlob (a built-in wrapper over NLTK and Pattern) for sentiment analysis. The `SentimentService` will utilize TextBlob to compute polarity and subjectivity scores for a given article text.

## Consequences
- Advantages:
  - Easy to use API for sentiment polarity and subjectivity.
  - Lightweight and minimal configuration.
- Disadvantages:
  - Limited language support (primarily English).
  - May not be suitable for large-scale or highly accurate sentiment tasks.

```python
from textblob import TextBlob

def analyze_sentiment(text: str) -> dict:
    blob = TextBlob(text)
    return { 'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity }
```
