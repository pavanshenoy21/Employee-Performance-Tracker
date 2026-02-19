import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from file_handler import create_file, read_data
from operations import add_record, update_record, delete_record, search_record

# SETUP
create_file()

# Visuals figure size (width, height) in inches — change this to resize charts window
VIS_FIGSIZE = (18, 12)

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

# FUNCTIONS
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

def show_performance_charts():
    """Display 4 matplotlib charts showing score distribution for all performance metrics"""
    data = read_data()
    
    if not data:
        messagebox.showwarning("No Data", "No employee records found.")
        return
    
    # Extract scores and convert to integers
    punctuality = [int(row[2]) for row in data]
    teamwork = [int(row[3]) for row in data]
    work_quality = [int(row[4]) for row in data]
    communication = [int(row[5]) for row in data]
    
    # Create 2x2 subplot layout
    fig, axes = plt.subplots(2, 2, figsize=VIS_FIGSIZE)
    fig.suptitle('Employee Performance Review - Score Distribution', fontsize=16, fontweight='bold')
    
    metrics = [
        (punctuality, 'Punctuality', axes[0, 0]),
        (teamwork, 'Teamwork', axes[0, 1]),
        (work_quality, 'Work Quality', axes[1, 0]),
        (communication, 'Communication', axes[1, 1])
    ]
    
    for scores, metric_name, ax in metrics:
        # Create histogram showing score distribution
        bins = range(4, 12)  # Bins from 4 to 11 (scores are 5-10)
        counts, edges, patches = ax.hist(scores, bins=bins, color='steelblue', 
                                         edgecolor='black', linewidth=1.2, alpha=0.7)
        
        # Color the highest bar differently
        max_count_idx = counts.argmax()
        patches[max_count_idx].set_color('green')
        patches[max_count_idx].set_alpha(0.9)
        
        # Add value labels on top of bars (slightly above bar to avoid overlap)
        for count, patch in zip(counts, patches):
            if count > 0:
                height = patch.get_height()
                ax.text(patch.get_x() + patch.get_width()/2., height + 0.3,
                        f'{int(count)}',
                        ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        ax.set_xlabel('Score (0-10)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Number of Employees', fontsize=11, fontweight='bold')
        ax.set_title(f'{metric_name} Score Distribution', fontsize=12, fontweight='bold')
        ax.set_xticks(range(5, 11))
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Calculate statistics
        avg_score = round(sum(scores) / len(scores), 2)
        max_score = max(scores)
        min_score = min(scores)
        
        # Add compact stats box in upper-right to reduce overlap
        stats_text = f'Avg: {avg_score}\nMax: {max_score}\nMin: {min_score}\nCount: {len(scores)}'
        ax.text(0.98, 0.98, stats_text, transform=ax.transAxes,
            fontsize=9, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85, edgecolor='black'))
    
    # Leave room for the suptitle and add spacing between subplots
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    fig.subplots_adjust(hspace=0.35, wspace=0.25)

    # Try to maximize the matplotlib window (works on common backends on Windows)
    try:
        mng = plt.get_current_fig_manager()
        try:
            mng.window.state('zoomed')
        except Exception:
            try:
                mng.window.showMaximized()
            except Exception:
                pass
    except Exception:
        pass

    plt.show()

#FORM
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

#BUTTONS
btn = tk.Frame(root)
btn.pack()

tk.Button(btn, text="Add", width=12, command=add_click).grid(row=0, column=0, padx=5)
tk.Button(btn, text="Update", width=12, command=update_click).grid(row=0, column=1, padx=5)
tk.Button(btn, text="Delete", width=12, command=delete_click).grid(row=0, column=2, padx=5)
tk.Button(btn, text="Visuals", width=12, command=show_performance_charts).grid(row=0, column=3, padx=5)

#SEARCH
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search by ID/Name").grid(row=0, column=0)
tk.Entry(search_frame, textvariable=search).grid(row=0, column=1)

tk.Button(search_frame, text="Search", command=search_click).grid(row=0, column=2, padx=5)
tk.Button(search_frame, text="Show All", command=show_all).grid(row=0, column=3, padx=5)

#TABLE
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
