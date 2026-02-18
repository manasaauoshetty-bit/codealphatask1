import random

def choose_word():
    words = ["python", "banana", "secret", "guitar", "cherry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect and set(word) != set(guessed_letters):
        print("\n" + display_word(word, guessed_letters))
        print(f"Guessed letters: {' '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        if guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Oops! Wrong guess.")
            guessed_letters.append(guess)
            incorrect_guesses += 1

    if set(word) == set([c for c in guessed_letters if c in word]):
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()