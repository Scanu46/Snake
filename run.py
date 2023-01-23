from tkinter import *
import random 

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 60
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#B9QEQA"
FOOD_COLOR = "#008000"
BACKGROUND_COLOR = "2D2364"

class Sn:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class obj:
    pass

def turn():
    pass

def direct():
    pass

def colis():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 45))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: direct('left'))
window.bind('<Right>', lambda event: direct('right'))
window.bind('<Up>', lambda event: direct('up'))
window.bind('<Down>', lambda event: direct('down'))

snake = Sn()
food = obj()

turn(snake, food)

window.mainloop()



    