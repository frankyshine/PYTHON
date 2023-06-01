# Project: Simple Todo List

# Importing Required Modules
import json

listfile = 'C:/Users/fadje/OneDrive/PYTHON/Sample projects/Todo_List_Functional/TodoListFile.json'

# Function to Load Todos from File
def load_todos():
    try:
        with open(listfile, 'r') as file:
            todos = json.load(file)
    except FileNotFoundError:
        todos = []
    return todos

# Function to Save Todos to File
def save_todos(todos):
    with open(listfile, 'w') as file:
        json.dump(todos, file)

# Function to Add a New Todo
def add_todo():
    todo = input("Enter a new todo: ")
    todos.append(todo)
    save_todos(todos)
    print("Todo added successfully!")

# Function to Remove a Todo
def remove_todo():
    print_todos()
    choice = int(input("Enter the index of the todo to remove: "))
    if choice >= 0 and choice < len(todos):
        removed_todo = todos.pop(choice)
        save_todos(todos)
        print(f"Removed: {removed_todo}")
    else:
        print("Invalid index!")

# Function to Print Todos
def print_todos():
    print("Todo List:")
    if todos:
        for index, todo in enumerate(todos):
            print(f"{index}. {todo}")
    else:
        print("No todos.")

# Main Program Loop
todos = load_todos()

while True:
    print("\n-- Simple Todo List --")
    print("1. Add Todo")
    print("2. Remove Todo")
    print("3. Print Todos")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_todo()
    elif choice == '2':
        remove_todo()
    elif choice == '3':
        print_todos()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")
