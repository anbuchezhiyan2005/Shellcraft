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
    path = " ".join(parts[1:])
    curr_path = os.getcwd()

    if path == "~":
        try:
            home_path = os.path.expanduser("~")
            os.chdir(home_path)
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            os.chdir(curr_path)

    elif os.path.isdir(path):
        try:
            os.chdir(path)
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            os.chdir(curr_path)
    else:
        sys.stdout.write(f"cd: {path}: No such file or directory\n")

def type_command(parts: list, command_dict: dict):
    command = parts[0]
    if command in command_dict:
        sys.stdout.write(f"{command} is a shell builtin\n")
    else:
        utils.helper(command)