import time
import random
import copy

# Intro
print("Hello!")
time.sleep(1)
print("I am a guessing game with numbers :)")

time.sleep(1.33333)
print("Call me... Dan's guessing game V1")
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

time.sleep(0.3)
print("Boooo! Is the ghost of debugging! Close your eyes!")
time.sleep(1)
print("DEBUG DEBUG DEBUG SPOILER: The special number i'm thinking of is..." + str(specialNumber))

for guessesTaken in range(1, 5):
    print("Take a guess: ")

    try:
        guess = int(input())
    except ValueError:
        print("Your guess should be a number!")
        time.sleep(0.5)
        print("Try again.")
        try:
            guess = int(input())
        except ValueError:
            print("Your guess should be a number!")
            time.sleep(0.5)
            print("Try again. Last chance before I shutdown")
        else:
            print("Processing guess. Beep-Boop...")
    else:
        print("Processing guess. Beep-Boop...")

    if guess < specialNumber:
        print("Oops, that's not the number I was thinking about! Mine is a bit bigger")
    elif guess > specialNumber:
        print("Darn, that's bigger than I was thinking. Try again!")
    else:
        break
        # The condition above is for the correct guess
if guess == specialNumber:
    print("Nice. That's my number!")
else:
    print("Sorry, that's not my number. I was thinking of " + str(specialNumber))

# Scoreboard creation
Scoreboard = ["Dan the Creator", str(username)]
Scoreboard.index(username)

print("The users who tried this challenge before are: " + str(Scoreboard) + ". You should be proud of yourself")
print("")
print("SCORE BOARD")

for username in Scoreboard:
    print(str(Scoreboard.index(username)) + ". " + str(username))
