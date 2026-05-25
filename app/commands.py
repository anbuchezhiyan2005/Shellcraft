import sys
import os
import shutil
from app.enums import result as base_result


def _new_result():
    return base_result.copy()


def echo_command(parts: list, command_dict: dict):
    result = _new_result()
    output = " ".join(parts[1:])
    result["stdout"] = f"{output}\n"
    return result


def exit_command(parts: list, command_dict: dict):
    sys.exit(0)


def pwd_command(parts: list, command_dict: dict):
    result = _new_result()
    result["stdout"] = f"{os.getcwd()}\n"
    return result


def cd_command(parts: list, command_dict: dict):
    result = _new_result()
    path = " ".join(parts[1:])
    curr_path = os.getcwd()

    if path == "~" or path == "":
        try:
            home_path = os.path.expanduser("~")
            os.chdir(home_path)
        except Exception as e:
            result["stderr"] = f"Error: {e}\n"
            result["returncode"] = 1
            os.chdir(curr_path)

    elif os.path.isdir(path):
        try:
            os.chdir(path)
        except Exception as e:
            result["stderr"] = f"Error: {e}\n"
            result["returncode"] = 1
            os.chdir(curr_path)
    else:
        result["stderr"] = f"cd: {path}: No such file or directory\n"
        result["returncode"] = 1
    return result


def type_command(parts: list, command_dict: dict):
    result = _new_result()
    if len(parts) < 2:
        result["stderr"] = "type: missing argument\n"
        result["returncode"] = 1
        return result
    command = parts[1]
    if command in command_dict:
        result["stdout"] = f"{command} is a shell builtin\n"
    else:
        fullPath = shutil.which(command)
        if fullPath:
            result["stdout"] = f"{command} is {fullPath}\n"
        else:
            result["stderr"] = f"{command} not found\n"
            result["returncode"] = 1

    return result
