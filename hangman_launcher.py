# Program   : Hangman Launcher
# File      : hangman_launcher.py
# Desc      : Load and launch hangman from online or local file
# Author    : Abdallah Abuhamda
# Instructor: David Baker
# Course    : CIS156, CGCC
# Date      : 05-02-2023

import os
import subprocess
import urllib.request

# Functions to launch game
def launch_local(file_name):
    """Launches the game from a local file."""
    if not os.path.exists(file_name):
        print("File not found.")
    else:
        launch_command = ["python", file_name]
        subprocess.Popen(launch_command, creationflags=subprocess.CREATE_NEW_CONSOLE)

def launch_github(url):
    """Launches the game from a GitHub URL."""
    try:
        response = urllib.request.urlopen(url)
        script_content = response.read().decode()
        with open("temp.py", "w") as f:
            f.write(script_content)
        launch_command = ["python", "temp.py"]
        subprocess.Popen(launch_command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    except:
        print("Error: Could not download game from GitHub repo. Check launcher and ensure correct url is set.")

# Prompt user to load game locally or from internet
print("Select an option [1/2]:")
print("[1] Load game from local file")
print("[2] Load game from GitHub repo")

option = input("Enter option number: ")

# Launch script based on user input
if option == "1":
    # Load game from local file
    file_name = input("Enter the path to your file: ")
    launch_local(file_name)
elif option == "2":
    # Load game from GitHub repo
    url = "https://raw.githubusercontent.com/vibraniumdroid/hangman-dismemberer/main/abuhamda_hangman_dismemberer_v1_02.py"
    launch_github(url)
else:
    print("Invalid option.")
