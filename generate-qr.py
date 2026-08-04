"""
DIAN Racing Test Ride Log — 生成永久 QR 码（Cloudflare Pages）
"""
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

DIR = os.path.dirname(os.path.abspath(__file__))
QR_PATH = os.path.join(DIR, 'qr-code.png')

# 永久 URL — Cloudflare Pages，国内可直连
URL = 'https://testridelog.pages.dev'

print(f'Generating QR for: {URL}')

W, H = 600, 780

qr = qrcode.QRCode(box_size=8, border=2)
qr.add_data(URL)
qr.make(fit=True)
qr_img = qr.make_image(fill_color='white', back_color='black').convert('RGB')
qr_size = 310
qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)

canvas = Image.new('RGB', (W, H), 'black')
draw = ImageDraw.Draw(canvas)

# Accent bars
draw.rectangle([0, 0, W, 4], fill='#cc0000')
draw.rectangle([0, H - 4, W, H], fill='#cc0000')

# Fonts
try:
    en_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 38)
    en_sub = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 18)
    en_cap = ImageFont.truetype('C:/Windows/Fonts/segoeuil.ttf', 15)
    cn_main = ImageFont.truetype('C:/Windows/Fonts/msyh.ttc', 30)
    cn_sub = ImageFont.truetype('C:/Windows/Fonts/msyh.ttc', 18)
    url_font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 12)
except:
    f = ImageFont.load_default()
    en_title = en_sub = en_cap = cn_main = cn_sub = url_font = f

def cx(bb):
    return (W - (bb[2] - bb[0])) // 2

# Top
bb = draw.textbbox((0, 0), 'TEST RIDE LOG', font=en_title)
draw.text((cx(bb), 36), 'TEST RIDE LOG', fill='white', font=en_title)
bb = draw.textbbox((0, 0), 'DIAN RACING', font=en_sub)
draw.text((cx(bb), 84), 'DIAN RACING', fill='#cc0000', font=en_sub)
draw.line([(180, 118), (W - 180, 118)], fill='#2a2a2a', width=1)

# SCAN TO OPEN
bb = draw.textbbox((0, 0), 'SCAN TO OPEN', font=en_cap)
draw.text((cx(bb), 136), 'SCAN TO OPEN', fill='#666', font=en_cap)

# QR
qr_y = 162
qr_x = (W - qr_size) // 2
draw.rectangle([qr_x - 10, qr_y - 10, qr_x + qr_size + 10, qr_y + qr_size + 10], fill='#cc0000')
draw.rectangle([qr_x - 6, qr_y - 6, qr_x + qr_size + 6, qr_y + qr_size + 6], fill='black')
canvas.paste(qr_img, (qr_x, qr_y))

# Chinese below
info_y = qr_y + qr_size + 34
bb = draw.textbbox((0, 0), '赛车测试日志', font=cn_main)
draw.text((cx(bb), info_y), '赛车测试日志', fill='white', font=cn_main)
bb = draw.textbbox((0, 0), '同济大学 DIAN Racing 电车队', font=cn_sub)
draw.text((cx(bb), info_y + 42), '同济大学 DIAN Racing 电车队', fill='#a8a8a8', font=cn_sub)

# Divider + URL
div_y = info_y + 80
draw.line([(150, div_y), (W - 150, div_y)], fill='#2a2a2a', width=1)
bb = draw.textbbox((0, 0), URL, font=url_font)
draw.text((cx(bb), div_y + 20), URL, fill='#3a3a3a', font=url_font)

# Corner marks
cs, co = 12, 24
for px, py in [(co, co), (W - co, co), (co, H - co), (W - co, H - co)]:
    draw.line([(px - cs//2, py), (px + cs//2, py)], fill='#cc0000', width=2)
    draw.line([(px, py - cs//2), (px, py + cs//2)], fill='#cc0000', width=2)

canvas.save(QR_PATH)
print(f'[OK] QR saved: {QR_PATH}')
print(f'[OK] URL: {URL}')
