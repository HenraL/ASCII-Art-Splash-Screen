#!/bin/env python3
##
## EPITECH PROJECT, 2022
## ASCII-Art-Splash-Screen
## File description:
## ascii_revisited.py
##

# Code written by (c) Henry Letellier (please leave this in the file)

import random
import os
import requests

default_art = """
  _________
 /   _____/ __________________ ___.__.
 \\_____  \\ /  _ \\_  __ \\_  __ <   |  |
 /        (  <_> )  | \\/|  | \\/\\___  |
/_______  /\\____/|__|   |__|   / ____|
        \\/                     \\/
            _______
            \\      \\   ____
            /   |   \\ /  _ \\
           /    |    (  <_> )
           \\____|__  /\\____/
                   \\/
                       .__
                       |__| _____ _____     ____   ____   ______
                       |  |/     \\\\__  \\   / ___\\_/ __ \\ /  ___/
                       |  |  Y Y  \\/ __ \\_/ /_/  >  ___/ \\___ \\ 
                       |__|__|_|  (____  /\\___  / \\___  >____  >
                                \\/     \\//_____/      \\/     \\/ 
                             __             .___
                           _/  |_  ____   __| _/____  ___.__.   
                           \\   __\\/  _ \\ / __ |\\__  \\<   |  |
                            |  | (  <_> ) /_/ | / __ \\\\___  |   
                            |__|  \\____/\\____ |(____  / ____|   
                                             \\/     \\/\\/
"""

def get_file_content(filename:str, location:str) -> str:
    f = open(f"{location}/{filename}", "r", encoding="utf-8")
    content = f.read()
    f.close()
    return content

def display(the_file_content:str) -> None:
    print(the_file_content)

def get_file_online(url_start:str, url_end:str, int_max:int) -> str:
    content = requests.get(f"{url_start}{str(random.randint(1,int_max))}{url_end}")
    if content.status_code == 200:
        raw_file_content = content.content
        decoded_content = raw_file_content.decode()
        if "</html>" not in decoded_content:
            return decoded_content
        else:
            return ""
    else:
        return ""

usr_location = os.getcwd()
file_url_start = 'https://raw.githubusercontent.com/DanCRichards/ASCII-Art-Splansh-Screen/master/art/'
file_url_end = ".txt"
max_nb_files = 9
file_content = get_file_online(file_url_start, file_url_end, max_nb_files)
if file_content == "":
    try:
        program_location = f"{os.environ['HOME']}/manually_installed_software/ascii_in_terminal/ASCII-Art-Splash-Screen_fork/"
        # Change the path of program_location in order to set tge repository containing the folder with the ascii art folder
        art_location = "art"
        # Change the content of the variable art_location in order to change the name of the folder containing the art files
        os.chdir(program_location)
        art_files = os.listdir(art_location)
        art_file = random.randint(1, len(art_files)-1)
        file_name = art_files[art_file]
        file_content = get_file_content(file_name, art_location)
        os.chdir(usr_location)
    except:
        file_content = default_art

display(file_content)
