import time
import random
import copy

# Intro
print("Hello!")
time.sleep(1)
print("I am a guessing game with numbers :)")

time.sleep(1.33333)
print("Call me... Dan's guessing game V1" + "\n")
time.sleep(1)
print("What is your name?")
time.sleep(1)

# Obtain username

print("User`s name:")
time.sleep(1)
username = input()
time.sleep(1)
print("Ah... so you are " + username)
print("Well met!")

time.sleep(1)
print("Well, " + username + " I am thinking of a number between...")
specialNumber: int = random.randint(1, 40)
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("1 and 40")

# time.sleep(0.3)
# print("Boooo! Is the ghost of debugging! Close your eyes!")
# time.sleep(1)
# print("DEBUG DEBUG DEBUG SPOILER: The special number i'm thinking of is..." + str(specialNumber))
guessesTaken = 0

while guessesTaken < 5:
    print("Take a guess: ")
    #print("DEBUG: Guesses taken: " + str(guessesTaken))

    nonIntegerInput = False
    guessTamperedWith = False

    try:
        guess = int(input())
    except ValueError:
        print("Your guess should be a number!")
        time.sleep(0.5)
        print("Try again.")
        nonIntegerInput = True
        guessesTaken -= 1
        try:
            guess = int(input())
        except ValueError:
            print("Your guess should be a number!")
            time.sleep(0.5)
            print("Typing can be hard, but I believe in you :)")
            guess = 0
            guessTamperedWith = True
            nonIntegerInput = True
            guessesTaken -= 1
        else:
            print("Processing guess. Beep-Boop...")
            time.sleep(0.5)
    else:
        print("Processing guess. Beep-Boop...")
        time.sleep(0.5)
        guessesTaken += 1

    if guessTamperedWith:
        print("Since you missed your chance once, I will assume you flipped a coin and wanted to score '20'")
        guess = 20

    if guess < specialNumber:
        try:
            print("Oops, that's not the number I was thinking about! Mine is a bit bigger")
        except NameError:
            print("You did not input a number yet")

    elif guess > specialNumber:
        print("Darn, that's bigger than I was thinking. Try again!")
    else:
        break
        # The condition above is for the correct guess

# Scoreboard creation
Scoreboard = ["Dan the Creator", str(username)]
Scoreboard.index(username)

# TODO: Create a leaderboard
# TODO: Create a *permanent* leaderboard
# TODO: Create a basic scoring system (maybe -1 for wrong and +5 for right?)

print("The users who tried this challenge before are: " + str(Scoreboard) + ". You should be proud of yourself")
print("")
print("SCORE BOARD")

for username in Scoreboard:
    print(str(Scoreboard.index(username)) + ". " + str(username))
