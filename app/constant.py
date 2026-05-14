import sys
import os
import shutil
path_dirs = os.environ.get("PATH", "").split(os.pathsep)

def helper(command: str):
    fullPath = shutil.which(command)
    print(fullPath)
    if fullPath:
        sys.stdout.write(f"{command} is {fullPath} \n")    
    else:
        sys.stdout.write(f"{command} not found\n")
    
    return

commands = {
    "exit": lambda _: sys.exit(0),
    "echo": lambda args: sys.stdout.write(f"{" ".join(args[1:])} \n"),
    "type": lambda args: sys.stdout.write(f"{arg} is a shell builtin\n") 
                            if (arg := args[1]) in commands 
                            else helper(arg)
}
