import pytest
import requests
from app.services.news_service import NewsAPIClient


def test_get_top_headlines_success(monkeypatch):
    """Test that get_top_headlines returns expected data on success."""
    # Sample fake response data
    fake_data = {'status': 'ok', 'totalResults': 1, 'articles': [{'title': 'Test', 'description': 'Desc'}]}

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return fake_data

    # Monkeypatch requests.get
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: FakeResponse())

    client = NewsAPIClient('fake_key')
    result = client.get_top_headlines(category='test', country='us')
    assert result == fake_data


def test_get_top_headlines_http_error(monkeypatch):
    """Test that get_top_headlines raises HTTPError on bad status."""
    class FakeResponse:
        def raise_for_status(self):
            raise requests.HTTPError("Bad request")

    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: FakeResponse())

    client = NewsAPIClient('fake_key')
    with pytest.raises(requests.HTTPError):
        client.get_top_headlines(category='test', country='us')
