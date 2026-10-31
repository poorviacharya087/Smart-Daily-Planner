import tkinter as tk
from tkinter import messagebox
from datetime import date

root = tk.Tk()
root.title("Smart Daily Planner")
root.geometry("450x550")
root.configure(bg="#F3E8FF")

tasks = []

def add_task():
    task = task_entry.get().strip()

    if not task:
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    status = tk.BooleanVar(value=False)

    row = tk.Frame(root, bg="#F3E8FF")
    row.pack(anchor="w", padx=20, pady=5, fill="x")

    checkbox = tk.Checkbutton(
        row,
        text=task,
        variable=status,
        bg="#F3E8FF",
        font=("Arial", 12),
        selectcolor="#D8B4FE"
    )
    checkbox.pack(side="left")

    tasks.append({
        "name": task,
        "status": status,
        "row": row
    })

    task_entry.delete(0, tk.END)

def complete_task():
    selected = [
        task for task in tasks
        if task["status"].get()
    ]

    if not selected:
        messagebox.showinfo(
            "Information",
            "Please tick a task first!"
        )
        return

    for task in selected:
        task["row"].config(bg="#BBF7D0")

        for widget in task["row"].winfo_children():
            widget.config(bg="#BBF7D0")

    messagebox.showinfo(
        "Success",
        "Selected task marked as completed!"
    )

def delete_task():
    selected = [task for task in tasks if task["status"].get()]

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please tick the task you want to delete!"
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete the selected task(s)?"
    )

    if confirm:
        for task in selected:
            task["row"].destroy()
            tasks.remove(task)

heading = tk.Label(
    root,
    text="✨ Smart Daily Planner ✨",
    font=("Arial", 18, "bold"),
    bg="#F3E8FF",
    fg="#6B21A8"
)
heading.pack(pady=15)

tk.Label(
    root,
    text="Today's Date: " + str(date.today()),
    bg="#F3E8FF"
).pack()

task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=15)

tk.Button(
    root,
    text="➕ Add Task",
    command=add_task,
    bg="#A78BFA",
    fg="white",
    width=18
).pack(pady=5)

tk.Button(
    root,
    text="✅ Complete Task",
    command=complete_task,
    bg="#86EFAC",
    width=18
).pack(pady=5)

#Delete Task button
tk.Button(root,text="Delete Task",command=delete_task,bg="#FCA5A5",width=20).pack(pady=5)

#Task Display Area
task_frame=tk.Frame(root,bg="#F3E8FF")
task_frame.pack(side="left",anchor="nw", padx=10,pady=10)
root.mainloop()