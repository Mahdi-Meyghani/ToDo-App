import todo_functions
import PySimpleGUI as sg
import time


sg.theme("DarkTeal12")

time_label = sg.Text(key="-TM-")
label = sg.Text("Type in a To-Do:")
input_text = sg.InputText(tooltip="Enter a To-Do", key="-IN-")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
list_box = sg.Listbox(values=todo_functions.get_todos(),
                      size=(45, 10),
                      enable_events=True,
                      key="-LIST-")

window = sg.Window("My To-Do App",
                   layout=[[time_label],
                           [label],
                           [input_text, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Arial", 15))

while True:
    event, values = window.read(timeout=200)
    now = time.strftime("%a, %b %d, %Y, %H:%M:%S")
    window["-TM-"].update(now)
    match event:
        case "-LIST-":
            item = values["-LIST-"][0]
            window["-IN-"].update(item)
        case "Add":
            todos = todo_functions.get_todos()
            new_todo = values["-IN-"] + "\n"
            todos.append(new_todo)
            todo_functions.write_todos(todos)

            window["-LIST-"].update(todos)
        case "Edit":
            try:
                todos = todo_functions.get_todos()

                todo_to_edited = values["-LIST-"][0]
                index = todos.index(todo_to_edited)
                new_todo = values["-IN-"]
                todos[index] = new_todo

                todo_functions.write_todos(todos)

                window["-LIST-"].update(todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Arial", 13))
        case "Complete":
            try:
                todo_to_complete = values["-LIST-"][0]
                todos = todo_functions.get_todos()
                todos.remove(todo_to_complete)
                todo_functions.write_todos(todos)
                window["-LIST-"].update(todos)
                window["-IN-"].update("")
            except IndexError:
                sg.popup("Please select an item first.", font=("Arial", 13))
            except ValueError:
                sg.popup("Please select an item first.", font=("Arial", 13))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
