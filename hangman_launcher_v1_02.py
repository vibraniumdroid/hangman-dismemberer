# Program   : Hangman Launcher
# File      : hangman_launcher_v1_02.py
# Desc      : Load and launch hangman from online or local file
# Author    : Abdallah Abuhamda
# Instructor: David Baker
# Course    : CIS156, CGCC
# Date      : 05-02-2023

import os
import subprocess
import urllib.request

# Prompt user to load game locally or from internet
print("Select an option [1/2]:")
print("[1] Load game from local file")
print("[2] Load game from GitHub repo")

option = input("Enter option number: ")

# Launch script based on user input
match option:
    case "1":
        # Load game from local file
        file_name = input("Enter the path to your file: ")

        # Check if file exists
        if not os.path.exists(file_name):
            print("File not found.")
        else:
            # Launch file
            match os.name:
                case "nt":  # For windows
                    subprocess.Popen(["cmd", "/k", "python", file_name], creationflags=subprocess.CREATE_NEW_CONSOLE)
                case "posix":  # For linux/mac
                    match True:
                        # Search for various terminal emulators on unix systems
                        case os.path.exists("/usr/bin/x-terminal-emulator"):
                            subprocess.Popen(["x-terminal-emulator", "-e", "python3", file_name])
                        case os.path.exists("/usr/bin/gnome-terminal"):
                            subprocess.Popen(["gnome-terminal", "--", "python3", file_name])
                        case os.path.exists("/Applications/Utilities/Terminal.app"):
                            subprocess.Popen(["open", "-a", "Terminal.app", file_name])
                        case _:
                            print("No compatible terminal emulator found.")
                            print("x-terminal-emulator and gnome-terminal may be used for linux systems")
                case _:
                    print("Error! Unsupported operating system.")

    case "2":
        # Load the game from GitHub repo
        url = "https://raw.githubusercontent.com/vibraniumdroid/hangman-dismemberer/main/abuhamda_hangman_dismemberer_v1_02.py" # Change version accordingly

        # Download file
        try:
            response = urllib.request.urlopen(url)
            script_content = response.read().decode()
            # Save to temp file "temp.py"
            with open("temp.py", "w") as f:
                f.write(script_content)
            # Launch file
            match os.name:
                case "nt":  # For windows
                    subprocess.Popen(["cmd", "/k", "python", "temp.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
                case "posix":  # For linux/mac
                    match True:
                        # Search for various terminal emulators on unix systems
                        case os.path.exists("/usr/bin/x-terminal-emulator"):
                            subprocess.Popen(["x-terminal-emulator", "-e", "python3", "temp.py"])
                        case os.path.exists("/usr/bin/gnome-terminal"):
                            subprocess.Popen(["gnome-terminal", "--", "python3", "temp.py"])
                        case os.path.exists("/Applications/Utilities/Terminal.app"):
                            subprocess.Popen(["open", "-a", "Terminal.app", "temp.py"])
                        case _:
                            print("No compatible terminal emulator found.")
                            print("x-terminal-emulator and gnome-terminal may be used for linux systems")
                case _:
                    print("Error! Unsupported operating system.")
        except:
            print("Error: Could not download game from GitHub repo. Check launcher and ensure correct url is set.")

    case _:
        print("Invalid option.")
        
"""
** Changelog **

1_00:
    -Initial release

1_01:
    -Added option to load game from online file
    
1_02:
    -Improved OS support by adding various terminal emulator options.
    -Updated default URL to game file
    
     
     
     


"""
