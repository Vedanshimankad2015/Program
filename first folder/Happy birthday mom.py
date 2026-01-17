import tkinter as tk
from PIL import Image, ImageTk
import os
import time
import winsound

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Happy Birthday Mom ❤️")
root.geometry("900x600")
root.resizable(False, False)

WIDTH = 900
HEIGHT = 600

# ---------------- COLORS ----------------
PINK = "#ffe6ee"
WHITE = "#ffffff"
RED = "#d6336c"

# ---------------- CANVAS ----------------
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack()

# ---------------- FRONT PAGE ----------------
front_frame = tk.Frame(canvas, bg=PINK, width=WIDTH, height=HEIGHT)
front_window = canvas.create_window(0, 0, anchor="nw", window=front_frame)

title = tk.Label(
    front_frame,
    text="Happy Birthday Mom ❤️",
    font=("Comic Sans MS", 32, "bold"),
    bg=PINK,
    fg=RED
)
title.pack(pady=20)

# ---------------- IMAGE ----------------
img_path = os.path.join(os.path.dirname(__file__), "mom.jpeg")

if os.path.exists(img_path):
    img = Image.open(img_path).resize((350, 350))
    mom_photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(front_frame, image=mom_photo, bg=PINK)
    img_label.image = mom_photo
    img_label.pack(pady=10)
else:
    tk.Label(
        front_frame,
        text="mom.jpeg NOT FOUND",
        font=("Arial", 18),
        bg=PINK,
        fg="red"
    ).pack()

# ---------------- INSIDE PAGE ----------------
inside_frame = tk.Frame(canvas, bg=WHITE, width=WIDTH, height=HEIGHT)
inside_window = canvas.create_window(WIDTH, 0, anchor="nw", window=inside_frame)

message = (
    
    "Dear Mummy,\n\n"
    "Wishing you a day filled with love, joy,\n"
    "and all the happiness you give us every day.\n\n"
    "Happy Birthday ❤️🎂\n\n"
    "— Your Bulbul"
)

tk.Label(
    inside_frame,
    text=message,
    font=("Comic Sans MS", 20),
    bg=WHITE,
    fg="#333",
    justify="center"
).pack(expand=True)

tk.Label(
    inside_frame,
    text="💖 💐 🎂 💝 🌸",
    font=("Arial", 28),
    bg=WHITE
).pack(pady=20)

# ---------------- SONG ----------------
SONG_PATH = os.path.join(os.path.dirname(__file__), "o_meri_maa.wav")

def play_song():
    if os.path.exists(SONG_PATH):
        winsound.PlaySound(SONG_PATH, winsound.SND_ASYNC)
    else:
        print("Song file not found")

# ---------------- OPEN ANIMATION ----------------
def open_card():
    play_song()
    for _ in range(0, WIDTH, 30):
        canvas.move(front_window, -30, 0)
        canvas.move(inside_window, -30, 0)
        root.update()
        time.sleep(0.01)

# ---------------- BUTTON ----------------
tk.Button(
    front_frame,
    text="💌 Open the Card",
    font=("Arial", 18, "bold"),
    bg=RED,
    fg="white",
    command=open_card
).pack(pady=20)

# ---------------- RUN ----------------
root.mainloop()
from playsound import playsound

SONG_PATH = r"E:\USER DATA\Downloads\o_meri_maa.mp3"
# ↑ r"" is IMPORTANT for Windows paths

print("Type 'go' and press Enter → song plays")
print("Type 'exit' to quit")

while True:
    cmd = input(">> ").strip().lower()

    if cmd == "go":
        print("🎵 Playing song...")
        playsound(SONG_PATH)

    elif cmd == "exit":
        print("👋 Bye")
        break

    else:
        print("❌ Type 'go' or 'exit'")
