class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, habit_name):
        self.habits[habit_name] = []

    def mark_completed(self, habit_name, date):
        if habit_name in self.habits:
            self.habits[habit_name].append(date)
        else:
            print(f"Habit '{habit_name}' not found.")

    def display_habits(self):
        for habit, dates in self.habits.items():
            print(f"{habit}: {', '.join(dates)}")

def main():
    tracker = HabitTracker()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Mark Habit Completed")
        print("3. Display Habits")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            habit_name = input("Enter the habit name: ")
            tracker.add_habit(habit_name)
            print(f"Habit '{habit_name}' added.")
        elif choice == "2":
            habit_name = input("Enter the habit name: ")
            date = input("Enter the date (DD-MM-YYYY): ")
            tracker.mark_completed(habit_name, date)
            print(f"Habit '{habit_name}' marked as completed on {date}.")
        elif choice == "3":
            tracker.display_habits()
        elif choice == "4":
            print("Exiting Habit Tracker.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
