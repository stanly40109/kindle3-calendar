from __future__ import annotations

import calendar
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image, ImageDraw, ImageFont
import holidays


WIDTH, HEIGHT = 1072, 1448  # Kindle Paperwhite 3 native resolution
TZ = ZoneInfo("Asia/Taipei")
ROOT = Path(__file__).parent
OUTPUT = ROOT / "docs" / "calendar.png"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
        "C:/Windows/Fonts/msjhbd.ttc" if bold else "C:/Windows/Fonts/msjh.ttc",
    ]
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    raise RuntimeError("找不到可顯示繁體中文的字型。請依 README 在 GitHub Actions 執行。")


def center(draw: ImageDraw.ImageDraw, xy: tuple[float, float], text: str, fnt, fill=0):
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text((xy[0] - (box[2] - box[0]) / 2, xy[1] - (box[3] - box[1]) / 2), text, font=fnt, fill=fill)


def main() -> None:
    now = datetime.now(TZ)
    year, month, today = now.year, now.month, now.day
    tw_holidays = holidays.Taiwan(years=year)
    image = Image.new("L", (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(image)

    title = font(72, bold=True)
    subtitle = font(30)
    weekday = font(32, bold=True)
    day_font = font(40)
    day_font_bold = font(40, bold=True)
    tiny = font(22)

    center(draw, (WIDTH / 2, 155), f"{year} 年 {month} 月", title)
    center(draw, (WIDTH / 2, 238), now.strftime("%A").replace("Monday", "星期一").replace("Tuesday", "星期二").replace("Wednesday", "星期三").replace("Thursday", "星期四").replace("Friday", "星期五").replace("Saturday", "星期六").replace("Sunday", "星期日"), subtitle, fill=85)
    draw.line((90, 295, WIDTH - 90, 295), fill=30, width=3)

    left, right = 90, WIDTH - 90
    top = 365
    col_w = (right - left) / 7
    row_h = 145
    for index, label in enumerate(["一", "二", "三", "四", "五", "六", "日"]):
        center(draw, (left + col_w * (index + .5), 330), label, weekday, fill=90 if index < 5 else 140)

    weeks = calendar.Calendar(firstweekday=0).monthdayscalendar(year, month)
    while len(weeks) < 6:
        weeks.append([0] * 7)

    for row, week in enumerate(weeks):
        y1 = top + row * row_h
        for col, day in enumerate(week):
            x1 = left + col * col_w
            x2, y2 = x1 + col_w, y1 + row_h
            if day == today:
                draw.rounded_rectangle((x1 + 7, y1 + 7, x2 - 7, y2 - 7), radius=16, fill=230, outline=0, width=3)
            elif col >= 5:
                draw.rectangle((x1 + 8, y1 + 8, x2 - 8, y2 - 8), fill=247)
            if day:
                is_holiday = datetime(year, month, day).date() in tw_holidays
                fill = 120 if col >= 5 or is_holiday else 0
                center(draw, ((x1 + x2) / 2, y1 + 61), str(day), day_font_bold if day == today else day_font, fill=fill)
                if is_holiday:
                    name = str(tw_holidays.get(datetime(year, month, day).date(), ""))
                    center(draw, ((x1 + x2) / 2, y1 + 108), name[:6], tiny, fill=125)

    footer = f"今天：{year:04d}-{month:02d}-{today:02d}  ·  台灣時間"
    center(draw, (WIDTH / 2, HEIGHT - 100), footer, subtitle, fill=105)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, "PNG", optimize=True)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
