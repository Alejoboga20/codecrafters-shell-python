import sys

command_list: list[str] = ["echo"]


def get_user_input():
    user_input: str = input()

    return user_input.strip()


def print_output(output: str):
    sys.stdout.write(output)
    sys.stdout.write("\n")


def handle_command(user_input: str):
    last_user_inputs.append(user_input)
    handle_exit_command(user_input)

    command = user_input.split(" ")[0]

    if command in command_list:
        if command == "echo":
            output_list = user_input.split(" ")[1:]
            output = " ".join(output_list)
            return print_output(output)
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
