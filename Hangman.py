import random

wordlist = 'airplane vehicle television speaker computer'.upper().split()
random.shuffle(wordlist)

secret_word = wordlist.pop()
correct = []
incorrect = []

print("DEBUG: %a" % secret_word)

def draw_board():
    #Draw the Gallows (Eventually) as well as display the word.
    for i in secret_word:
        if i in correct:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print("\n\n")
    print("*** MISSED LETTERS ***")
    for i in incorrect:
        print(i, end=' ')
    print('\n***********************')

def user_guess():
    #Allow the user to take a guess. Append that letter to correct or incorrect.
    while True:
        guess = input("Guess a letter\n: ").upper()
        if guess in correct or guess in incorrect:
            print("You have already guessed that letter. Guess again.")
        elif guess.isnumeric():
            print("Please enter only letters, not numbers. Guess again.")
        elif len(guess) > 1:
            print("Please enter only one letter at a time. Guess again.")
        elif len(guess) == 0:
            print("Please enter your selection.")
        else:
            break
    if guess in secret_word:
        correct.append(guess)
    else:
        incorrect.append(guess)

while True:
    draw_board()
    user_guess()
