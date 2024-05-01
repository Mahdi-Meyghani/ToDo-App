# from todo_functions import get_todos
import todo_functions
import time

now = time.strftime("%a, %b %d, %Y at %H:%M:%S")
print("Today is", now)

test = True
while test:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add '):
        todo = user_action[4:]

        todos = todo_functions.get_todos()

        todos.append(todo.strip() + "\n")

        todo_functions.write_todos(todos)

    elif user_action == 'show':

        todos = todo_functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action == 'exit':
        test = False

    elif user_action.startswith('complete '):
        try:
            index = int(user_action[9:])
            index -= 1

            todos = todo_functions.get_todos()

            todo_to_complete = todos[index].strip('\n')
            todos.pop(index)

            todo_functions.write_todos(todos)

            message = f"Todo '{todo_to_complete}' was removed from the Todos list."
            print(message)

        except ValueError:
            print("You should enter a number of todo for complete.")
            continue

        except IndexError:
            print(f"There is no item with that number.")
            continue

    elif user_action.startswith('edit '):
        try:
            index = int(user_action[5:])
            index -= 1

            todos = todo_functions.get_todos()

            todo_to_edit = todos[index].strip('\n')

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo.lower().strip() + '\n'
            todo_edited = todos[index].strip('\n')

            todo_functions.write_todos(todos)

            message = f"Edited Todo '{todo_to_edit}' to Todo '{todo_edited}'."
            print(message)

        except ValueError:
            print("You should enter a number of todo for edit.")
            continue

        except IndexError:
            print(f"There is no item with that number.")
            continue

    else:
        print("Hey, you entered an unknown command!")

print("Bye!")
