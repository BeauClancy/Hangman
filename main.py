# Imports
import random  # Randomly choose an item from a list []
import time

# Welcome message and user registration
print("\nWelcome to the Hangman game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)  # Halt program execution for set time

# Countdown
print("The game is about to start!\n Let's play Hangman!")
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("Let's go!")
time.sleep(1)


# Main function for argument initialisation
# with the parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["music", "image", "film", "promise", "kids", "lungs", "cat", "rhyme", "plants"]
    word = random.choice(words_to_guess)
    length = len(word)  # Length helps us to get the length of the string.
    count = 0  # Count is initialized to zero and would increment in the further code
    display = '_' * length
    already_guessed = []
    play_game = ""


# A loop to re-execute the game when the first round ends:
def loosing_play_loop():
    global play_game
    play_game = input("Are you for redeeming yourself? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Come on, play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Your loss! But thanks for playing the game of the hanging man! We definitely expect you back again!")
        exit()


# Initializing all the conditions required for this game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 6
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Muhaha. Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Oh no! Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Dangerous! Another wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Tough luck! Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "__|__\n")
            print("You're cutting it close! Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("I'm sorry, but I warned you. You are hanged!!!\n")
            print("The missing letters were:", word + " You correctly guessed:", already_guessed)
            loosing_play_loop()

    if word == '_' * length:
        print("Woop woop! You guessed the word and you may live! Off you go!")
        exit()

    elif count != limit:
        hangman()


main()

hangman()
