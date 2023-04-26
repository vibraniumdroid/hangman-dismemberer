# Program   : Hangman: Dismemberer
# File      : abuhamda_hangman_dismemberer_v1_01.py
# Author    : Abdallah Abuhamda
# Instructor: David Baker
# Course    : CIS156, CGCC
# Date      : 04-25-2023

# Import
from os import system, name
from time import sleep
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

  * * *

  A thrilling and fully featured CLI-based game played as the victim, a captive desperately
  trying to guess the hidden word before the perpetrator dismembers them.

  **Instructions:**

  * You start with 10 HP, which is directly tied to the number of limbs and accessories you have.
  
  * Each time you guess a letter incorrectly, the perpetrator will dismember a body part or take an accessory from you, reducing your HP.
  
  * If you guess a letter correctly, the perpetrator gains 1 IP (insanity point).
  
  * If you manage to guess three consecutive letters correctly, the perpetrator's IP will reach a critical point,
    and you'll be presented with the opportunity to attempt escape.
    
  * If you decide to take the opportunity, you'll be asked to guess one more letter.
    If you get this letter right, you'll be able to escape the perpetrator, reveal the hidden word, and beat the game!
    But if you guess incorrectly, you'll take critical damage, reducing your HP even further.

  **Survive long enough to guess the hidden word and escape the perpetrator**

  * * *
  """)


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

    # Update perpetrator insanity
    perpetrator.check_consecutive_correct_guesses(correct_guess)
    
    # convert the modified list back to a string and return it
    return ''.join(word_so_far_list)

# main
def main():
    
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
        
        
        # Welcomes user
        print("------ Welcome to Hangman: Dismemberer! ------\n")
        
        # Presents list of options and collects input
        print("[1] Play Hangman: Dismemberer")
        print("[2] About Hangman: Dismemberer")
        print("[3] Quit game")
        menu_val = input("Please select an option [1-3]: ")
        
        # Convert user input to int if digit is detected
        if menu_val.isdigit():
            menu_val = int(menu_val)
        
        match menu_val:
            case 1:
                # Debugging purposes
                print(f"\nThe word is \"{word}\". Revealed for debugging and demonstration purposes only.")
                sleep(3)
                
                while word not in word_so_far:
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
                
                # Branch statement to deal with different game outcomes
                if game_passed:
                    print("You beat the game by guessing the word!\n")
                elif game_escaped:
                    print("You beat the game by escaping!")
                    print(f"The word was \"{word}\"\n")
                else:
                    print("You died!")
                    print(f"The word was \"{word}\"\n")
                
                
            case 2:
                # Prints game desc.
                print_description()
            case 3:
                # Exits program
                print("\nGoodbye!\n")
                break
            case _:
                # Reminds user to enter valid input
                print("\nError! Please enter valid, numeric input (1-3)\n")
        
    


# call main
if __name__ == '__main__':
    main()
    

"""
Future work on this program should include, but will not necessarily be limited to,
better input validation, more menu options, more debugging options, more gameplay mechanics,
and better in-game interface. The ability to read files from user specified locations, online
or local, would also be beneficial. A gameplay record could also be implemented,
storing various metrics in a local file. Finally, perhaps a more complex game mode including
multiple words, and even sentences, could be implemented.

"""
