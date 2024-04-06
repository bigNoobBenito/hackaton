import random
import time

WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
word = random.choice(WORDS)
correct = word
test = ""
while word:
    position = random.randrange(len(word))
    test += word[position]
    word = word[:position] + word[(position + 1):]
print(
"""
      Welcome to WORD JUMBLE!!!

      Unscramble the leters to make a word.
      (press the enter key at prompt to quit)
      """
      )
print("The jumble is:", test)
tic = time.perf_counter()
guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it, you guessed it!\n")
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
print("Thanks for playing")
