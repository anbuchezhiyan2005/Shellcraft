import sys
import shlex
import readline
from app import utils
from app import commands

command_dict = {
    "exit": lambda _: commands.exit_command(),
    "echo": lambda parts: commands.echo_command(parts),
    "type": lambda parts: commands.type_command(parts, command_dict),
    "pwd": lambda _: commands.pwd_command(),
    "cd": lambda parts: commands.cd_command(parts) 
}

def completer(text, state):
    matches = []

    for key in command_dict:
        if key.startswith(text):
            matches.append(key)
    
    if state < len(matches):
        return matches[state]
    else:
        return None

readline.set_completer(completer)
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
