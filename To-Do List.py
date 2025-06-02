import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.configure(bg="#f5f5f5")

        self.tasks = []

        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=10, selectbackground="#A3E4D7")
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark as Done", command=self.mark_done, bg="#2196F3", fg="white")
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white")
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, t in enumerate(self.tasks):
            display_text = f"{t['task']} ✅" if t['done'] else t['task']
            self.task_listbox.insert(tk.END, display_text)

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = True
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Please select a task to mark as done.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
