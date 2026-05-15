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

def check_directory(userInput: str):
    command = get_command(userInput)
    path = userInput[len(command) + 1:]
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

def tokenize(userInput: str):
    command = get_command(userInput)
    input = userInput[len(command) + 1:]
    tokens = shlex.split(input, posix = True)
    print(tokens)
    return tokens
    

def get_command(userInput: str):
    command = ""

    for char in userInput:
        if char == " ":
            if command:
                return command     
        else:
            command += char
    
    return command

        
        


