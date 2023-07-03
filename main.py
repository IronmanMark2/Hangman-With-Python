import random

def play_hangman():
    my_file = open("words.txt")
    data = my_file.read()
    my_file.close()

    words = data.split('\n')[:-1]
    randomword = random.choice(words)

    count = len(randomword)
    display = ["_"] * count
    print(display)

    max_attempts = 7  # Maximum number of incorrect guesses
    attempts = 0  # Counter for incorrect guesses

    hangman_stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========="""
    ]

    while attempts < max_attempts and "_" in display:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in display:
            print("You've already guessed that letter.")
            continue

        correct_guess = False
        for i, letter in enumerate(randomword):
            if letter == guess:
                display[i] = letter
                correct_guess = True

        if correct_guess:
            print("Correct guess!")
        else:
            attempts += 1
            print("Wrong guess! Attempts remaining:", max_attempts - attempts)
            print(hangman_stages[attempts - 1])  # Print hangman stage

        print(display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", randomword)
    else:
        print("Sorry, you ran out of attempts. The word was:", randomword)

    play_again = ""
    while play_again not in ["yes", "no"]:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "no"]:
            print("Wrong input. Please enter 'yes' or 'no'.")

    if play_again == "yes":
        play_hangman()
    else:
        print("Goodbye!")

play_hangman()
