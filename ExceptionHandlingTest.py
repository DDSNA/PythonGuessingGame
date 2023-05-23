import time
import random

# Intro
print("Hello!")
time.sleep(1)
print("I am a guessing game with numbers :)")

time.sleep(1.33333)
print("Call me... Dan's guessing game V1")
time.sleep(1.7)
print("What is your name?")
time.sleep(1)

# Obtain username

print("User`s name:")
time.sleep(1)
username = input()
time.sleep(2)
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

print("Boooo! Is the ghost of debugging! Close your eyes!")
print("DEBUG DEBUG DEBUG SPOILER: The special number i'm thinking of is..." + str(specialNumber))

for guessesTaken in range (1, 5):
    print("Take a guess: ")
    guess = int(input())

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


