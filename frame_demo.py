from tkinter import *
import random

# Create the main window
root = Tk()
root.geometry("800x600")  # Set the window size to 800x600 pixels
root.title("Game Center")

################################# ROOT CODE ####################################################
'''MODEL'''


landing_frame = Frame(root, bg="teal")
hangman_frame = Frame(root, bg="teal")
demo_frame = Frame(root, bg="light blue")

# Place all frames in same position
for frame in [landing_frame, hangman_frame, demo_frame]:
    frame.place(x=0, y=0, width=800, height=600)


def raise_frame(frame):
    frame.tkraise()


words = open("Tkinter---Frame-Notes-and-Demo-main\wordbank.txt", "r")
wordbank = words.read().split()

images = []
for i in range(1, 8):
    images.append(PhotoImage(file=f"Tkinter---Frame-Notes-and-Demo-main\images\{i}.png"))

secret_word = ""
guessed_letters = set()
incorrect_guesses = 0
game_over = False

def hangman_new_game():
    global secret_word, guessed_letters, incorrect_guesses, game_over
    secret_word = random.choice(wordbank).upper()
    guessed_letters = set()
    incorrect_guesses = 0
    game_over = False
    hangman_image.config(image=images[0])
    message_label.config(text="Guess a letter or word!")
    dashes_label.config(text=" ".join("_" for _ in secret_word))
    guess_entry.delete(0, END)
    for button in letter_buttons:
        button.config(state=NORMAL, bg="SystemButtonFace")

def hangman_process_guess():
    global incorrect_guesses, game_over
    if game_over: return
    
    guess = guess_entry.get().upper()
    guess_entry.delete(0, END)
    
    if not guess: return
    
    if len(guess) > 1:
        if guess == secret_word:
            dashes_label.config(text=" ".join(secret_word))
            message_label.config(text="You win! The word was " + secret_word)
            game_over = True
        else:
            incorrect_guesses += 1
            hangman_image.config(image=images[incorrect_guesses])
            if incorrect_guesses >= 6:
                message_label.config(text=f"Game over! The word was {secret_word}")
                dashes_label.config(text=" ".join(secret_word))
                game_over = True
        return
    
    letter = guess[0]
    if letter in guessed_letters: return
    
    guessed_letters.add(letter)
    for button in letter_buttons:
        if button["text"] == letter:
            button.config(state=DISABLED, bg="light gray")
            break
    
    if letter in secret_word:
        dashes_label.config(text=" ".join(letter if letter in guessed_letters else "_" for letter in secret_word))
        if all(letter in guessed_letters for letter in secret_word):
            message_label.config(text="You win! The word was " + secret_word)
            game_over = True
    else:
        incorrect_guesses += 1
        hangman_image.config(image=images[incorrect_guesses])
        if incorrect_guesses >= 6:
            message_label.config(text=f"Game over! The word was {secret_word}")
            dashes_label.config(text=" ".join(secret_word))
            game_over = True

################################# LANDING PAGE #################################################
'''MODEL'''


'''CONTROLLER'''
# Create buttons that switch to different frames
hangman_button = Button(
    landing_frame,
    text="HANGMAN", fg="white", bg="teal", font=("Arial", 30),
    command=lambda: [raise_frame(hangman_frame), hangman_new_game()])
hangman_button.place(x=150, y=375, width=200, height=50)

demo_button = Button(
    landing_frame,
    text="DEMO", fg="white", bg="teal", font=("Arial", 30),
    command=lambda: raise_frame(demo_frame))
demo_button.place(x=450, y=375, width=200, height=50)

'''VIEW'''
# Add a title label to the landing frame
landingpage_title = Label(landing_frame, text="Game Center", fg="white", bg="teal", font=("Arial", 30))
landingpage_title.place(x=200, y=20, width=400, height=50)

################################# HANGMAN PAGE #################################################
'''MODEL'''
# Game logic is handled in the root code section

'''CONTROLLER'''
# Home button to return to the landing page
home_button = Button(hangman_frame, text="HOME", fg="white", bg="teal", font=("Arial", 20), command=lambda: raise_frame(landing_frame))
home_button.place(x=300, y=530, width=200, height=50)

'''VIEW'''
# Hangman game widgets
title_label = Label(hangman_frame, text="Hangman", font=("Arial", 30), fg="white", bg="teal")
title_label.place(x=200, y=20, width=400, height=50)

hangman_image = Label(hangman_frame, image=images[0], bg="teal")
hangman_image.place(x=250, y=100, width=300, height=200)

message_label = Label(hangman_frame, text="Guess a letter or word!", font=("Arial", 14), fg="white", bg="teal")
message_label.place(x=200, y=320, width=400, height=30)

dashes_label = Label(hangman_frame, text="", font=("Arial", 18), fg="white", bg="teal")
dashes_label.place(x=200, y=360, width=400, height=30)

letter_buttons = []
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    btn = Button(hangman_frame, text=letter, font=("Arial", 12), width=3, height=1,
                 command=lambda l=letter: [guess_entry.delete(0, END), guess_entry.insert(0, l), hangman_process_guess()])
    btn.place(x=100 + (i%9)*70, y=400 + (i//9)*40, width=50, height=30)
    letter_buttons.append(btn)

guess_entry = Entry(hangman_frame, font=("Arial", 12), width=20)
guess_entry.place(x=300, y=480, width=200, height=30)

submit_button = Button(hangman_frame, text="Submit", font=("Arial", 12), command=hangman_process_guess)
submit_button.place(x=300, y=520, width=200, height=30)

################################# DEMO PAGE #################################################
'''MODEL'''
class Player:
    def __init__(self, up_key, right_key, down_key, left_key, outline):
        self.x = 20
        self.y = 20
        self.radius = 20

        self.square = canvas.create_rectangle(self.x - self.radius, self.)
        root.bind(up_key, self.up)
        root.bind(down_key, self.down)
        root.bind(right_key, self.right)
        root.bind(left_key, self.left)


def up(self):
    canvas.move(self.square, 0, 10)
    

'''CONTROLLER'''
# Home button to return to the landing page
home_button = Button(demo_frame, text="HOME", fg="white", bg="light blue", font=("Arial", 30), command=lambda: raise_frame(landing_frame))
home_button.place(x=300, y=530, width=200, height=50)

'''VIEW'''
# Title label for the demo page
demo_title = Label(demo_frame, text="Demo Game", fg="white", bg="light blue", font=("Arial", 30))
demo_title.place(x=200, y=20, width=400, height=50)

# Start by showing the landing page
raise_frame(landing_frame)

balls = []
for i in range(10):
    balls.append(ball())

# Keep the window open and running
root.mainloop()
