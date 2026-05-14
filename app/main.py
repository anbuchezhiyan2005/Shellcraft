import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = sys.stdin.readline().strip()
        args = command.split()
        if args[0] == "exit":
            break
        if args[0] == "echo":
            sys.stdout.write(" ".join(args[1:]) + "\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")
        pass


if __name__ == "__main__":
    main()
