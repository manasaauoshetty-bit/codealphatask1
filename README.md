# codealphatask1
A Python implementation of the classic Hangman Game. This task demonstrates the use of core programming concepts including random modules, while loops, and string/list manipulation. Developed for the CodeAlpha internship program.
# CodeAlpha_Hangman_Game

## 📌 Project Overview
This project is a text-based **Hangman Game** developed as part of my Python Programming internship at **CodeAlpha**. The goal of the project is to create an interactive console application where a player tries to guess a hidden word by suggesting letters within a limited number of attempts.

## 🎮 How to Play
1. The computer randomly selects a secret word from a predefined list.
2. The player is shown underscores `_` representing the letters of the hidden word.
3. The player enters a letter to guess:
   - If the letter is in the word, it reveals its position.
   - If the letter is incorrect, the player loses one of their **6 lives**.
4. The game ends when:
   - The player guesses all letters correctly (**Win**).
   - The player runs out of lives (**Loss**).

## 🚀 Features
- **Random Word Selection**: Uses the `random` module to pick words from a list of 5 predefined terms.
- **Input Validation**: Ensures the user inputs valid single letters.
- **Attempt Tracking**: Tracks and displays the number of remaining lives.
- **Game State Updates**: Real-time feedback on correct/incorrect guesses and the current state of the hidden word.

## 🛠️ Key Concepts Used
- **Modules**: `random` for choosing words.
- **Loops**: `while` loops for the game engine.
- **Conditionals**: `if-elif-else` for game logic and win/loss conditions.
- **Data Structures**: Lists and Strings to store word data and user progress.

