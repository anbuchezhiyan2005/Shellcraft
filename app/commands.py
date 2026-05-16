import sys
import os
from app import utils
import subprocess

def echo_command(parts: list):
    if ">" in parts:
        idx = parts.index(">")
        LHS_command = parts[: idx]
        output_file_path = parts[idx + 1]

        try:
            directory = os.path.dirname(os.path.abspath(output_file_path))
            if directory:
                try:
                    os.makedirs(directory, exist_ok = True)
                except Exception as e:
                    sys.stderr.write(f"Error creating directory {directory}: {e}\n")

            result = subprocess.run(LHS_command, capture_output = True, text = True)
            with open(output_file_path, mode = "w", encoding = "utf-8") as file:
                file.write(result.stdout)

        except Exception as e:
            sys.stderr.write(f"Error: {e}")
    else:
        utils.execute(parts)

def exit_command():
    sys.exit(0)

def pwd_command():
    sys.stdout.write(f"{os.getcwd()}\n")

def cd_command(parts: list):
    utils.check_directory(parts)

def type_command(parts: list, command_dict: dict):
    utils.check_builtin(parts[1], command_dict)
    
    