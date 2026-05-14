import sys
commands = {
    "exit": lambda input: sys.exit(0),
    "echo": lambda input: sys.stdout.write(input + "\n"),
    "type": lambda input: sys.stdout.write(f"{args} is a shell builtin\n") if (args := input) in commands else sys.stdout.write(f"{args} not found\n")
}
def main():
    while True:
        sys.stdout.write("$ ")
        input = sys.stdin.readline().strip()
        command = input.split(" ")[0] if input else ""
        userInput = " ".join(input[5:])
        if command == "exit":
            commands[command]
        elif command == "echo":
            commands[command](userInput)
        elif command == "type":
            commands[command](userInput)
        pass


if __name__ == "__main__":
    main()
