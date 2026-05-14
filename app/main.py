import sys
from app import constant
from app import utils

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        userInput = sys.stdin.readline().strip()
        if not userInput:
            continue

        input = userInput.split()
        command = input[0] if input else ""
        if command in constant.commands:
            constant.commands[command](input)
        else:
            utils.execute(input)


if __name__ == "__main__":
    main()
