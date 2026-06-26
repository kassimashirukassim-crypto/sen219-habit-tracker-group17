import tkinter as tk
from tkinter import messagebox, ttk

class HabitTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SEN 219 — Group 17 Habit Tracker")
        self.root.geometry("650x550")
        self.root.configure(bg="#121212") # Dark mode background

        # Data structure for habits
        self.weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.habits = {
            "Study for SEN 219": [False]*7,
            "Review Exam Timetable": [False]*7,
            "Drink 3L of Water": [False]*7,
            "Sleep 7+ Hours": [False]*7
        }
        
        self.checkbox_objects = {}

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("TLabel", background="#121212", foreground="white")
        
        # --- Top Title ---
        title_label = tk.Label(root, text="SEN 219 — Group 17 Tracker", font=("Arial", 16, "bold"), fg="white", bg="#004d40", pady=10)
        title_label.pack(fill=tk.X)

        # --- Metrics Card ---
        self.metrics_frame = tk.Frame(root, bg="#1e1e1e", bd=2, relief=tk.GROOVE)
        self.metrics_frame.pack(fill=tk.X, padx=15, pady=10)
        
        metrics_title = tk.Label(self.metrics_frame, text="📊 Overall Performance Metrics", font=("Arial", 11, "bold"), fg="#b0bec5", bg="#1e1e1e")
        metrics_title.pack(pady=2)
        
        self.efficiency_label = tk.Label(self.metrics_frame, text="0.0% Efficiency", font=("Arial", 18, "bold"), fg="#69f0ae", bg="#1e1e1e")
        self.efficiency_label.pack(pady=5)

        # --- Habits Container ---
        self.scroll_frame = tk.Frame(root, bg="#121212")
        self.scroll_frame.pack(fill=tk.BOTH, expand=True, padx=15)
        
        self.render_habits_interface()
        self.update_efficiency()

        # --- Bottom Input Row ---
        bottom_frame = tk.Frame(root, bg="#121212")
        bottom_frame.pack(fill=tk.X, padx=15, pady=15)

        self.new_habit_entry = tk.Entry(bottom_frame, font=("Arial", 11), bg="#2c2c2c", fg="white", insertbackground="white", bd=1)
        self.new_habit_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=4, padx=(0, 10))
        self.new_habit_entry.insert(0, "Add Custom Mobile Habit...")
        self.new_habit_entry.bind("<FocusIn>", lambda args: self.new_habit_entry.delete(0, tk.END) if self.new_habit_entry.get() == "Add Custom Mobile Habit..." else None)

        add_btn = tk.Button(bottom_frame, text="＋ Add", font=("Arial", 10, "bold"), bg="#00796b", fg="white", activebackground="#004d40", activeforeground="white", bd=0, padx=15, command=self.add_habit)
        add_btn.pack(side=tk.RIGHT)

    def render_habits_interface(self):
        # Clear existing layout components
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
        self.checkbox_objects.clear()

        # Generate rows for each habit
        for habit_name, schedule in self.habits.items():
            habit_card = tk.Frame(self.scroll_frame, bg="#1e1e1e", bd=1, relief=tk.RIDGE)
            habit_card.pack(fill=tk.X, pady=6)

            # Header row inside card (Habit Name + Edit/Delete buttons)
            header_row = tk.Frame(habit_card, bg="#1e1e1e")
            header_row.pack(fill=tk.X, padx=8, pady=4)

            lbl = tk.Label(header_row, text=habit_name, font=("Arial", 11, "bold"), fg="white", bg="#1e1e1e", anchor="w")
            lbl.pack(side=tk.LEFT, fill=tk.X, expand=True)

            edit_btn = tk.Button(header_row, text="✏️", font=("Arial", 9), bg="#2c2c2c", fg="gray", activebackground="#3c3c3c", bd=0, command=lambda h=habit_name: self.edit_habit(h))
            edit_btn.pack(side=tk.LEFT, padx=4)

            del_btn = tk.Button(header_row, text="🗑️", font=("Arial", 9), bg="#2c2c2c", fg="red", activebackground="#3c3c3c", bd=0, command=lambda h=habit_name: self.delete_habit(h))
            del_btn.pack(side=tk.LEFT, padx=2)

            # Days Checkbox Grid Row
            grid_row = tk.Frame(habit_card, bg="#1e1e1e")
            grid_row.pack(fill=tk.X, padx=5, pady=5)

            self.checkbox_objects[habit_name] = []
            for i, day in enumerate(self.weekdays):
                day_box = tk.Frame(grid_row, bg="#1e1e1e")
                day_box.pack(side=tk.LEFT, fill=tk.X, expand=True)

                day_lbl = tk.Label(day_box, text=day, font=("Arial", 8), fg="gray", bg="#1e1e1e")
                day_lbl.pack()

                var = tk.BooleanVar(value=schedule[i])
                cb = tk.Checkbutton(day_box, variable=var, bg="#1e1e1e", activebackground="#1e1e1e", selectcolor="#2c2c2c", command=self.update_efficiency)
                cb.pack()
                
                self.checkbox_objects[habit_name].append(var)

    def update_efficiency(self):
        total_slots = len(self.checkbox_objects) * 7
        if total_slots == 0:
            self.efficiency_label.config(text="0.0% Efficiency")
            return

        checked_count = 0
        for habit_name, vars_list in self.checkbox_objects.items():
            for i, var in enumerate(vars_list):
                self.habits[habit_name][i] = var.get() # Sync state back to data map
                if var.get():
                    checked_count += 1

        score = (checked_count / total_slots) * 100
        self.efficiency_label.config(text=f"{score:.1f}% Efficiency")

    def add_habit(self):
        name = self.new_habit_entry.get().strip()
        if name and name != "Add Custom Mobile Habit...":
            if name not in self.habits:
                self.habits[name] = [False]*7
                self.new_habit_entry.delete(0, tk.END)
                self.render_habits_interface()
                self.update_efficiency()
            else:
                messagebox.showwarning("Warning", "This habit already exists!")

    def delete_habit(self, habit_name):
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete '{habit_name}'?"):
            del self.habits[habit_name]
            self.render_habits_interface()
            self.update_efficiency()

    def edit_habit(self, old_name):
        # Quick popup window to rename habit text
        edit_win = tk.Toplevel(self.root)
        edit_win.title("Edit Habit")
        edit_win.geometry("300x120")
        edit_win.configure(bg="#1e1e1e")
        
        tk.Label(edit_win, text="Rename Habit Name:", fg="white", bg="#1e1e1e", pady=5).pack()
        ent = tk.Entry(edit_win, font=("Arial", 10))
        ent.pack(pady=5, padx=10, fill=tk.X)
        ent.insert(0, old_name)
        
        def save_change():
            new_name = ent.get().strip()
            if new_name and new_name != old_name:
                self.habits[new_name] = self.habits.pop(old_name)
                edit_win.destroy()
                self.render_habits_interface()
                self.update_efficiency()
            else:
                edit_win.destroy()

        tk.Button(edit_win, text="Save", bg="#00796b", fg="white", bd=0, padx=10, command=save_change).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()
    
