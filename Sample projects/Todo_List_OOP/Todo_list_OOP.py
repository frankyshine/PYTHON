import pickle

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

    def save_list(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_list(self, filename):
        with open(filename, 'rb') as file:
            self.tasks = pickle.load(file)

def main():
    todo_list = TodoList()

    while True:
        print("\n--- Todo List ---")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Save list")
        print("5. Load list")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
            print("Task removed successfully.")
        elif choice == '3':
            tasks = todo_list.get_tasks()
            if tasks:
                print("\nTasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks.")
        elif choice == '4':
            filename = input("Enter filename to save: ")
            todo_list.save_list(filename)
            print("List saved successfully.")
        elif choice == '5':
            filename = input("Enter filename to load: ")
            todo_list.load_list(filename)
            print("List loaded successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
