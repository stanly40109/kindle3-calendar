from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1072, 1448
OUTPUT = Path(__file__).parent / "docs" / "calendar.png"


def choose_font(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for path in paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    raise RuntimeError("Missing system font")


def centered(draw, position, text, font, fill=0):
    box = draw.textbbox((0, 0), text, font=font)
    draw.text((position[0] - (box[2] - box[0]) / 2, position[1] - (box[3] - box[1]) / 2), text, font=font, fill=fill)


def main():
    now = datetime.now(ZoneInfo("Asia/Taipei"))
    image = Image.new("L", (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    centered(draw, (WIDTH / 2, 310), now.strftime("%B").upper(), choose_font(58, bold=True), fill=75)
    centered(draw, (WIDTH / 2, 445), now.strftime("%A").upper(), choose_font(38), fill=125)
    centered(draw, (WIDTH / 2, HEIGHT / 2 + 110), f"{now.day:02d}", choose_font(360, bold=True))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, "PNG", optimize=True)


if __name__ == "__main__":
    main()
