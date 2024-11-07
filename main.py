from os import error
from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
import time


class Logic:

  def __init__(self, root, WrongGuesses):
    wordfile = open("words.txt", "r")
    wordlist = wordfile.readlines()
    word = wordlist[random.randrange(0, len(wordlist))]
    #print(word)
    #print(len(word.strip("\n")))
    self.word = word.strip("\n")
    print(self.word)
    self.guessed = "_" * (len(word) - 1)
    self.root = root
    self.wrong = "Incorrect Guesses: "
    self.WrongGuesses = WrongGuesses
    self.numberincorrect = 0

  def passthrough(self, guesslabel):
    self.guesslabel = guesslabel
    self.config(self.guessed)

  def canvaspassthrough(self, canvas):
    self.canvas = canvas

  def closure(self):
    self.close = True

  def guess(self, guess, entry):
    entry.delete(0, END)
    guessed = "".join(self.guessed)
    #print(guessed)
    guesslbl = self.guesslabel
    #print("Attempting edit")
    word = self.word
    if guess == None or guess == "":
      pass
    if guess == word:
      guessed = word
      self.config(text=guessed)
      self.win()
    elif len(guess) == 1 and guess[0] in list(word):
      #print("1")
      count = 0
      for letter in word:
        count += 1
        #print(count - 1)
        if letter == guess:
          guessed = list(guessed)
          guessed[count - 1] = guess
      guessed = "".join(guessed)
      #print(guessed)
    elif (len(guess) == 1 and guess[0] not in list(word)) or (len(guess) > 1):
      self.incorrectguess(guess)
    if "".join(guessed) == word:
      guessed = word
      self.config(text=guessed)
      self.win()
    #print(list("".join(guessed)))
    #print(list(word))
    self.guessed = guessed
    self.config(text=guessed)

  def win(self):
    result = messagebox.askquestion(title="You won!", message="Play again?")
    if result == "yes" or result == "YES":  #I do not yet know the output format
      restart(self.root)
    else:
      time.sleep(0.5)
      exit()

  def loss(self):
    result = messagebox.askquestion(title="Game over.",
                                    message="You lost. The word was: " +
                                    self.word + "\n Play again?")
    if result == "yes" or result == "YES":  #I do not yet know the output format
      restart(self.root)
    else:
      time.sleep(0.1)
      exit()

  def incorrectguess(self, guess):
    #print("wrong")
    #if (len(self.wrong) % 25) < 3:
    #self.wrong += "\n"
    self.wrong += guess + " "
    self.WrongGuesses.config(text=self.wrong)
    self.numberincorrect += 1
    numberincorrect = self.numberincorrect
    canvas = self.canvas
    if numberincorrect == 1:  #Bottom
      canvas.create_line(75, 250, 300, 250)
    elif numberincorrect == 2:  #Side
      canvas.create_line(125, 250, 125, 50)
    elif numberincorrect == 3:  #Top
      canvas.create_line(125, 50, 275, 50)
    elif numberincorrect == 4:  #Support Beam
      canvas.create_line(125, 75, 150, 50)
    elif numberincorrect == 5:  #Rope
      canvas.create_line(250, 50, 250, 75)
    elif numberincorrect == 6:  #Head
      canvas.create_oval(230, 75, 270, 115)
    elif numberincorrect == 7:  #Body
      canvas.create_line(250, 115, 250, 175)
    elif numberincorrect == 8:  #Arm L
      canvas.create_line(250, 140, 225, 150)
    elif numberincorrect == 9:  #Arm R
      canvas.create_line(250, 140, 275, 150)
    elif numberincorrect == 10:  #Leg L
      canvas.create_line(250, 175, 225, 200)
    elif numberincorrect == 11:  #Leg R
      canvas.create_line(250, 175, 275, 200)
      time.sleep(0.1)
      self.loss()

  def config(self, text):
    guesslabel = self.guesslabel
    textlist = list(text)
    output = " ".join(textlist)
    guesslabel.config(text=output)


def restart(root):
  root.destroy()


while True:
  root = Tk()
  root.title("Hangman")

  content = ttk.Frame(root)
  root.resizable(False, False)

  frame = Canvas(content, borderwidth=5, relief="ridge", width=500, height=300)
  WrongGuesses = ttk.Label(content, text="Incorrect guesses: ", wraplength=150)
  LogicObject = Logic(root, WrongGuesses)
  guesslbl = ttk.Label(content, text=LogicObject.guessed)
  LogicObject.passthrough(guesslbl)

  entry = ttk.Entry(content)
  GuessButton = ttk.Button(
      content,
      text="Guess",
      command=lambda: LogicObject.guess(entry.get(), entry))
  NewGame = ttk.Button(content, text="New Game", command=lambda: restart(root))

  content.grid(column=0, row=0)
  frame.grid(column=0, row=0, columnspan=3, rowspan=3)
  guesslbl.grid(column=3, row=0, columnspan=2)
  entry.grid(column=3, row=2, columnspan=2)
  GuessButton.grid(column=3, row=4)
  NewGame.grid(column=4, row=4)
  WrongGuesses.grid(column=3, row=1, columnspan=2)

  LogicObject.canvaspassthrough(frame)

  root.protocol("WM_DELETE_WINDOW", exit)
  root.mainloop()
