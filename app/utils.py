import sys
import shutil
import subprocess
import os
from collections import namedtuple

RedirectionResult = namedtuple("RedirectionResult", ["redirect", "idx"])

def helper(command: str):
    fullPath = shutil.which(command)
    if fullPath:
        sys.stdout.write(f"{command} is {fullPath}\n")    
    else:
        sys.stdout.write(f"{command} not found\n")

def check_redirection(parts: list):

    if not parts:
        return RedirectionResult("", -1)
    
    redirect = ""
    idx = -1
    if ">" in parts:
        idx = parts.index(">")
        redirect = ">"
    elif "1>" in parts:
        idx = parts.index("1>")
        redirect = "1>"
    elif "2>" in parts:
        idx = parts.index("2>")
        redirect = "2>"
    
    return RedirectionResult(redirect, idx)

def execute_redirection(redirect: str, idx: int, parts: list):
    LHS_command = parts[: idx]
    if idx + 1 >= len(parts):
        return
    
    output_file_path = parts[idx + 1]

    try:
        create_directory_for_file(output_file_path)

        result = subprocess.run(LHS_command, capture_output = True, text = True)        
        with open(output_file_path, mode = "w", encoding = "utf-8") as file:
            file.write(result.stderr if redirect == "2>" else result.stdout)

        if redirect in ("1>", ">") and result.stderr:
            sys.stderr.write(result.stderr)
        
        if redirect == "2>" and result.stdout:
            sys.stdout.write(result.stdout)
        

    except Exception as e:
        sys.stderr.write(f"Error: {e}")

def execute(parts: list):
    command = parts[0]
    path = shutil.which(command)
    if path:
        redirect, idx = check_redirection(parts)
        if redirect:
            execute_redirection(redirect, idx, parts)
        else:
            subprocess.run(parts)
            
    else:
        sys.stderr.write(f"{command}: command not found\n")

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

def create_directory_for_file(file_path: str):
    directory = os.path.dirname(os.path.abspath(file_path))
    if directory:
        try:
            os.makedirs(directory, exist_ok = True)
        except Exception as e:
            sys.stderr.write(f"Error creating directory {directory}: {e}\n")

def check_builtin(command: str, command_dict: dict):
    if command in command_dict:
        sys.stdout.write(f"{command} is a shell builtin\n")
    else:
        helper(command)
        


