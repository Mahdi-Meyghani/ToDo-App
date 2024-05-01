"""
This is the requirements
functions for To-Dos.
"""

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH) -> list:
    """
    Read a text file and return the list
    of to-dos items.
    """
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list: list, filepath=FILEPATH) -> None:
    """ Write the to-dos items list in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
