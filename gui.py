import todo_functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-Do:")
input_text = sg.InputText(tooltip="Enter a To-Do", key="-IN-")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=todo_functions.get_todos(),
                      size=(45, 10),
                      enable_events=True,
                      key="-LIST-")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_text, add_button], [list_box, edit_button]],
                   font=("Arial", 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["-LIST-"])
    match event:
        case "Add":
            todos = todo_functions.get_todos()
            new_todo = values["-IN-"] + "\n"
            todos.append(new_todo)
            todo_functions.write_todos(todos)

            window["-LIST-"].update(todos)
        case "Edit":
            todos = todo_functions.get_todos()

            todo_to_edited = values["-LIST-"][0]
            index = todos.index(todo_to_edited)
            new_todo = values["-IN-"]
            todos[index] = new_todo

            todo_functions.write_todos(todos)

            window["-LIST-"].update(todos)
        case "-LIST-":
            item = values["-LIST-"][0]
            window["-IN-"].update(item)
        case sg.WIN_CLOSED:
            break

window.close()
