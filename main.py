import streamlit as st
import backend

def goappend():
    newitem = st.session_state['add']
    backend.appending("todo.txt", newitem)
    st.session_state['add'] = ""

st.title("Todo App")

st.text_input(label="", placeholder="Add a new Todo...",
              on_change=goappend, key="add")

st.subheader("The list of tasks:")
tasks = backend.reading("todo.txt")
for index, item in enumerate(tasks):
    clean_item = item.strip()  # Remove any newline characters
    checkbox = st.checkbox(clean_item, key=f"todo_{index}")
    if checkbox:
        backend.appending("inprogress.txt", clean_item)
        tasks.pop(index)
        backend.writing("todo.txt", tasks)
        key_to_delete = f"todo_{index}"
        if key_to_delete in st.session_state:
            del st.session_state[key_to_delete]
        st.rerun()

st.subheader("In Progress Tasks:")
tasks2 = backend.reading("inprogress.txt")
for index, item2 in enumerate(tasks2):
    clean_item2 = item2.strip()
    checkbox = st.checkbox(clean_item2, key=f"inprogress_{index}")
    if checkbox:
        backend.appending("done.txt", clean_item2)
        tasks2.pop(index)
        backend.writing("inprogress.txt", tasks2)
        key_to_delete = f"inprogress_{index}"
        if key_to_delete in st.session_state:
            del st.session_state[key_to_delete]
        st.rerun()

st.subheader("Completed Tasks:")
tasks3 = backend.reading("done.txt")
for item3 in tasks3:
    st.write(item3.strip())  # Clean up display of completed tasks
