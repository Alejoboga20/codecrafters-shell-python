# Python Command Line Interface (CLI) from Scratch

This project is a basic Command Line Interface (CLI) built from scratch in Python. It supports executing system commands, handling custom commands like `echo`, and simulating terminal-like behaviors with dynamic command handling.

## Features

- **Custom Command Handling**: Supports built-in commands like `echo`, `type`, and more.
- **System Command Execution**: Runs executable files located in specified directories.
- **Argument Parsing**: Accepts arguments for commands, allowing commands like `my_exe <argument>`.
- **Interactive Prompt**: Displays a `$ ` prompt after each command, simulating a terminal.

## Getting Started

### Prerequisites

- **Python 3.8+** is required to run this project.

### Running the CLI

```
python3 app/main.py
```

### Usage

Once running, you’ll see a $ prompt where you can enter commands. The CLI will interpret and execute recognized commands or print an error message if the command is not found.
