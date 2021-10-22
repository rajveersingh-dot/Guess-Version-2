# Imports
from breezypythongui import W, EasyFrame
import random


class GuessingGame(EasyFrame):
    # Innit method defined
    def __init__(self):
        """
        Converts an input of string to uppercase and display the results.
        """
        EasyFrame.__init__(self)
        self.setSize(400, 200)
        self.setTitle("Guess Number")
        self.setResizable("true")

        # Variables
        self.random_int = random.randrange(1, 100)
        self.num_of_guesses = 0
        self.hi_score = 90909
        try:
            readf = open('HISCORES.txt', 'r')
            getscr = readf.readline()
        except FileNotFoundError:
            readf = open('HISCORES.txt', 'w')
            getscr = ""
        
        readf.close()
        if getscr != "":
            self.hi_score = int(getscr)

        #rules

        # Inputs
        self.addLabel(text="Guess", row=2, column=0, sticky="E")
        self.userGuess = self.addIntegerField(value=0, row=2, column=1, sticky="W")

        # Command
        self.guessButton = self.addButton(text="Ok", row=3, column=0, columnspan=2, command=self.guess)
        self.resetButton = self.addButton(text="Play Again", row=6, column=0, columnspan=2, state="disabled", command=self.play)

        # Output
        self.resultLabel = self.addLabel(text="Take a guess", row=4, column=0, columnspan=2, foreground="black", sticky="NSEW")
        self.guessleftlabel = self.addLabel(text=f"Guesses: {self.num_of_guesses}", row=5, column=1)
        if self.hi_score == 90909:
            self.hiscorelabel = self.addLabel(text=f"Hi-Score: not yet decided", row=5,column=0)
        else:
            self.hiscorelabel = self.addLabel(text=f"Hi-Score: {self.hi_score}", row=5, column=0)

    def play(self):
        self.num_of_guesses = 0
        self.resultLabel["text"] = "Take a guess"
        self.resultLabel["foreground"] = "black"
        self.random_int = random.randrange(1, 101)
        self.guessButton["state"] = "normal"
        self.userGuess["state"] = "normal"
        self.resetButton["state"] = "disabled"



def main():
    GuessingGame().mainloop()


if __name__ == '__main__':
    main()
