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

def execute(parts: list):
    command = parts[0]
    path = shutil.which(command)
    if path:
        redirection = False
        idx = -1
        if ">" in parts:
            idx = parts.index(">")
            redirection = True
        elif "1>" in parts:
            idx = parts.index("1>")
            redirection = True
        else:
            redirection = False
        
        if redirection:
            LHS_command = parts[: idx]
            output_file_path = parts[idx + 1] if idx + 1 < len(parts) else sys.stderr.write("Error: Missing output file for redirection\n")

            try:
                directory = os.path.dirname(os.path.abspath(output_file_path))
                if directory:
                    try:
                        os.makedirs(directory, exist_ok = True)
                    except Exception as e:
                        sys.stderr.write(f"Error creating directory {directory}: {e}\n")

                result = subprocess.run(LHS_command, capture_output = True, text = True)
                with open(output_file_path, mode = "w", encoding = "utf-8") as file:
                    file.write(result.stdout + result.stderr)

            except Exception as e:
                sys.stderr.write(f"Error: {e}")
        else:
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
        


