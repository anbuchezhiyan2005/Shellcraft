import sys
import os

path_dirs = os.environ.get("PATH", "").split(os.pathsep)

commands = {
    "exit": lambda _: sys.exit(0),
    "echo": lambda input: sys.stdout.write(f"{" ".join(input[1:])} \n"),
    "type": lambda input: sys.stdout.write(f"{args} is a shell builtin\n") 
                            if (args := input[1]) in commands 
                            else helper(args)
}

def helper(command: str):
    for dir in path_dirs:
        fullPath = os.path.join(dir, command)
        try:
            if os.path.isFile(fullPath) and os.access(fullPath, os.X_OK):
                sys.stdout.write(f"{command} is {fullPath} \n")
                return
            else: 
                continue

        except Exception as e:
            sys.stderr.write(f"Error: {e} \n")
        finally:
            pass
    
    sys.stdout.write("f{command} not found\n")


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
