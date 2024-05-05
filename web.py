import streamlit as st
import todo_functions

st.title("My Todo App")
st.subheader("This Is My Todo App.")
st.write("This app is to increase your productivity.")

todos = todo_functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo")

