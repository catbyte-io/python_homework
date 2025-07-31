# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        result = ""
        nonlocal guesses
        guesses.append(letter)
        # Enumerate through each letter in the secret
        for i, s_letter in enumerate(secret_word):
            # Check if that letter was guessed
            if s_letter in guesses:
                # If guessed, append to result
                result += s_letter
            else:
                # If not guessed, append underscore
                result += "_"
        print(result)

        if "_" not in result:
            return True
        else:
            return False

    return hangman_closure


# Design hangman game
secret = "secretword"
game = make_hangman(secret)

# Continually ask for a letter
while True:
    letter = input("Guess a letter: ")

    # Break if all letters are guessed
    if game(letter):
        break
