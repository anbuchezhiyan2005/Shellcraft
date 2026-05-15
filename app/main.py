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
        if command in constant.command_dict:
            constant.command_dict[command](userInput)
        else:
            utils.execute(userInput)


if __name__ == "__main__":
    main()
