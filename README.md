# Kindle Nordic daily lockscreen

此模板每天輸出一張 PW3 專用的 `1072×1448` 灰階 PNG。畫面採乾淨的北歐留白感，只顯示英文月份、英文星期與大日期；不使用中文字型，也不含行程、天氣、假日或其他資訊。

1. 在 GitHub 新增一個公開 repository，例如 `kindle-calendar`。
2. 將此資料夾的所有內容上傳至 repository 根目錄。
3. 到 **Settings → Pages**，選 **Deploy from a branch**、`main`、`/docs`。
4. 到 **Actions** 手動執行一次 `Update Kindle date`。
5. Kindle 圖片網址為：

   `https://<你的帳號>.github.io/kindle-calendar/calendar.png`

在 Online Screensaver 的 `config.sh` 設定：

```sh
DEFAULTINTERVAL=1440
SCHEDULE="00:00-24:00=1440"
IMAGE_URI="https://<你的帳號>.github.io/kindle-calendar/calendar.png"
DISABLE_WIFI=1
```

GitHub Actions 每天在台灣時間 00:15 重新產圖並提交至 Pages；排程偶爾可能延遲。公開 repository 若 60 天沒有任何活動，GitHub 可能停用排程，重新手動執行一次工作流程即可恢復。
