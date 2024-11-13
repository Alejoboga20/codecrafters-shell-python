import sys

command_list: list[str] = ["pwd", "cd"]


def get_user_input():
    user_input: str = input()

    return user_input


def print_output(output: str):
    sys.stdout.write(output)
    sys.stdout.write("\n")


def find_command(command: str):
    if command in command_list:
        return command
    else:
        return f"{command}: command not found"


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    user_input = get_user_input()
    result = find_command(user_input)

    print_output(result)


if __name__ == "__main__":
    main()
