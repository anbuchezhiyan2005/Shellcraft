import shlex
import readline
import glob
import os
from app import utils
from app import commands

command_dict = {
    "exit": lambda _: commands.exit_command(),
    "echo": lambda parts: commands.echo_command(parts),
    "type": lambda parts: commands.type_command(parts, command_dict),
    "pwd": lambda _: commands.pwd_command(),
    "cd": lambda parts: commands.cd_command(parts) 
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
    
    sorted(matches)
    if state < len(matches):
        return matches[state] + " "
    else:
        return None

argument_completers = {
    "echo": lambda text, state: file_completer(text, state),
    "type": lambda text, state: cmd_completer(text, state),
    "cd": lambda text, state: file_completer(text, state),
    "cat": lambda text, state: file_completer(text, state)
}

def main_completer(text, state):
    line_buffer = readline.get_line_buffer()

    parts = shlex.split(line_buffer)

    if len(parts) <= 1:
        return cmd_completer(text, state)
    else:
        command = parts[0]
        if command in argument_completers:
            return argument_completers[command](text, state)
        else:
            return cmd_completer(text, state)


readline.set_completer(main_completer)
readline.parse_and_bind("tab: complete")

def main():
    while True:
        userInput = input("$ ")
        if not userInput:
            continue
        parts = shlex.split(userInput)
        command = parts[0]
        if command in command_dict:
            command_dict[command](parts)
        else:
            utils.execute(parts)


if __name__ == "__main__":
    main()
