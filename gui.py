import todo_functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-Do:")
input_text = sg.InputText(tooltip="Enter a To-Do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_text, add_button]])
window.read()
print("Hi there !")
window.close()
