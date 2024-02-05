import random

# List of words to choose from
words = [
    'apple',
    'banana',
    'cherry',
    'date',
    'elderberry',
    'fig',
    'grape',
    'honeydew'
]

# Function to choose a random word

def choose_word(words):
    return random.choice(words)

# Function to display the current state of the word

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

# Function to play the game

def play_hangman():
    word = choose_word(words)
    guessed_letters = []
    attempts = 6
    print('Welcome to Hangman! Try to guess the word.')
    while True:
        print(display_word(word, guessed_letters))
        if '_' not in display_word(word, guessed_letters):
            print('Congratulations! You guessed the word:', word)
            break
        if attempts == 0:
            print('Sorry, you ran out of attempts. The word was:', word)
            break
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue
        if guess in guessed_letters:
            print('You already guessed that letter.')
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print('Incorrect! You have', attempts, 'attempts left.')
    print('Game over.')