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

external_commands = utils.get_all_external_commands()
all_commands = sorted(list(command_dict.keys()) + external_commands)

def completer(text, state):
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
