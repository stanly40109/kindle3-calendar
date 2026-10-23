# Kindle 月曆：GitHub Pages 模板

這個模板每天產生一張 `1072×1448` 灰階 PNG，適合 Kindle Paperwhite 3。月曆採繁體中文、台灣時區、週一為每週第一日，標示今日與台灣國定假日；不含任何私人行程。

## 部署到自己的 GitHub

1. 在 GitHub 建立一個新的 **公開** repository，例如 `kindle-calendar`。
2. 將本資料夾內所有檔案上傳到該 repository 的根目錄。
3. 到 repository 的 **Settings → Pages**。
4. 在 **Build and deployment**，選擇 **Deploy from a branch**；branch 選 `main`，folder 選 `/docs`，然後儲存。
5. 到 **Actions**，開啟 `Update Kindle calendar`，按 **Run workflow** 一次。
6. 等工作流程完成，月曆網址會是：

   `https://<你的帳號>.github.io/kindle-calendar/calendar.png`

   若 repository 名稱不是 `kindle-calendar`，請把網址中的名稱替換成實際 repository 名稱。

## Kindle 的 Online Screensaver 設定

在 `extensions/onlinescreensaver/bin/config.sh` 設定：

```sh
DEFAULTINTERVAL=1440
SCHEDULE="00:00-24:00=1440"
IMAGE_URI="https://<你的帳號>.github.io/kindle-calendar/calendar.png"
DISABLE_WIFI=1
```

再從 KUAL 的 Online-Screensaver 選單先選 **Update now**；確認鎖屏正常顯示後，才選 **Enable auto-download**。

## 注意事項

- GitHub Pages 的 PNG 是公開的。此模板只輸出日期與假日，請不要把私人行程、姓名或地址寫進去。
- GitHub Actions 排程可能偶有延遲；每天更新一次的月曆通常不受影響。
- 公開 repository 連續 60 天沒有任何活動時，GitHub 可能停用排程工作流程；開啟 Actions 手動執行一次即可重新啟用。
