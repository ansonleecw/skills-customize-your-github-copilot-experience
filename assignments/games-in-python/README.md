# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game in Python that uses strings, loops, conditionals, and user input. You will implement the game logic, manage game state, and provide clear user feedback.

## 📝 Tasks

### 🛠️ Core Hangman Game

#### Description
Implement the playable Hangman game that runs in the terminal. The program should choose a hidden word, accept letter guesses, show progress, and end with a win or lose message.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list in the script.
- Prompt the player to guess a single letter each turn.
- Display the current progress using underscores and revealed letters (e.g., _ a _ _ n).
- Track and display the number of incorrect guesses remaining (suggested: 6 attempts).
- Prevent repeated guesses from reducing remaining attempts and inform the player when a letter was already guessed.
- End the game when the word is fully guessed or when attempts are exhausted, showing a clear win or lose message.

Example gameplay snippet:

```text
Secret word: _ a _ _ n
Guess a letter: g
Incorrect. Attempts remaining: 5
Guess a letter: h
Correct! _ a _ _ n
Guess a letter: n
Correct! _ a _ n
...
You win! The word was 'hangn'
```

### 🛠️ Optional Enhancements and Quality

#### Description
Add one or more enhancements to improve usability, robustness, or replayability. Write clean, commented code and include instructions to run the program.

#### Requirements
Completed program should:

- Implement at least one enhancement such as:
  - Difficulty levels that change the allowed attempts or word list.
  - Loading words from an external file (words.txt) instead of an in-script list.
  - ASCII-art hangman that progresses with incorrect guesses.
  - A simple high-score or stats file tracking wins/losses (optional).
- Include clear instructions in a top-of-file docstring or comment on how to run the game (e.g., python3 hangman.py).
- Provide basic input validation (ignore non-letter or multi-character inputs) and handle EOF/interrupts gracefully.
- Add inline comments and meaningful function/variable names for readability.

```text
Run:
$ python3 hangman.py
```
