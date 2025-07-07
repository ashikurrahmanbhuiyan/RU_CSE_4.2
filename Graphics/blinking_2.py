import tkinter as tk
import random

# Constants
WIDTH = 800
HEIGHT = 600
NUM_STARS = 100
STAR_COLORS = ["white", "yellow", "lightblue", "pink", "lightgreen", "violet"]

# Create the window
root = tk.Tk()
root.title("Twinkling Stars in Night Sky")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Store star references
stars = []

# Create stars at random positions
for _ in range(NUM_STARS):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = random.randint(1, 3)
    color = random.choice(STAR_COLORS)
    star = canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=color)
    stars.append((star, x, y, r))

# Animation loop
def twinkle():
    for i, (star, x, y, r) in enumerate(stars):
        # Random chance to twinkle
        if random.random() < 0.3:
            new_color = random.choice(STAR_COLORS + ["black"])  # black = disappear
            new_r = random.randint(1, 4)
            canvas.coords(star, x - new_r, y - new_r, x + new_r, y + new_r)
            canvas.itemconfig(star, fill=new_color, outline=new_color)
    root.after(100, twinkle)

twinkle()  # Start animation
root.mainloop()
