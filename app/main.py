import os
import sys

commands: dict[str, str] = {
    "echo": "echo is a shell builtin",
    "type": "type is a shell builtin",
    "exit": "exit is a shell builtin",
}

commands_list = commands.keys()


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


def handle_command(user_input: str):
    handle_exit_command(user_input)

    command = user_input.split(" ")[0]

    if command in commands_list:
        if command == "echo":
            handle_echo_command(user_input)
        if command == "type":
            return handle_type_command(user_input)
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
    paths = handle_path_variable()
    command = user_input.split(" ")[1]

    """ Support for built-in commands """
    if command in commands_list:
        return print_output(commands[command])

    """ Support for commands in PATH """
    if command not in paths.keys():
        return print_output(f"{command}: not found")

    formatted_output = f"{command} is {paths[command]}/{command}"

    return print_output(formatted_output)


def run_shell():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    user_input = get_user_input()
    handle_command(user_input)


def main():
    while True:
        run_shell()


if __name__ == "__main__":
    main()
