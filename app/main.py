import os
import subprocess
import sys

builtin_commands: dict[str, str] = {
    "pwd": "pwd is a shell builtin",
    "echo": "echo is a shell builtin",
    "type": "type is a shell builtin",
    "exit": "exit is a shell builtin",
}


def handle_path_variable() -> dict[str, str]:
    path_variable = os.environ.get("PATH")

    if path_variable is None:
        return {}

    paths: list[str] = []
    paths_content: dict[str, str] = {}
    paths = path_variable.split(":")

    for path in paths:
        if os.path.isdir(path) and os.path.exists(path):
            content = os.listdir(path)

            for command in content:
                if command not in paths_content.keys():
                    paths_content[command] = path

    return paths_content


def get_user_input():
    user_input: str = input()

    return user_input.strip()


def print_output(output: str):
    sys.stdout.write(output)
    sys.stdout.write("\n")
    sys.stdout.flush()


def handle_command(user_input: str, complete_commands_list: dict[str, str] = {}):
    handle_exit_command(user_input)
    parts = user_input.split(" ")
    command = parts[0]
    arguments = parts[1:]

    if command in complete_commands_list.keys():
        if command == "echo":
            return handle_echo_command(user_input)
        if command == "type":
            return handle_type_command(user_input)
        if command == "pwd":
            return handle_pwd_command()

        command_full_path = f"{complete_commands_list[command]}/{command}"
        result = subprocess.run(
            [command_full_path] + arguments, capture_output=True, text=True)
        print_output(result.stdout.strip())

    else:
        return print_output(f"{user_input}: command not found")


def handle_exit_command(command: str):
    splitted_command = command.split(" ")

    if len(splitted_command) == 2:
        exit_command = splitted_command[0]
        code = splitted_command[1]

        if exit_command == "exit":
            sys.exit(int(code))

    return


def handle_echo_command(user_input: str):
    output_list = user_input.split(" ")[1:]
    output = " ".join(output_list)
    return print_output(output)


def handle_type_command(user_input: str):
    paths_content = handle_path_variable()
    command = user_input.split(" ")[1]

    """ Support for built-in commands """
    if command in builtin_commands.keys():
        return print_output(builtin_commands[command])

    """ Support for commands in PATH """
    if command not in paths_content.keys():
        return print_output(f"{command}: not found")

    formatted_output = f"{command} is {paths_content[command]}/{command}"

    return print_output(formatted_output)


def handle_pwd_command():
    current_working_directory = os.getcwd()
    return print_output(current_working_directory)


def run_shell():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    path_content = handle_path_variable()
    complete_commands_list = path_content | builtin_commands
    user_input = get_user_input()
    handle_command(user_input, complete_commands_list)


def main():
    while True:
        run_shell()


if __name__ == "__main__":
    main()
