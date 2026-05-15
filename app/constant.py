import sys
import os
from app import utils
commands = {
    "exit": lambda _: sys.exit(0),
    "echo": lambda args: sys.stdout.write(f"{" ".join(args[1:])}\n"),
    "type": lambda args: sys.stdout.write(f"{arg} is a shell builtin\n") 
                            if (arg := args[1]) in commands 
                            else utils.helper(arg),
    "pwd": lambda _: sys.stdout.write(f"{os.getcwd()}\n")
}


