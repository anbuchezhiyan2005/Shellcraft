import shlex
import sys
import os
from app import utils

def echo_command(userInput: str):
    sys.stdout.write(f"{" ".join(utils.tokenize(userInput))}\n")

def exit_command():
    sys.exit(0)

def pwd_command():
    sys.stdout.write(f"{os.getcwd()}\n")

def cd_command(userInput: str):
    utils.check_directory(userInput)

def type_command(userInput: str, command_dict: dict):
    parts = shlex.split(userInput)
    utils.check_builtin(parts[1], command_dict)
    
    