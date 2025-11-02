# ------------------------------------------------------ EL PYTHONCITO XD 🐍🐍🐍🐍!!!!
from tkinter import *
import pandas as pd
from random import choice

BG_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ************************************************************************ FUNCTIONS
def next_card():
    """This function displays a new French word and prepares automatic rotation."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(title_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """This function turn the card over and show the translation."""
    global current_card
    english_word = current_card["English"]

    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=english_word, fill="white")


def is_known():
    """This function mark a word as known, remove it from learning, and move on to the next."""
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)

    next_card()


# ************************************************************************ GUI
window = Tk()
window.title("Flash Card APP")
window.geometry("+300+25")
window.config(bg=BG_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)
# ------------- Canvas
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

title_canvas = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# ------------- Buttons
wrong_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
known_btn = Button(image=right_img, highlightthickness=0, command=is_known)
known_btn.grid(column=1, row=1)

next_card()

# --------------------------------
window.mainloop()
