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
    elif ">>" in parts:
        idx = parts.index(">>")
        redirect = ">>"
    elif "1>>" in parts:
        idx = parts.index("1>>")
        redirect = "1>>"
    elif "2>>" in parts:
        idx = parts.index("2>>")
        redirect = "2>>"

    return RedirectionResult(redirect, idx)


def execute_redirection(redirect: str, idx: int, parts: list):
    LHS_command = parts[:idx]
    if idx + 1 >= len(parts):
        return

    output_file_path = parts[idx + 1]

    try:
        create_directory_for_file(output_file_path)

        to_file = ""
        to_console = ""
        console_stream = sys.stdout

        result = subprocess.run(LHS_command, capture_output=True, text=True, shell = True)

        if redirect in (">", "1>", ">>", "1>>"):
            to_file = result.stdout
            to_console = result.stderr
            console_stream = sys.stderr
        elif redirect in ("2>", "2>>"):
            to_file = result.stderr
            to_console = result.stdout
            console_stream = sys.stdout
        
        mode = "a" if ">>" in redirect else "w"
        
        if to_file:
            with open(output_file_path, mode = mode, encoding = "utf-8") as file:
                file.write(to_file)
        
        if to_console:
            console_stream.write(to_console)

    except Exception as e:
        sys.stderr.write(f"Error: {e}")


def execute(parts: list):
    command_string = " ".join(parts)
    try:
        subprocess.run(command_string, shell = True)

    except FileNotFoundError:
        sys.stderr.write(f"{parts[0]}: command not found\n")


def check_directory(parts: list):
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


def create_directory_for_file(file_path: str):
    directory = os.path.dirname(os.path.abspath(file_path))
    if directory:
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            sys.stderr.write(f"Error creating directory {directory}: {e}\n")


def check_builtin(command: str, command_dict: dict):
    if command in command_dict:
        sys.stdout.write(f"{command} is a shell builtin\n")
    else:
        helper(command)

def get_command_from_path(path: str):
    base_name = os.path.basename(path)
    command, extension = os.path.splitext(base_name)
    return command

def get_all_external_commands():
    directories = os.environ.get("PATH", "").split(os.pathsep)
    external_commands = set()

    for dir in directories:
        if not os.path.isdir(dir):
            continue
        try:
            for file in os.listdir(dir):
                if os.name == "nt":
                    cmd, ext = os.path.splitext(file)
                    if shutil.which(cmd):
                        external_commands.add(cmd)
                else:
                    file_path = os.path.join(dir, file)
                    if os.access(file_path, os.X_OK) and not os.path.isdir(file_path):
                        external_commands.add(file)

        except OSError:
            continue
    return list(external_commands)

def get_pwd_files():
    curr_path = os.getcwd()
    content = os.listdir(curr_path)
    files = []
    for c in content:
        if not os.path.isdir(c):
            files.append(c)
    
    return files
