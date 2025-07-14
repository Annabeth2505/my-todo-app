import streamlit as st
import functions

def add_todo():
    todo= st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title('My Todo App')
st.subheader("Hello. Welcome to Ananya's todo app")
st.write('This app is meant to increase my productivity')
st.text_input(label= '', placeholder= 'Enter a task',
              on_change= add_todo, key= 'new_todo')

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo.{i}")
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[f"todo.{i}"]
        st.rerun()
