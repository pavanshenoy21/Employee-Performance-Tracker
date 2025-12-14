import tkinter as tk
from tkinter import ttk, messagebox

from file_handler import create_file, read_data
from operations import add_record, update_record, delete_record, search_record

# ---------- SETUP ----------
create_file()

root = tk.Tk()
root.title("Employee Performance Review Manager")
root.geometry("1000x600")

emp_id = tk.StringVar()
name = tk.StringVar()
punc = tk.StringVar()
team = tk.StringVar()
work = tk.StringVar()
comm = tk.StringVar()
search = tk.StringVar()

# ---------- FUNCTIONS ----------
def clear_entries():
    emp_id.set("")
    name.set("")
    punc.set("")
    team.set("")
    work.set("")
    comm.set("")

def show_all():
    table.delete(*table.get_children())
    for row in read_data():
        table.insert("", "end", values=row)

def add_click():
    try:
        add_record(
            emp_id.get(),
            name.get(),
            int(punc.get()),
            int(team.get()),
            int(work.get()),
            int(comm.get())
        )
        clear_entries()
        show_all()
    except:
        messagebox.showerror("Error", "Enter valid numeric scores (0–10)")

def update_click():
    update_record(
        emp_id.get(),
        name.get(),
        int(punc.get()),
        int(team.get()),
        int(work.get()),
        int(comm.get())
    )
    clear_entries()
    show_all()

def delete_click():
    delete_record(emp_id.get())
    clear_entries()
    show_all()

def search_click():
    table.delete(*table.get_children())
    for row in search_record(search.get()):
        table.insert("", "end", values=row)

def select_row(event):
    selected = table.focus()
    if selected:
        data = table.item(selected)["values"]
        emp_id.set(data[0])
        name.set(data[1])
        punc.set(data[2])
        team.set(data[3])
        work.set(data[4])
        comm.set(data[5])

# ---------- MAIN CODE ----------
form = tk.Frame(root)
form.pack(pady=10)

labels = [
    ("Employee ID", emp_id),
    ("Name", name),
    ("Punctuality (0-10)", punc),
    ("Teamwork (0-10)", team),
    ("Work Quality (0-10)", work),
    ("Communication (0-10)", comm)
]

for i, (text, var) in enumerate(labels):
    tk.Label(form, text=text).grid(row=i, column=0, padx=5, pady=2)
    tk.Entry(form, textvariable=var).grid(row=i, column=1)

# ---------- BUTTONS ----------
btn = tk.Frame(root)
btn.pack()

tk.Button(btn, text="Add", width=12, command=add_click).grid(row=0, column=0, padx=5)
tk.Button(btn, text="Update", width=12, command=update_click).grid(row=0, column=1, padx=5)
tk.Button(btn, text="Delete", width=12, command=delete_click).grid(row=0, column=2, padx=5)

# ---------- SEARCH ----------
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search by ID/Name").grid(row=0, column=0)
tk.Entry(search_frame, textvariable=search).grid(row=0, column=1)

tk.Button(search_frame, text="Search", command=search_click).grid(row=0, column=2, padx=5)
tk.Button(search_frame, text="Show All", command=show_all).grid(row=0, column=3, padx=5)

# ---------- TABLE ----------
columns = (
    "EmployeeID", "Name",
    "Punctuality", "Teamwork",
    "WorkQuality", "Communication",
    "Average"
)

table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=130)

table.pack(pady=10)
table.bind("<<TreeviewSelect>>", select_row)

show_all()
root.mainloop()

