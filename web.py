import streamlit as st
import todo_functions


todos = todo_functions.get_todos()
def add_todo():
    todo = st.session_state["new todo"] + "\n"
    print(todo)
    todos.append(todo)
    todo_functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This Is My Todo App.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo", key="new todo",
              on_change=add_todo)
print("Hello")
st.session_state
