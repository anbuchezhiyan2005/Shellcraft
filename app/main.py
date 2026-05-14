import sys
import os

path_dirs = os.environ.get("PATH", "").split(os.pathsep)

commands = {
    "exit": lambda _: sys.exit(0),
    "echo": lambda args: sys.stdout.write(f"{" ".join(args[1:])} \n"),
    "type": lambda args: sys.stdout.write(f"{command} is a shell builtin\n") 
                            if (command := args[1]) in commands 
                            else helper(command)
}

def helper(command: str):
    for dir in path_dirs:
        fullPath = os.path.join(dir, command)
        try:
            if os.path.isfile(fullPath) and os.access(fullPath, os.X_OK):
                sys.stdout.write(f"{command} is {fullPath} \n")
                return

        except Exception as e:
            sys.stderr.write(f"Error: {e} \n")
    
    sys.stdout.write(f"{command} not found\n")


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
