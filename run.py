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
    pass

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

    