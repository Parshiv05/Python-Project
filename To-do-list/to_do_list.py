import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List Application")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=5)

root.mainloop()