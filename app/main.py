import sys
builtin = ["exit", "echo", "type"]

def main():
    while True:
        sys.stdout.write("$ ")
        command = sys.stdin.readline().strip()
        args = command.split()
        if args[0] == "exit":
            break
        elif args[0] == "echo":
            sys.stdout.write(" ".join(args[1:]) + "\n")
        elif args[0] == "type":
            if args[1] in builtin:
                sys.stdout.write(f"{args[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{args[1]}: not found\n")
        else:
            sys.stdout.write(f"{command}: not found\n")
        pass


if __name__ == "__main__":
    main()
