from pathlib import *
import settings
from os import chdir

parent = Path('..')
current_path = settings.work_path
chdir(current_path)

nest_index = 0

def make_folder(user_input):
    if len(user_input) < 2:
        print("Argument expected")
    else:
        Path.mkdir(Path.cwd() / user_input[1])

def remove_folder(user_input):
    if len(user_input) < 2:
        print("Argument expected")
    else:
        Path.rmdir(Path.cwd() / user_input[1])

def change_folder(user_input):
    if len(user_input) < 2:
        print("Argument expected")
    else:
        global nest_index
        if user_input[1] == '..':
            if nest_index == 0:
                print('Cannot move out from work folder')
            else:
                nest_index -= 1
                chdir(Path.cwd() / user_input[1])
        else:
            nest_index += 1
            chdir(Path.cwd() / user_input[1])

def make_file(user_input):
    if len(user_input) < 2:
        print("Argument expected")
    else:
        Path.touch(Path.cwd() / user_input[1])


def main():

    while True:
        user_input = input(str(Path.cwd()) + " >>").split()
        if user_input[0] == "mkfolder":
            make_folder(user_input)

        elif user_input[0] == "rmfolder":
            remove_folder(user_input)

        elif user_input[0] == "cd":
            change_folder(user_input)

        elif user_input[0] == "mkfile":
            make_file(user_input)

        else:
            print("Unknown command!")
main()