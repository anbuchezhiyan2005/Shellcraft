import shlex
import readline
import glob
import os
from app import utils
from app import commands

command_dict = {
    "exit": lambda parts, command_dict: commands.exit_command(parts, command_dict),
    "echo": lambda parts, command_dict: commands.echo_command(parts, command_dict),
    "type": lambda parts, command_dict: commands.type_command(parts, command_dict),
    "pwd": lambda parts, command_dict: commands.pwd_command(parts, command_dict),
    "cd": lambda parts, command_dict: commands.cd_command(parts, command_dict),
}

argument_completers = {
    "echo": lambda text, state: file_completer(text, state),
    "type": lambda text, state: cmd_completer(text, state),
    "cd": lambda text, state: file_completer(text, state),
    "cat": lambda text, state: file_completer(text, state),
}

external_commands = utils.get_all_external_commands()
all_commands = sorted(list(command_dict.keys()) + external_commands)


def cmd_completer(text, state):
    matches = []

    for cmd in all_commands:
        if cmd.startswith(text):
            matches.append(cmd)

    if len(matches) == 1:
        if state == 0:
            return matches[state] + " "
        else:
            return None

    if state < len(matches):
        return matches[state] + " "
    else:
        return None


def file_completer(text, state):
    matches = glob.glob(text + "*")

    for i, match in enumerate(matches):
        if os.path.isdir(match):
            matches[i] += os.sep

    if len(matches) == 1:
        if state == 0:
            return matches[state] + " "
        else:
            return None

    if state < len(matches):
        return matches[state] + " "
    else:
        return None


def main_completer(text, state):
    line_buffer = readline.get_line_buffer()
    begin_index = readline.get_begidx()
    end_index = readline.get_endidx()

    target_word = line_buffer[begin_index:end_index]

    if begin_index == 0:
        return cmd_completer(target_word, state)

    try:
        parts = shlex.split(line_buffer)

        if len(parts) > 0:
            command = parts[0]
            completer_func = argument_completers.get(command, file_completer)
            return completer_func(target_word, state)

    except ValueError:
        return None


readline.set_completer(main_completer)
readline.set_completer_delims(" \t\n")
readline.parse_and_bind("tab: complete")


def main():
    while True:
        userInput = input("$ ")
        if not userInput:
            continue
        try:
            parts = shlex.split(userInput)
        except ValueError:
            continue
        if parts:
            utils.execute(parts, command_dict)


if __name__ == "__main__":
    main()
