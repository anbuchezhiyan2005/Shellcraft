from app import commands

command_dict = {
    "exit": lambda _: commands.exit_command(),
    "echo": lambda input: commands.echo_command(input),
    "type": lambda input: commands.type_command(input),
    "pwd": lambda _: commands.pwd_command(),
    "cd": lambda input: commands.cd_command(input) 
}


