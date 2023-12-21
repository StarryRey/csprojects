#  To-Do List in Python

def display_todo_list(todo_list): #Function to-do list
    print("To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print()

# Function to add a task to the to-do list
def add_task(todo_list, new_task):
    todo_list.append(new_task)
    print(f"Task '{new_task}' added to the to-do list.\n")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.\n")
    else:
        print("Invalid task index. Please enter a valid index.\n")

# Main function to manage the to-do list
def main():
    todo_list = []

    while True:
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            new_task = input("Enter the task: ")
            add_task(todo_list, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        
        elif choice == '4':
            print("Quitting the to-do list project. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
