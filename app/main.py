import sys
from app import constant
from app import utils


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        userInput = sys.stdin.readline()
        if not userInput:
            continue

        userInput = userInput.strip() 
        command = utils.get_command(userInput)
        if command in constant.commands:
            constant.commands[command](userInput)
        else:
            utils.execute(command)


if __name__ == "__main__":
    main()
