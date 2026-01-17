import turtle

screen = turtle.Screen()
screen.setup(600, 400)
screen.colormode(255)

r, g, b = 120, 200, 150

def click(x, y):
    global r, g, b
    r = (r + 20) % 256
    g = (g + 10) % 256
    b = (b + 30) % 256
    screen.bgcolor(r, g, b)

screen.onclick(click)
screen.mainloop()
