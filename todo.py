import os

class TodoApp:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file if it exists"""
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    task = line.strip()  # Remove whitespace and newlines
                    if task:  # Only add non-empty tasks
                        self.tasks.append(task)
            print(f"Loaded {len(self.tasks)} tasks from {self.filename}")
        except FileNotFoundError:
            print(f"No existing task file found. Starting with empty list.")
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')
            print("Tasks saved successfully!")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self):
        """Add a new task to the list"""
        task = input("Enter a new task: ").strip()
        if task:
            self.tasks.append(task)
            print(f"Task '{task}' added successfully!")
            self.save_tasks()
        else:
            print("Task cannot be empty!")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found!")
            return
        
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print(f"\nTotal tasks: {len(self.tasks)}")
    
    def remove_task(self):
        """Remove a task from the list"""
        if not self.tasks:
            print("No tasks to remove!")
            return
        
        self.view_tasks()
        try:
            task_num = int(input("\nEnter task number to remove: "))
            if 1 <= task_num <= len(self.tasks):
                removed_task = self.tasks.pop(task_num - 1)  # Remove by index
                print(f"Task '{removed_task}' removed successfully!")
                self.save_tasks()
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def remove_task_by_name(self):
        """Remove a task by searching for its name"""
        if not self.tasks:
            print("No tasks to remove!")
            return
        
        search_term = input("Enter task name or part of it to remove: ").strip().lower()
        matching_tasks = []
        
        for i, task in enumerate(self.tasks):
            if search_term in task.lower():
                matching_tasks.append((i, task))
        
        if not matching_tasks:
            print("No matching tasks found!")
            return
        
        if len(matching_tasks) == 1:
            index, task = matching_tasks[0]
            self.tasks.pop(index)
            print(f"Task '{task}' removed successfully!")
            self.save_tasks()
        else:
            print("\nMultiple matching tasks found:")
            for i, (index, task) in enumerate(matching_tasks, 1):
                print(f"{i}. {task}")
            
            try:
                choice = int(input("Enter number of task to remove: "))
                if 1 <= choice <= len(matching_tasks):
                    index, task = matching_tasks[choice - 1]
                    self.tasks.pop(index)
                    print(f"Task '{task}' removed successfully!")
                    self.save_tasks()
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a valid number!")
    
    def insert_task(self):
        """Insert a task at a specific position"""
        if not self.tasks:
            self.add_task()
            return
        
        self.view_tasks()
        try:
            position = int(input("\nEnter position to insert task (1 to {}): ".format(len(self.tasks) + 1)))
            if 1 <= position <= len(self.tasks) + 1:
                task = input("Enter the task: ").strip()
                if task:
                    self.tasks.insert(position - 1, task)  # Insert at specific position
                    print(f"Task '{task}' inserted at position {position}!")
                    self.save_tasks()
                else:
                    print("Task cannot be empty!")
            else:
                print("Invalid position!")
        except ValueError:
            print("Please enter a valid number!")
    
    def clear_all_tasks(self):
        """Clear all tasks"""
        if not self.tasks:
            print("No tasks to clear!")
            return
        
        confirm = input(f"Are you sure you want to delete all {len(self.tasks)} tasks? (y/N): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            self.tasks.clear()
            self.save_tasks()
            print("All tasks cleared!")
        else:
            print("Operation cancelled.")
    
    def show_menu(self):
        """Display the main menu"""
        print("\n" + "="*40)
        print("       TO-DO LIST MANAGER")
        print("="*40)
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Remove task by number")
        print("4. Remove task by name")
        print("5. Insert task at position")
        print("6. Clear all tasks")
        print("7. Exit")
        print("="*40)
    
    def run(self):
        """Main application loop"""
        print("Welcome to To-Do List Manager!")
        
        while True:
            self.show_menu()
            
            try:
                choice = input("\nEnter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.view_tasks()
                elif choice == '2':
                    self.add_task()
                elif choice == '3':
                    self.remove_task()
                elif choice == '4':
                    self.remove_task_by_name()
                elif choice == '5':
                    self.insert_task()
                elif choice == '6':
                    self.clear_all_tasks()
                elif choice == '7':
                    print("Thank you for using To-Do List Manager!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1-7.")
            
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == "__main__":
    app = TodoApp()
    app.run()