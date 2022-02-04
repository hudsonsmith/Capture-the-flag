#! /bin/python3
# A capture the flag challenge for practicing pentesting stuff.

import json
from datetime import datetime
from os import system, listdir, mkdir
from shutil import rmtree
from time import sleep
from random import choice

lesson = "Reverse Shells"
flag_location = "Reverse Shells"
flag_text = "finished"

# Adjust the directory name accordingly.
challenge_location = "/home/hudson/hacking_tests/reverse_shells"

# Load the high scores.
with open("scores.json", "r") as f:
    data = json.load(f)
    scores = data["scores"]
    scores.sort()

highscore = scores[0]

# In seconds.
completion_time = 60

time_limit: int = int(round(datetime.now().timestamp())) + completion_time

# Keep track to see if the screen needs to be cleared.
second = 0
prev_second = 0

directory_names = [
    "cheese",
    "bread",
    "milk",
    "wife",
    "fish",
    "photos",
    "games",
    "big",
    "pancakes",
    "child",
]

file_names = [
    "butt.png",
    "wrath_mode.exe",
    "dingo.jpg",
    "fire_girl.png",
    "nerfdirt.exe",
    "superhot.exe",
    "no_cap_on_this_app.msi",
    "shovel.sh",
    "pancake.py",
    "cookie.cpp",
    "pie.py",
    "rubber_ducky.rb",
    "see.c",
    "maximus.jpg",
    "girl.mp4",
    "five.mp3",
    "penta.mp3",
    "male.mp4",
]

# Make random directories for the hacker to navigate through.

# Start by removing everything in the challenge.
for item in listdir(challenge_location):
    rmtree(f"{challenge_location}/{item}")


# Then make new directories.
dirs: list = []

for _ in range(5):
    # Make sure there are no duplicates.
    duplicate = True

    while duplicate is True:
        name = choice(directory_names)

        # If there is already a dir with that name then do nothing.
        if name in dirs:
            continue
        else:
            dirs.append(name)
            duplicate = False

# Get the directory that will contain the flag.
ctf_dir = choice(dirs)

for dir in dirs:
    mkdir(f"{challenge_location}/{dir}")

for dir in dirs:
    if dir == ctf_dir:
        flag_location = f"{challenge_location}/{dir}/flag.ctf"
        flag = open(f"{challenge_location}/{dir}/flag.ctf", "w")
        flag.close()

    for file in file_names:
        new_file = open(f"{challenge_location}/{dir}/{file}", "w")
        new_file.close()

while True:
    f = open(flag_location, "r")
    text = f.read()

    current_time = int(round(datetime.now().timestamp()))

    if time_limit <= current_time:
        print("You lose, game over.")
        f.close()
        break

    elif text == f"{flag_text}\n":
        print("Challenge completed. Congrats.")

        time_taken = completion_time - second

        print(f"Time Taken: {time_taken}.")

        if highscore > time_taken:
            print("High Score Beaten! Let's GO!")

        scores.append(time_taken)

        with open("scores.json", "w") as f:
            json.dump({"scores": scores}, f)

        f.close()

        with open(flag_location, "w") as f:
            f.write("")

        break

    second = time_limit - current_time

    # If the second is not equal to the previous second.
    if second != prev_second:
        system("clear")
        print("Current Lesson: {lesson}\n")
        print(f"Time left: {second} seconds.")
        print(f"Highscore: {highscore} seconds.")
        prev_second = second
