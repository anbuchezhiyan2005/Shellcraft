# Shellcraft

A Unix shell built from scratch in Python.

## Approach
I look up functions, read docs, and debug as I go — but the decisions on how to structure and build this are my own.

## Features
- `echo` — print text to stdout, handles quoted strings
- `exit` — exit the shell
- `pwd` — print current working directory
- `cd` — change directory, supports `~`
- `type` — identify if a command is a shell builtin or external
- External command execution via PATH resolution
- **Redirection (`>` and `1>`)** — redirect stdout to a file, creating directories as needed

## Project Structure
```
app/
├── main.py      # REPL loop and command routing
├── commands.py  # Builtin command implementations
└── utils.py     # Helper utilities
```

## Run
```bash
python3 -m app.main
```

## Status
🚧 Work in progress