import random
def main():
    min = 0
    max = 100
    randomInt = random.randrange(min, max)
    numOfGuessesLeft = 10
    guess = None
    print("The guessing range is between " + str(min) + " and " + str(max))
    print(f"You have {numOfGuessesLeft} guesses to win this game")
    while True:
        try:
            if numOfGuessesLeft > 0:
                guess = int(input("Enter your Guess: "))
                if guess < randomInt:
                    numOfGuessesLeft -= 1
                    print(f"Too Low\nYou have {numOfGuessesLeft} guesses left")
                    continue
                elif guess > randomInt:
                    numOfGuessesLeft -= 1
                    print(f"Too High\nYou have {numOfGuessesLeft} guesses left")
                    continue
                else:
                    numOfGuessesLeft -= 1
                    print(f"Game Won\nThe number was {randomInt}\nNumof Guesses Left: {numOfGuessesLeft}")
                    break
            if numOfGuessesLeft == 0:
                print("Game over. No guesses left")
        except ValueError:
            print("Wrong input!!!\nNumbers only.")
            continue
if __name__ == "__main__":
    main()