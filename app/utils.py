import sys
import shutil
import subprocess
import os
import shlex

def helper(command: str):
    fullPath = shutil.which(command)
    if fullPath:
        sys.stdout.write(f"{command} is {fullPath}\n")    
    else:
        sys.stdout.write(f"{command} not found\n")

def execute(input: str):
    parts = shlex.split(input)
    command = parts[0]
    path = shutil.which(command)
    if path:
        subprocess.run(parts)
    else:
        sys.stdout.write(f"{command}: command not found\n")

def check_directory(parts: list):
    path = " ".join(parts[1:])
    curr_path = os.getcwd()

    if path == "~":
        try:
            home_path = os.path.expanduser('~')
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

def check_builtin(command: str, command_dict: dict):
    if command in command_dict:
        sys.stdout.write(f"{command} is a shell builtin\n")
    else:
        helper(command)
        


