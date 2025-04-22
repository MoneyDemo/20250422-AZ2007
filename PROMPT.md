幫我使用 Python 撰寫一個 WEB 應用，網站的主要目的是熱點新聞加上輿情分析。

# 這個網站的功能包括：
1. 爬取熱點新聞
2. 輿情分析
3. 顯示新聞和輿情分析結果
4. 首頁可以選擇新聞類別
   - 國內新聞
   - 國際新聞
   - 體育新聞
   - 娛樂新聞
5. 選擇完類別後，顯示該類別的熱點新聞
6. 點擊新聞標題後，顯示該新聞的詳細內容和輿情分析結果

# 系統的網站架構與設計應該要有
- OS 是 Windows 11
- 要使用 python 的虛擬環境來開發。
  - 虛擬環境的名稱為 newsenv。
- 使用 Python 3.11.9 的版本。
- 使用 Flask 作為後端框架。
- 提供 README.md 檔案，說明如何啟動網站等常見 README 內容。
  - 要包含如何執行各種不同的測試的指令與說明。
- 程式碼必須包含適當的註解。
  - 所有的 Class 與 Method 一定要有註解
  - 所有的變數與參數一定要有註解
  - 適當地為所有程式碼加入註解
- 程式碼必須包含適當的單元測試。
  - 測試框架要使用 pytest
  - 測試只針對邏輯部分，前端與服務層不需要測試。
- 使用 Bootstrap 5 來設計網站。
  - 使用 fontawesome 來提供 ICON。
  - 畫面要華麗
  - 必要時可以加入一些動畫效果。
  - 畫面的整體色調要繽紛
- 使用 jsdeliver CDN 來載入 Bootstrap 5 與 fontawesome。
  
其他要求:
- Update relevant documentation in /docs when modifying features
- Keep README.md in sync with new capabilities
- Maintain changelog entries in CHANGELOG.md
- 分階段實作，先產生計畫，並在 https://github.com/lettucebo/20250422-AZ2007 上面新增 issue 來追蹤進度，每完成一步驟就加入 comment 說明目前狀態與進度等等
  - When creating issue, remember to add corresponding labels
  - note: remember always update the issue and add issue comment everytime
- 請使用簡體中文來進行後續與所有的回覆

先不要執行，請先產出一個執行計畫與檔案文件目錄結構給我看，以及提供預計要使用那些 API 來取得新聞資訊，並提供這些API的前置作業說明，例如: 需要註冊帳號、取得 API KEY 等等。