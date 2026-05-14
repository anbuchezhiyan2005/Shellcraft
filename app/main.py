import sys
commands = {
    "exit": lambda input: sys.exit(0),
    "echo": lambda input: sys.stdout.write(f"{" ".join(input[1:])} \n"),
    "type": lambda input: sys.stdout.write(f"{args} is a shell builtin\n") 
                            if (args := input[1]) in commands 
                            else sys.stdout.write(f"{args} not found\n")
}

def main():
    while True:
        sys.stdout.write("$ ")
        userInput = sys.stdin.readline().strip()
        input = userInput.split()
        command = input[0] if input else ""
        if command in commands:
            commands[command](input)
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
