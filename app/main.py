import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = sys.stdin.readline().strip()
        if command == "exit":
            break
        sys.stdout.write(f"{command}: command not found\n")
        pass


if __name__ == "__main__":
    main()
