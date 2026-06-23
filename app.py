import customtkinter as ctk
from tkinter import messagebox

# --- STYLE THE THEME ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ModernHabitTracker(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("SEN 219: Open Source Software Development — Group 17")
        self.geometry("600x700")
        self.resizable(False, False)

        # --- DEFAULT HABITS ---
        self.habits = {
            "Study for SEN 219": [False] * 7,
            "Review Exam Timetable": [False] * 7,
            "Drink 3L of Water": [False] * 7,
            "Sleep 7+ Hours": [False] * 7
        }
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.checkbox_objects = {}

        self.create_widgets()

    def create_widgets(self):
        # Header Box
        self.header_frame = ctk.CTkFrame(self, fg_color="#1F6AA5", corner_radius=10)
        self.header_frame.pack(fill="x", padx=20, pady=15, ipady=10)
        
        ctk.CTkLabel(self.header_frame, text="SEN 219: Open Source Software Development", font=("Arial", 14, "bold"), text_color="white").pack(pady=2)
        ctk.CTkLabel(self.header_frame, text="Practical Project — Group 17 Contribution", font=("Arial", 11), text_color="#E0E0E0").pack()
        
        ctk.CTkLabel(self, text="🎓 Student Daily Habit Tracker", font=("Arial", 20, "bold")).pack(pady=10)

        # Main Workspace Grid Container
        self.main_container = ctk.CTkFrame(self, corner_radius=15)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=10)

        self.render_habit_interface()

        # Modern Analytics Banner
        self.analytics_frame = ctk.CTkFrame(self, height=60, corner_radius=10, border_width=1, border_color="#1F6AA5")
        self.analytics_frame.pack(fill="x", padx=20, pady=10)
        
        self.score_label = ctk.CTkLabel(self.analytics_frame, text="Overall Weekly Efficiency Score: 0.0%", font=("Arial", 14, "bold"), text_color="#2ECC71")
        self.score_label.pack(pady=15)

        # Input Row
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=15)
        
        self.habit_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter a new student habit...", width=250, font=("Arial", 12))
        self.habit_entry.pack(side="left", padx=10)
        
        self.add_btn = ctk.CTkButton(self.input_frame, text="Add Custom Habit", command=self.add_habit, font=("Arial", 12, "bold"))
        self.add_btn.pack(side="left", padx=5)

        # Legal Open Source Footer
        ctk.CTkLabel(self, text="Released under the official open-source MIT License. Managed by Group 17 Leader.", font=("Arial", 10, "italic"), text_color="gray").pack(side="bottom", pady=8)
        
        self.calculate_progress()

    def render_habit_interface(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

        for col_idx, day in enumerate(self.days):
            ctk.CTkLabel(self.main_container, text=day, font=("Arial", 11, "bold"), text_color="#1F6AA5").grid(row=0, column=col_idx+1, padx=12, pady=10)

        for row_idx, (habit, completions) in enumerate(self.habits.items()):
            ctk.CTkLabel(self.main_container, text=habit, font=("Arial", 12, "bold"), anchor="w", width=180).grid(row=row_idx+1, column=0, sticky="w", padx=15, pady=10)
            
            self.checkbox_objects[habit] = []
            for col_idx in range(7):
                cb = ctk.CTkCheckBox(self.main_container, text="", width=20, height=20, checkbox_width=20, checkbox_height=20, command=self.calculate_progress)
                if completions[col_idx]:
                    cb.select()
                cb.grid(row=row_idx+1, column=col_idx+1, padx=12, pady=10)
                self.checkbox_objects[habit].append(cb)

    def add_habit(self):
        new_habit = self.habit_entry.get().strip()
        if new_habit and new_habit not in self.habits:
            self.habits[new_habit] = [False] * 7
            self.habit_entry.delete(0, 'end')
            self.render_habit_interface()
            self.calculate_progress()
        elif not new_habit:
            messagebox.showwarning("System Notice", "Habit description cannot be blank!")

    def calculate_progress(self):
        total_slots = len(self.habits) * 7
        total_done = 0
        
        for habit in self.habits:
            for col_idx in range(7):
                is_checked = self.checkbox_objects[habit][col_idx].get()
                self.habits[habit][col_idx] = bool(is_checked)
                if is_checked:
                    total_done += 1
                    
        score = (total_done / total_slots) * 100 if total_slots > 0 else 0
        self.score_label.configure(text=f"Overall Weekly Efficiency Score: {round(score, 1)}%")

if __name__ == "__main__":
    app = ModernHabitTracker()
    app.mainloop()