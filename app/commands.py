import shlex
import sys
import os
from app import constant
from app import utils

def echo_command(userInput: str):
    sys.stdout.write(f"{" ".join(utils.tokenize(userInput))}\n")

def exit_command():
    sys.exit(0)

def pwd_command():
    sys.stdout.write(f"{os.getcwd()}\n")

def cd_command(userInput: str):
    utils.check_directory(userInput)

def type_command(userInput: str):
    parts = shlex.split(userInput)
    argument = parts[1]
    
    if argument in constant.commands:
        sys.stdout.write(f"{argument} is a shell builtin\n")
    else:
        utils.helper(argument)