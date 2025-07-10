from tkinter import *
import random, pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Create New Flash Cards ------------------------------- #
try:
    french_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("data/french_words.csv")
data = french_words.to_dict(orient="records")
randomized_word ={}

def next_card():
    global randomized_word, flip_timer
    window.after_cancel(flip_timer)
    randomized_word = random.choice(data)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=randomized_word["French"], fill="black")
    canvas.itemconfig(card_background_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background_img, image=back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=randomized_word["English"], fill="white")


def known_word():
    next_card()
    data.remove(randomized_word)
    new_to_learn = pandas.DataFrame(data)
    new_to_learn.to_csv("data/words_to_learn.csv", index=False)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
#Flash cad front and back image
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

#Create flash card image on canvas
card_background_img = canvas.create_image(400, 263, image=front_img)

#Words on flash card
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_word)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()