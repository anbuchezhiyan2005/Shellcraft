import sys
import shutil
import subprocess
import os
from collections import namedtuple
from app.enums import result as base_result

RedirectionResult = namedtuple("RedirectionResult", ["redirect", "idx"])


def _new_result():
    return base_result.copy()


def _normalize_result(result_obj):
    result = _new_result()

    if result_obj is None:
        return result

    if isinstance(result_obj, dict):
        result["stdout"] = result_obj.get("stdout", "")
        result["stderr"] = result_obj.get("stderr", "")
        result["returncode"] = result_obj.get("returncode", 0)
        return result

    result["stdout"] = getattr(result_obj, "stdout", "") or ""
    result["stderr"] = getattr(result_obj, "stderr", "") or ""
    result["returncode"] = getattr(result_obj, "returncode", 0)
    return result


def check_redirection(parts: list):
    if not parts:
        return RedirectionResult("", -1)

    for token in ("2>>", "1>>", ">>", "2>", "1>", ">"):
        if token in parts:
            return RedirectionResult(token, parts.index(token))

    return RedirectionResult("", -1)


def execute_redirection(redirect: str, output_file_path: str, result):
    try:
        create_directory_for_file(output_file_path)

        to_file = ""
        to_console = ""
        console_stream = sys.stdout

        if redirect in (">", "1>", ">>", "1>>"):
            to_file = result["stdout"]
            to_console = result["stderr"]
            console_stream = sys.stderr
        elif redirect in ("2>", "2>>"):
            to_file = result["stderr"]
            to_console = result["stdout"]
            console_stream = sys.stdout

        mode = "a" if ">>" in redirect else "w"

        with open(output_file_path, mode=mode, encoding="utf-8") as file:
            if to_file:
                file.write(to_file)

        if to_console:
            console_stream.write(to_console)

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")


def execute(parts: list, command_dict: dict):
    if not parts:
        return
    redirect, idx = check_redirection(parts)
    command = parts[0]

    if redirect:
        LHS_command = parts[:idx]
        if not LHS_command:
            return
        if idx + 1 >= len(parts):
            return
        output_file_path = parts[idx + 1]

        if command in command_dict:
            result_obj = command_dict[command](LHS_command, command_dict)
        else:
            try:
                result_obj = subprocess.run(LHS_command, capture_output=True, text=True)
            except FileNotFoundError:
                result = _new_result()
                result["stderr"] = f"{parts[0]}: command not found\n"
                result["returncode"] = 127
                result_obj = result

        result = _normalize_result(result_obj)
        execute_redirection(redirect, output_file_path, result)
        return

    else:
        if command in command_dict:
            result_obj = command_dict[command](parts, command_dict)
        else:
            try:
                result_obj = subprocess.run(parts, capture_output=True, text=True)
            except FileNotFoundError:
                result = _new_result()
                result["stderr"] = f"{parts[0]}: command not found\n"
                result["returncode"] = 127
                result_obj = result

    result = _normalize_result(result_obj)

    if result["stdout"]:
        sys.stdout.write(result["stdout"])

    if result["stderr"]:
        sys.stderr.write(result["stderr"])

    return


def create_directory_for_file(file_path: str):
    directory = os.path.dirname(os.path.abspath(file_path))
    if directory:
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            sys.stderr.write(f"Error creating directory {directory}: {e}\n")


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
