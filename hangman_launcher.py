# Program   : Hangman Launcher
# File      : hangman_launcher.py
# Desc      : Load and launch hangman from online or local file
# Author    : Abdallah Abuhamda
# Instructor: David Baker
# Course    : CIS156, CGCC
# Date      : 05-02-2023

import os
import platform
import subprocess
import urllib.request

# Functions to launch game
def launch_local(file_name):
    """Launches the game from a local file."""
    if not os.path.exists(file_name):
        print("File not found.")
    else:
        launch_command = get_terminal_command() + ["python", file_name]
        subprocess.Popen(launch_command)

def launch_online(url):
    """Launches the game from an online URL."""
    try:
        response = urllib.request.urlopen(url)
        script_content = response.read().decode()
        with open("temp.py", "w") as f:
            f.write(script_content)
        launch_command = get_terminal_command() + ["python", "temp.py"]
        subprocess.Popen(launch_command)
    except:
        print("Error: Could not download game from URL. Check launcher and ensure correct url is set.")

def get_terminal_command():
    """Returns the command to launch a terminal emulator on the current platform."""
    if platform.system() == "Windows":
        return ["cmd", "/c", "start", "cmd.exe", "/k"]
    elif platform.system() == "Darwin":
        return ["open", "-a", "Terminal"]
    else: # assume Linux
        # Check for common terminal emulators
        if os.path.exists("/usr/bin/gnome-terminal"):
            return ["gnome-terminal", "--"]
        elif os.path.exists("/usr/bin/x-terminal-emulator"):
            return ["x-terminal-emulator", "-e"]
        elif os.path.exists("/usr/bin/xfce4-terminal"):
            return ["xfce4-terminal", "-x"]
        else:
            return [] # fallback to no terminal command

# Prompt user to load game locally or from internet
print("Select an option [1/2]:")
print("[1] Load game from local file")
print("[2] Load game from online file")

option = input("Enter option number: ")

# Launch script based on user input
if option == "1":
    # Load game from local file
    file_name = input("Enter the path to your file: ")
    launch_local(file_name)
elif option == "2":
    # Load game from online file
    print("Leave empty and enter to use default URL")
    url = input(f"Enter the URL to the online file: ")
    if not url:
        url = "https://raw.githubusercontent.com/vibraniumdroid/hangman-dismemberer/main/abuhamda_hangman_dismemberer_v1_02.py"
    launch_online(url)
else:
    print("Error! Invalid option.")
