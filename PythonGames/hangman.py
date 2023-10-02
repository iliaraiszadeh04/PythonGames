import random

# List of words for the game
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

# Select a random word from the list
word_to_guess = random.choice(words)
guessed_word = ['_'] * len(word_to_guess)
attempts = 6

while attempts > 0 and '_' in guessed_word:
    # Display the current state of the word
    print(' '.join(guessed_word))
    
    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue
    
    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")
        
if '_' not in guessed_word:
    print("Congratulations! You guessed the word: " + ''.join(guessed_word))
else:
    print("Out of attempts. The word was: " + word_to_guess)