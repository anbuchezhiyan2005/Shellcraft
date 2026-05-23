import sys
import os
import subprocess
import shutil

def echo_command(parts: list):
    return subprocess.run(parts, capture_output = True, text = True, shell = True)

def exit_command():
    sys.exit(0)

def pwd_command():
    sys.stdout.write(f"{os.getcwd()}\n")

def cd_command(parts: list):
    # path = " ".join(parts[1:])
    # curr_path = os.getcwd()

    # if path == "~":
    #     try:
    #         home_path = os.path.expanduser("~")
    #         os.chdir(home_path)
    #     except Exception as e:
    #         sys.stderr.write(f"Error: {e}\n")
    #         os.chdir(curr_path)

    # elif os.path.isdir(path):
    #     try:
    #         os.chdir(path)
    #     except Exception as e:
    #         sys.stderr.write(f"Error: {e}\n")
    #         os.chdir(curr_path)
    # else:
    #     sys.stdout.write(f"cd: {path}: No such file or directory\n")
    return subprocess.run(parts, capture_output = True, text = True, shell = True)

def type_command(parts: list, command_dict: dict):
    result = subprocess.run(parts, capture_output = True, text = True, shell = True)
    command = parts[0]
    if command in command_dict:
        result.stdout = f"{command} is a shell builtin\n"
    else:
        fullPath = shutil.which(command)
        if fullPath:
            result.stdout = f"{command} is {fullPath}\n"
        else:
            result.stderr = f"{command} not found\n"
    
    return result
