# Program   : Hangman Dismemberer
# File      : abuhamda_hangman_dismemberer_v1_02.py
# Author    : Abdallah Abuhamda
# Instructor: David Baker
# Course    : CIS156, CGCC
# Date      : 05-02-2023

# Import
from os import system, name
from time import sleep
import os
import platform
import urllib.request
import random
import re

# Classes and Functions

# Victim class for player character
class Victim:
    def __init__(self):
        # Stores victim hitpoints
        self.hp = 10
        # List containing victim body parts
        self.body_parts = ["head", "body", "left_arm", "right_arm", "left_leg",
        "right_leg", "hat", "overcoat", "left_shoe", "right_shoe"]
    
    # Removes body part
    def lose_body_part(self):
        if len(self.body_parts) > 0:
            lost_part = self.body_parts.pop()
            print(f"\nYou lost a {lost_part}!")
            self.hp -= 1
        else:
            print("You have no more body parts to lose.")
    
    # Returns hp
    def get_hp(self):
        return self.hp
    
    # Sets hp
    def set_hp(self, hp):
        self.hp = hp

# Perpetrator class
class Perpetrator:
    def __init__(self):
        # Stores perpetrator insanity points
        self.insanity_points = 0

    # Checks if the user's guess is correct and builds insanity accordingly
    def check_consecutive_correct_guesses(self, correct_guess):
        # Increments insanity when guess is correct
        if correct_guess:
            self.insanity_points += 1
            if self.insanity_points == 3:
                print("\nThe perpetrator has descened into insanity! You may now attempt escape!")
            if self.insanity_points == 4:
                print("\nThe perpetrator has gone completely mad!")
        # Resets insanity when user breaks streak
        else:
            self.insanity_points = 0

    # Returns ip
    def get_ip(self):
        return self.insanity_points
    
    # Sets ip
    def set_ip(self, ip):
        self.insanity_points = ip

import os
import platform         

# For printing various things in larger forms
def print_large_letters(usr_string, indent=0):
    """
    Prints a string of alphabetical characters as large ASCII letters.
    Optionally indents by a user-specified amount.
    """
    
    # Dictionary with ASCII art of each letter
    letters = {
        "A": ["  *  ", " * * ", "*   *", "*****", "*   *"],
        "B": ["**** ", "*   *", "**** ", "*   *", "**** "],
        "C": [" *** ", "*   *", "*    ", "*   *", " *** "],
        "D": ["**** ", "*   *", "*   *", "*   *", "**** "],
        "E": ["*****", "*    ", "*****", "*    ", "*****"],
        "F": ["*****", "*    ", "**** ", "*    ", "*    "],
        "G": [" *** ", "*    ", "* ***", "*   *", " *** "],
        "H": ["*   *", "*   *", "*****", "*   *", "*   *"],
        "I": ["*****", "  *  ", "  *  ", "  *  ", "*****"],
        "J": ["*****", "   * ", "   * ", "*  * ", "***  "],
        "K": ["*   *", "*  * ", "***  ", "*  * ", "*   *"],
        "L": ["*    ", "*    ", "*    ", "*    ", "*****"],
        "M": ["*   *", "** **", "* * *", "*   *", "*   *"],
        "N": ["*   *", "**  *", "* * *", "*  **", "*   *"],
        "O": [" *** ", "*   *", "*   *", "*   *", " *** "],
        "P": ["**** ", "*   *", "**** ", "*    ", "*    "],
        "Q": [" *** ", "*   *", "* * *", "*  **", " ****"],
        "R": ["**** ", "*   *", "**** ", "*  * ", "*   *"],
        "S": [" *** ", "*    ", " *** ", "    *", "***  "],
        "T": ["*****", "  *  ", "  *  ", "  *  ", "  *  "],
        "U": ["*   *", "*   *", "*   *", "*   *", " *** "],
        "V": ["*   *", "*   *", " * * ", " * * ", "  *  "],
        "W": ["*   *", "*   *", "* * *", "** **", "*   *"],
        "X": ["*   *", " * * ", "  *  ", " * * ", "*   *"],
        "Y": ["*   *", " * * ", "  *  ", "  *  ", "  *  "],
        "Z": ["*****", "   * ", "  *  ", " *   ", "*****"],
    }

    # Add indentation spaces
    indent_str = " " * indent
    
    # Print each row of each letter in usr_string using letters dictionary
    for row in range(5):
        print(indent_str, end="")
        for char in usr_string:
            letter = letters.get(char.upper(), ["      ", "      ", "      ", "      ", "      "])
            print(letter[row], end="  ")
        print()


def print_ui(victim, perpetrator, spaced_progress = ""):
    """Prints UI elements"""
    
    # Clear screen
    system('cls' if name == 'nt' else 'clear')
    
    # Branch statements for UI
    if victim.get_hp() == 10:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O    (hat)                      |
|   |      /|\   (overcoat)                 |
|   |      / \   (l/r shoe)        (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 9:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O    (hat)                      |
|   |      /|\   (overcoat)                 |
|   |      / \   (l shoe)          (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 8:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O    (hat)                      |
|   |      /|\   (overcoat)                 |
|   |      / \                     (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 7:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O    (hat)                      |
|   |      /|\                              |
|   |      / \                     (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 6:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O                               |
|   |      /|\                              |
|   |      / \                     (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 5:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O                               |
|   |      /|\                              |
|   |      /                       (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 4:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O                               |
|   |      /|\                              |
|   |                              (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 3:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O                               |
|   |      /|                               |
|   |                              (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 2:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O                               |
|   |       |                               |
|   |                              (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 1:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       O                               |
|   |                                       |
|   |                              (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|                 ___________  |
|___________________________________________|
""")
        
    elif victim.get_hp() == 0:
        print("""
 ___________________________________________
|                                           |
|    _______                                |
|   |       |                               |
|   |       x                               |
|   |      xxx                              |
|   |      x x                     (o)      |
|  _|_                             / \      |
| |   |______                       T       |
| |          |                     / \      |
| |__________|        /\O|/\   ___________  |
|___________________________________________|
""")
    # Prints hp, ip, and word progress
    
    if victim.get_hp() == 10:
        stats_string = f"Victim HP: {victim.get_hp()}/10 Perpetrator IP: {perpetrator.get_ip()}/3"
    else:
        stats_string = f"Victim HP: 0{victim.get_hp()}/10 Perpetrator IP: {perpetrator.get_ip()}/3"
    
    print(f"{stats_string : ^45}")
    print(f"\n{spaced_progress : ^45}\n")

def print_description():
    """Prints game description."""
    print("""
------ Hangman: Dismemberer ------

A thrilling and fully-featured CLI game played as the victim, trying to guess 
the hidden word before the perpetrator dismembers them.

**Instructions:**

- You start with 10 HP, which is directly tied to the number of limbs and 
accessories you have.

- Each incorrect guess results in the perpetrator dismembering a body part or 
taking an accessory, reducing your HP.

- When playing with longer words (> 4 letters):

  - If you guess a letter correctly, the perpetrator gains 1 IP.
  - If you guess three letters consecutively, the perpetrator's IP will reach 
    a critical point, and you'll have the chance to attempt escape.
  - If you choose to take the opportunity and guess one more letter, you can 
    escape and reveal the hidden word to beat the game.
  - But if you guess incorrectly, you'll take critical damage, reducing your HP.

**Survive long enough to guess the hidden word and escape the perpetrator**
""")

# Function for fake loading screen
def loading_dots(seconds, num_dots=3):
    """ Prints specified number of dots at given intervals. """
    for i in range(num_dots):
        sleep(seconds)
        # Print a dot without newline
        print(".", end="", flush=True)
    sleep(seconds)
    
# Function to prompt user before continuing
def prompt_and_clear():
    input("Press enter to continue...")
    system('cls' if name == 'nt' else 'clear')

# Reads words from local document

def choose_word_legacy():
    """Reads list of words from local file. Returns random word from list."""
    
    with open(r"C:\path\to\your\file.txt") as f:
        words = f.read().splitlines()
    return random.choice(words)

# Reads words from online document
def choose_word():
    """Reads list of words from online file. Returns random word from list."""
    
    url = 'https://raw.githubusercontent.com/vibraniumdroid/hangman-dismemberer/main/words.txt'
    with urllib.request.urlopen(url) as response:
        words = response.read().decode().splitlines()
    return random.choice(words)



# Checks guesses and manages victim/perpetrator
def word_guesser(word, word_so_far, guess, guesses, victim, perpetrator):
    """
    Takes a word, the word as guessed so far by the user, a guess, and a list of guesses.
    Also takes victim and perpetrator for gameplay purposes.
    Returns the updated word as guessed so far by the user and
    alters victim HP and perpetrator IP accordingly.

    """

    # Convert word_so_far to list 
    word_so_far_list = list(word_so_far)

    # Create variables to store limb loss and guess accuracy t/f vals
    lose_limb = True
    correct_guess = False
    
    
    if guess[0] not in guesses:
        # Loop through each character in the word
        for i in range(len(word)):
            # if the character matches the guess, replace the underscore with the guess
            if word[i] == guess[0]:
                word_so_far_list[i] = guess[0]
                lose_limb = False
                correct_guess = True
    
    # Dismember victim when guess is incorrect
    if lose_limb:
        victim.lose_body_part()
    
    # Update perpetrator insanity for appropriately sized words
    if len(word) > 4:
        perpetrator.check_consecutive_correct_guesses(correct_guess)
    
    # convert the modified list back to a string and return it
    return ''.join(word_so_far_list)

# main
def main():
    # Enables debugging options when true
    debug_game = False
    
    # Counter for outer loop
    outer_loop_count = 0
    
    try:
    
        while (True):
            # Creates a victim and a perpetrator
            victim = Victim()
            perpetrator = Perpetrator()
                   
            # Set word 
            word = choose_word()
                    
            # Set word so far
            word_so_far = "_" * len(word)
                    
            # A list to contain user guesses
            guesses = []
                    
            # Sets variables for game status
            game_passed = False
            game_escaped = False
                    
            # Loop counter variable (internal use)
            loop_count = 0
            
            # Introduces game on first run
            if outer_loop_count == 0:    
                # Welcomes user
                print_large_letters("Hangman", 14)
                print("\n")
                print_large_letters("Dismemberer")
                print("")
            # Labels menu as "Menu" on subsequent runs
            else:
                print_large_letters("Menu", 2)
                print("")
                
            # Presents list of options and collects input
            print("[1] Play Hangman: Dismemberer")
            print("[2] About Hangman: Dismemberer")
            print("[3] Debugging options")
            print("[0] Quit game")

            menu_val = input("Please select an option [0-3]: ")
                
            # Convert user input to int if digit is detected
            if menu_val.isdigit():
                menu_val = int(menu_val)
                
            match menu_val:
                case 0:
                    print("Goodbye")
                    break
                case 1:
                    # Debugging purposes
                    if debug_game:
                        print(f"\nThe word is \"{word}\". Revealed for debugging and demonstration purposes only.")
                    
                    # Fake loading screen
                    print("Loading game", end="", flush=True)
                    loading_dots(0.85)
                        
                    while word not in word_so_far:
                        try:
                            # Branch statements for escape options
                            if perpetrator.get_ip() == 3:
                                usr_val = input("Attempt escape? [Yes/No]: ")
                                if re.search("Yes|yes|Y|y", usr_val):
                                    print("Attempting escape!")
                                        
                                    # Collect user input for guess
                                    guess = input("Enter a correct guess to escape: ")
                                    
                                    # Pass to word_guesser function and update word so far
                                    word_so_far = (word_guesser(word, word_so_far, guess, guesses, victim, perpetrator))
                                    
                                    # Checks word status and acts accordingly
                                    if word in word_so_far:
                                        game_passed = True
                                        break
                                          
                                    # Append guess value to guesses list
                                    guesses.append(guess)
                                    
                                    # Branch statement to manage successful/failed escapes
                                    if perpetrator.get_ip() == 4:
                                        print("You escaped!")
                                        game_escaped = True
                                        break
                                    else:
                                        print("\nYour escape failed!")
                                        print("The perpetrator goes after you with a chainsaw!")
                                        print("You recieve critical damage!")
                                        victim.lose_body_part()
                                        victim.lose_body_part()
                                # Continues game if user opts against trying to escape
                                elif re.search("No|no|N|n", usr_val):
                                    print("The perpetrator has recovered! Proceeding normally...")
                                    perpetrator.set_ip(0)
                                # Continues game if user fails to enter valid input
                                else:
                                    print("Valid input not detected! Proceeding normally...")
                                    perpetrator.set_ip(0)
                            
                            # Prints UI on first loop iteration before guess
                            if loop_count == 0:
                                print_ui(victim, perpetrator, word_so_far)
                        
                            # Collect user input for guess
                            guess = input("\nEnter a guess: ")
                            
                            # Allows user to terminate game at any point by entering "0"
                            if guess[0] == "0":
                                print("Game terminated")
                                break
                            
                            if bool(re.search(r'[^a-zA-Z]', guess)):
                                raise ValueError("Uh oh... That's not a letter")
                            
                            # Pass to word_guesser function and update word so far
                            word_so_far = (word_guesser(word, word_so_far, guess, guesses, victim, perpetrator))
                            
                            if guess[0] in guesses:
                                print("\nUh oh... You've already guessed that.\n")
                            
                            # Append guess value to guesses list
                            guesses.append(guess)
                            
                            # For formatted contents of word_so_far
                            spaced_progress = ""
                            
                            # Split up word_so_far to print with formatting
                            for char in word_so_far:
                                spaced_progress += char + " "
                            
                            # Prints UI after short delay
                            sleep(2.2)
                            print_ui(victim, perpetrator, spaced_progress)
                            
                            if word in word_so_far:
                                game_passed = True
                                break
                            
                            # Breaks loop on death
                            if victim.get_hp() == 0:
                                break
                            
                            # Increment loop counter variable
                            loop_count += 1
                        
                        except ValueError as badinput:
                            print(badinput)
                            sleep(1.35)
                            
                        except KeyboardInterrupt:
                            print("\nYou entered \"CTRL-C\"! You may also enter enter 0 to terminate the game loop.")
                            sleep (1.35)
                            break
                           
                        except:
                            print("Error! Invalid input.")
                            sleep (1.35)
                    
                    # Branch statement to deal with different game outcomes
                    if game_passed:
                        print("You beat the game by guessing the word!\n")
                    elif game_escaped:
                        print("You beat the game by escaping!")
                        print(f"The word was \"{word}\"\n")
                    else:
                        print("You died!")
                        print(f"The word was \"{word}\"\n")
                    prompt_and_clear()
                    
                    
                case 2:
                    # Clear screen
                    system('cls' if name == 'nt' else 'clear')
                    # Prints game desc.
                    print_description()
                    prompt_and_clear()
                    
                case 3:
                    # Exits program
                    sub_menu3 = input("\nEnable debugging options? [Yes/No]: ")
                    
                    if re.search("Yes|yes|Y|y", sub_menu3):
                        debug_game = True
                        print("Enabling debugging options", end = "", flush = True)
                        loading_dots(0.5)
                        print("\nDebugging options enabled!\n")
                        
                    elif re.search("No|no|N|n", sub_menu3):
                        debug_game = False
                        print("Resetting debugging options", end = "", flush = True)
                        loading_dots(0.5)
                        print("\nDebugging options set to default!\n")
                    else:
                        print("Input not recognized! Proceeding as is", end = "", flush = True)
                        loading_dots(0.5)
                        print("\n")
                    prompt_and_clear()
                    
                case _:
                    # Reminds user to enter valid input
                    print("\nError! Please enter valid, numeric input (0-3)\n")
            # Increment outer loop
            outer_loop_count += 1    
    
    except KeyboardInterrupt:
        print("\nYou entered \"CTRL-C\"! Program terminated.")
            
    except:
        print("\nUnknown error! Program terminated.\n")
        
    


# call main
if __name__ == '__main__':
    main()
    


"""
** Changelog **

1_00:
    -Initial release

1_01:
    -Added support for online files
    -Set default .txt words list to an online file
    
1_02:
    -Improved error checking with try... except
    
    -Improved UI with prompt_and_clear() function
     Now prompts user to press enter and then clears screen
    
    -Added/changed menu options
        -Added debugging menu
        -Changed "Quit game" option to 0
        
    -Reworked bug where escape opportunities would be offered on shorter
     completed or nearly completed words. Insanity now only builds on words
     with > 4 characters.
     
    -Added fake loading screens with loading_dots() for better continuity
     
    -Added print_large_letters for better game introduction and menu label
    
     
     
     


"""
