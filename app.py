import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_efficiency(habits):
    total_slots = len(habits) * 7
    if total_slots == 0:
        return 0.0
    
    total_completed = 0
    for days in habits.values():
        total_completed += sum(days)
        
    return (total_completed / total_slots) * 100

def display_tracker(habits, weekdays):
    clear_screen()
    print("==========================================================")
    print("        SEN 219 — GROUP 17 DAILY HABIT TRACKER (CMD)      ")
    print("==========================================================")
    
    efficiency = calculate_efficiency(habits)
    print(f"📊 Overall Performance Metrics: {efficiency:.1f}% Efficiency\n")
    
    # Print header row for days
    print(f"{'Habit Name':<30}", end="")
    for day in weekdays:
        print(f"{day:>4}", end="")
    print("\n" + "-" * 60)
    
    # Print each habit and its checkmarks
    for habit_name, days in habits.items():
        # Truncate long names to keep columns aligned
        short_name = habit_name[:28] + ".." if len(habit_name) > 28 else habit_name
        print(f"{short_name:<30}", end="")
        for checked in days:
            mark = "[X]" if checked else "[ ]"
            print(f"{mark:>4}", end="")
        print()
    print("==========================================================")

def main():
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # Default starting habits matching your Flutter app
    habits = {
        "Study for SEN 219": [False] * 7,
        "Review Exam Timetable": [False] * 7,
        "Drink 3L of Water": [False] * 7,
        "Sleep 7+ Hours": [False] * 7,
    }

    while True:
        display_tracker(habits, weekdays)
        print("\n[1] Toggle a Habit Day | [2] Add New Habit | [3] Delete a Habit | [4] Exit")
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            print("\n--- Toggle Habit Day ---")
            habit_list = list(habits.keys())
            for idx, name in enumerate(habit_list):
                print(f"[{idx + 1}] {name}")
                
            try:
                h_choice = int(input("Select habit number: ")) - 1
                if 0 <= h_choice < len(habit_list):
                    selected_habit = habit_list[h_choice]
                    print("1:Mon | 2:Tue | 3:Wed | 4:Thu | 5:Fri | 6:Sat | 7:Sun")
                    day_choice = int(input("Select day number to toggle (1-7): ")) - 1
                    
                    if 0 <= day_choice < 7:
                        # Flip the boolean value (True to False or False to True)
                        habits[selected_habit][day_choice] = not habits[selected_habit][day_choice]
            except ValueError:
                pass

        elif choice == "2":
            new_habit = input("\nEnter name of custom mobile habit: ").strip()
            if new_habit and new_habit not in habits:
                habits[new_habit] = [False] * 7

        elif choice == "3":
            print("\n--- Delete a Habit ---")
            habit_list = list(habits.keys())
            for idx, name in enumerate(habit_list):
                print(f"[{idx + 1}] {name}")
            try:
                del_choice = int(input("Select habit number to delete: ")) - 1
                if 0 <= del_choice < len(habit_list):
                    habits.pop(habit_list[del_choice])
            except ValueError:
                pass

        elif choice == "4":
            print("\nExiting tracker. Good luck with your exams!")
            break

if __name__ == "__main__":
    main()
