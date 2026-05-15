import sys
import os
from app import utils

commands = {
    "exit": lambda _: sys.exit(0),
    "echo": lambda input: sys.stdout.write(f"{" ".join(utils.tokenize(input))}\n"),
    "type": lambda input: utils.type_command(input),
    "pwd": lambda _: sys.stdout.write(f"{os.getcwd()}\n"),
    "cd": lambda input: utils.check_directory(input) 
}


