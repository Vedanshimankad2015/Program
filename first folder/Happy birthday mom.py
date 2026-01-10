import tkinter as tk
from PIL import Image, ImageTk
import os

# ---------------- DEBUG PRINT ----------------
print("Program started")

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("TEST WINDOW")
root.geometry("600x400")
root.configure(bg="pink")

# ---------------- TEXT ----------------
label = tk.Label(
    root,
    text="TKINTER IS WORKING ✅",
    font=("Arial", 24, "bold"),
    bg="pink",
    fg="black"
)
label.pack(pady=20)

# ---------------- IMAGE TEST ----------------
img_path = os.path.join(os.path.dirname(__file__), "mom.jpeg")
print("Looking for image at:", img_path)

if os.path.exists(img_path):
    img = Image.open(img_path)
    img = img.resize((200, 200))
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=photo, bg="pink")
    img_label.image = photo
    img_label.pack(pady=10)
else:
    error = tk.Label(
        root,
        text="IMAGE NOT FOUND ❌",
        font=("Arial", 16),
        bg="pink",
        fg="red"
    )
    error.pack()

# ---------------- RUN ----------------
root.mainloop()
# ---------------- DEBUG PRINT ----------------
print("Program ended")
import tkinter as tk
from PIL import Image, ImageTk
import os
import time

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

# ---------------- MAIN CANVAS ----------------
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack()

# ---------------- FRONT PAGE FRAME ----------------
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
    error = tk.Label(
        front_frame,
        text="❌ mom.jpeg NOT FOUND\nPut the image in the same folder",
        font=("Arial", 16, "bold"),
        bg=PINK,
        fg="red"
    )
    error.pack(expand=True)

# ---------------- INSIDE PAGE FRAME ----------------
inside_frame = tk.Frame(canvas, bg=WHITE, width=WIDTH, height=HEIGHT)
inside_window = canvas.create_window(WIDTH, 0, anchor="nw", window=inside_frame)

message = (
    
    "Dear Mummy,\n\n"
    "Wishing you a day filled with love, joy, and \n     all the happiness you bring into our lives every day.\n"
        "Thank you for being the incredible person you are.\n   Happy Birthday!🤞💖🎂😍\n\n"
    "With all my love,\n\n"
    "Your bulbul"
)

msg_label = tk.Label(
    inside_frame,
    text=message,
    font=("Comic Sans MS", 20),
    bg=WHITE,
    fg="#333333",
    justify="center"
)
msg_label.pack(expand=True)

hearts = tk.Label(
    inside_frame,
    text="💖 💐 🎂 💝 🌸",
    font=("Arial", 28),
    bg=WHITE
)
hearts.pack(pady=20)

# ---------------- OPEN ANIMATION ----------------
def open_card():
    for i in range(0, WIDTH + 1, 30):
        canvas.move(front_window, -30, 0)
        canvas.move(inside_window, -30, 0)
        root.update()
        time.sleep(0.01)

# ---------------- OPEN BUTTON ----------------
open_btn = tk.Button(
    front_frame,
    text="💌 Open the Card",
    font=("Arial", 18, "bold"),
    bg=RED,
    fg="white",
    command=open_card
)
open_btn.pack(pady=20)

# ---------------- RUN ----------------
root.mainloop()