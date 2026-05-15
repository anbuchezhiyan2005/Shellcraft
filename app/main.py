import sys
from app import utils
from app import commands

command_dict = {
    "exit": lambda _: commands.exit_command(),
    "echo": lambda input: commands.echo_command(input),
    "type": lambda input: commands.type_command(input, command_dict),
    "pwd": lambda _: commands.pwd_command(),
    "cd": lambda input: commands.cd_command(input) 
}

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        userInput = sys.stdin.readline()
        userInput = userInput.strip() 
        if not userInput:
            continue
        
        command = utils.get_command(userInput)
        if command in command_dict:
            command_dict[command](userInput)
        else:
            utils.execute(userInput)


if __name__ == "__main__":
    main()
