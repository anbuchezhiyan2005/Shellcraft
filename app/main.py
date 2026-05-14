import sys
commands = {
    "exit": lambda _: sys.exit(0),
    "echo": lambda input: sys.stdout.write(input[1:] + "\n"),
    "type": lambda input: sys.stdout.write(f"{args} is a shell builtin\n") if (args := input[0]) in commands else sys.stdout.write(f"{args} not found\n")
}
def main():
    while True:
        sys.stdout.write("$ ")
        userInput = sys.stdin.readline().strip()
        input = userInput.split()
        command = input[0] if input else ""
        if command == "exit":
            commands[command]
        elif command == "echo":
            commands[command](input)
        elif command == "type":
            commands[command](input)
        pass


if __name__ == "__main__":
    main()
