import sys
import shutil
import subprocess
import os

def helper(command: str):
    fullPath = shutil.which(command)
    if fullPath:
        sys.stdout.write(f"{command} is {fullPath}\n")    
    else:
        sys.stdout.write(f"{command} not found\n")

def execute(command: list[str]):
    path = shutil.which(command[0])
    if path:
        subprocess.run(command)
    else:
        sys.stdout.write(f"{" ".join(command)}: command not found\n")

def check_directory(command: list):
    path = " ".join(command[1:])
    curr_path = os.getcwd()

    if path == "~":
        try:
            os.chdir(os.getenv('HOME'))
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
