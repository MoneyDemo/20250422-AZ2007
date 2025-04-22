# 部署指南

此文件說明如何在生產環境部署 NewsApp。

## 前置作業
1. 確認已安裝 Python 3.11.9。
2. 設定環境變數：
   - `NEWSAPI_KEY`：您的 NewsAPI 金鑰。
   - 其他可自訂的設定，可放入 `.env` 檔案。

## 安裝相依套件
```powershell
# 啟動虛擬環境
.\newsenv\Scripts\Activate.ps1
# 安裝套件
pip install -r requirements.txt
```

## 使用 Waitress 部署
```powershell
# 以 Waitress 作為 WSGI 伺服器，監聽 5000 埠
waitress-serve --port=5000 run:app
```

> 若無法直接呼叫 `waitress-serve`，可改成：
```powershell
python -m waitress --port=5000 run:app
```

## 使用 Docker (選用)
1. 建立 `Dockerfile`：
   ```Dockerfile
   FROM python:3.11.9-slim
   WORKDIR /app
   COPY . /app
   RUN pip install -r requirements.txt
   EXPOSE 5000
   CMD ["waitress-serve", "--port=5000", "run:app"]
   ```
2. 建立映像檔並執行：
   ```powershell
   docker build -t newsapp .
   docker run -d -p 5000:5000 --env NEWSAPI_KEY=your_api_key newsapp
   ```

## 注意事項
- 請確保防火牆開啟對應埠號。
- 可結合 Nginx 或 IIS 作反向代理以支援 HTTPS。
