import sys
import os
from app import utils

def echo_command(parts: list):
        redirect, idx = utils.check_redirection(parts)
        if redirect:
            utils.execute_redirection(redirect, idx, parts)
        else:
            output = " ".join(parts[1:])
            sys.stdout.write(output + "\n")

def exit_command():
    sys.exit(0)

def pwd_command():
    sys.stdout.write(f"{os.getcwd()}\n")

def cd_command(parts: list):
    utils.check_directory(parts)

def type_command(parts: list, command_dict: dict):
    utils.check_builtin(parts[1], command_dict)
    
    