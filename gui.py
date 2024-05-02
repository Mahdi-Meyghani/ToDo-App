import todo_functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-Do:")
input_text = sg.InputText(tooltip="Enter a To-Do", key="-IN-")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_text, add_button]],
                   font=("Arial", 12))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = todo_functions.get_todos()
            new_item = values["-IN-"] + "\n"
            todos.append(new_item)
            todo_functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
