import streamlit as st
import todo_functions
import time
from streamlit_autorefresh import st_autorefresh

st_autorefresh()
now = time.strftime("%a, %b %d, %Y at %H:%M:%S")
todos = todo_functions.get_todos()


def add_todo():
    new_todo = st.session_state["new todo"] + "\n"
    todos.append(new_todo)
    todo_functions.write_todos(todos)
    st.session_state["new todo"] = ""


st.title("My Todo App")
st.subheader("This Is My Todo App.")
st.write("This app is to increase your productivity.")
st.subheader(now)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo.strip()}-{index}")
    if checkbox:
        todos.pop(index)
        todo_functions.write_todos(todos)
        del st.session_state[f"{todo.strip()}-{index}"]
        st.rerun()

st.text_input(label="", placeholder="Add new todo", key="new todo",
              on_change=add_todo)
