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

def check_directory(path: str):
    curr_path = os.getcwd()
    if os.path.is_dir(path):
        try:
            os.chdir(path)
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            os.chdir(curr_path)
    
    else:
        sys.stdout.write(f"cd: {path}: No such file or directory\n")
