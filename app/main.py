import sys
from app import constant

def main():
    while True:
        sys.stdout.write("$ ")
        userInput = sys.stdin.readline().strip()
        input = userInput.split()
        command = input[0] if input else ""
        if command in constant.commands:
            constant.commands[command](input)
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
