import sys
import shutil
import subprocess

def helper(command: str):
    fullPath = shutil.which(command)
    if fullPath:
        sys.stdout.write(f"{command} is {fullPath} \n")    
    else:
        sys.stdout.write(f"{command} not found\n")

def execute(command: list[str]):
    path = shutil.which(command[0])
    if path:
        subprocess.run(command)
    else:
        sys.stdout.write(f"{" ".join(command)}: command not found\n")
