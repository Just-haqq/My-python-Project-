import random 

user_name = input("WHat is your name please? ")
print(f"Welcome{user_name}, Goodluck! ")
words = ["car", "bicycle", "orange", "pawpaw", "rainbow", "fanta", "Broom", "Mother", "Envelope", "Bowl"]
word = random.choice(words)
print("Guess the character ")

turns = 7
guesses = ''
while turns > 0:
    failed = 0 
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_")
            failed = failed + 1
    if failed == 0:
        print("You win ")
        print(f"The word is: {word}")
        break
    guess = input("guess a character: " )
    guesses += guess
    if guess not in word:
        turns = turns - 1
        print("Wrong")
        print(f"You have {turns} more guesses")
        if turns == 0:
            print("You loose ")