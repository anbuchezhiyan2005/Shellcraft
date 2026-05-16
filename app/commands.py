import sys
import os
from app import utils

def echo_command(parts: list):
    if ">" in parts:
        idx = parts.index(">")
        content = parts[idx - 1]
        file_path = parts[idx + 1]
        print(f"File path: {file_path}")

        try:
            directory = os.path.dirname(os.path.abspath(file_path))
            print(f"Directory: {directory}")
            if directory and not os.path.exists(directory):
                print("Directory does not exist")
                os.makedirs(directory)
            else:
               print("Directory exist") 

            with open(file_path, mode = "w", encoding = "utf-8") as file:
                file.write(content)

        except Exception as e:
            sys.stderr.write(f"Error: {e}")
    else:
        sys.stdout.write(f"{" ".join(parts[1:])}\n")

def exit_command():
    sys.exit(0)

def pwd_command():
    sys.stdout.write(f"{os.getcwd()}\n")

def cd_command(parts: list):
    utils.check_directory(parts)

def type_command(parts: list, command_dict: dict):
    utils.check_builtin(parts[1], command_dict)
    
    