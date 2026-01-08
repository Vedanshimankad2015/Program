from PIL import Image, ImageDraw, ImageFont

# Create image
width, height = 1200, 800
image = Image.new("RGB", (width, height), (255, 228, 235))
draw = ImageDraw.Draw(image)

# Try loading a font (fallback if not found)
try:
    title_font = ImageFont.truetype("arial.ttf", 80)
    text_font = ImageFont.truetype("arial.ttf", 36)
    sign_font = ImageFont.truetype("arial.ttf", 40)
except:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()
    sign_font = ImageFont.load_default()

# Title
title_text = "Happy Birthday Mom ❤️"
bbox = draw.textbbox((0, 0), title_text, font=title_font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
bbox = draw.textbbox((0, 0), title_text, font=title_font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
draw.text(
    ((width - tw) / 2, 50),
    title_text,
    fill=(255, 105, 180),
    font=title_font
)

# Message
message = (
    "Thank you for your support in everything\n"
    "your sacrifice of your career.\n"
    "You are the best Mom,Wife,Daughter,Sister,Friend\n"
    "the most important person in my life.\n\n"
    "May your life always be filled with joy and happiness\n"
    "Happpiest Birthday Mom!"
)

draw.multiline_text(
    (200, 250),
    message,
    fill=(60, 60, 60),
    font=text_font,
    spacing=15
)

signature = "With all my love,\nYour daughter 💐"
draw.multiline_text(
    (750, 550),
    signature,
    fill=(120, 40, 80),
    font=sign_font,
    spacing=10
)
for x in range(150, 1050, 150):
    draw.text((x, 700), "❤️", font=sign_font, fill=(200, 50, 100))

image.save("happy_birthday_mom.png")

print("🎉 Birthday card created")

from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk
import time

# Load your existing card
img_path = "happy_birthday_mom.png"
original = Image.open(img_path)

# Tkinter window
root = Tk()
root.title("Happy Birthday Mom ❤️")

# Canvas to display image
canvas = Canvas(root, width=1200, height=800)
canvas.pack()

# Animation: zoom in
for scale in range(50, 101, 2):  # 50% to 100%
    width = int(original.width * scale / 100)
    height = int(original.height * scale / 100)
    img = original.resize((width, height), Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)
    
    canvas.delete("all")
    # center the image
    canvas.create_image(600, 400, image=tk_img, anchor="center")
    root.update()
    time.sleep(0.03)

# Keep the window open
root.mainloop()

