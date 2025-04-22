# NewsApp

Web application for hot news retrieval and sentiment analysis.

## Requirements
- Windows 11
- Python 3.11.9
- Virtual environment: `newsenv`

## Setup
1. 建立並啟動虛擬環境：
   ```powershell
   python -m venv newsenv
   .\newsenv\Scripts\Activate.ps1
   ```
2. 安裝相依套件：
   ```powershell
   pip install -r requirements.txt
   ```
3. 複製環境變數範本：
   ```powershell
   copy .env.example .env
   ```
4. 編輯 `.env`，填入您的 NewsAPI Key：
   ```text
   NEWSAPI_KEY=your_api_key_here
   ```

## 執行
```powershell
python run.py
```

## 測試
```powershell
pytest
```

## 範例測試輸出
```bash
> pytest
======================== test session starts ========================
collected 4 items
 
tests/test_news_service.py ..                                 [50%]
tests/test_sentiment_service.py ..                            [100%]
 
========================= 4 passed in 0.45s =========================
```

## Changelog
請參閱 [CHANGELOG.md](CHANGELOG.md) 以取得版本歷史紀錄。

## 目錄結構
```
app/         # Flask application
  config.py
  services/news_service.py
  routes/news.py
  templates/
    base.html
    index.html
    category.html
    detail.html
run.py       # App entrypoint
requirements.txt
README.md
CHANGELOG.md
```
