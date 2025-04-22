from textblob import TextBlob


class SentimentService:
    """
    Service for performing sentiment analysis on text content using TextBlob.
    """

    def analyze(self, text: str) -> dict:
        """
        Analyze the sentiment of the given text.

        :param text: The text content to analyze
        :return: A dictionary with 'polarity' and 'subjectivity' scores
        """
        # Create a TextBlob object for sentiment analysis
        blob = TextBlob(text)
        # Return polarity (-1.0 to 1.0) and subjectivity (0.0 to 1.0)
        return {
            'polarity': blob.sentiment.polarity,
            'subjectivity': blob.sentiment.subjectivity
        }
