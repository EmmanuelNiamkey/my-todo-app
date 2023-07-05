FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # Custom function : to stop repeating same code over and over
    """ Read the text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # good to have 2 breadlines between functions and other parts of the code


def write_todos(todos_arg, filepath=FILEPATH):
    """ write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
