# Project: To-Do List Application

# Project Description:
# Create a basic to-do list application in Python that allows the user to add, view, and remove tasks. This project will help you practice using variables, data types, input/output, conditional statements, and loops

to_do_list = []
removed_task = []


def list_tasks():
    if to_do_list:
        print("Tasks:")
        for i, task in enumerate(to_do_list, 1):
            print(f'{i}-{task} ')
    else:
        print("Nothing on your list. =/")


def add_task():
    task = input("Enter the task: ")
    to_do_list.append(task)
    print(f'{task} added to the list.')


def remove_task():
    task_to_remove = input("Enter the task to remove: ")
    if task_to_remove in to_do_list:
        to_do_list.remove(task_to_remove)
        removed_task.append(task_to_remove)
        print(f'{task_to_remove} removed from the list.')
    else:
        print("There's no such thing to remove")


def undo_last_action():
    if removed_task:
        last_removed_task = removed_task.pop()
        to_do_list.append(last_removed_task)
        print(f'{last_removed_task} added back to your list.')
    else:
        print('Nothing to undo.')


def edit_task():
    if not to_do_list:
        print("There are no tasks to edit.")
        return

    list_tasks()

    to_edit = int(input("Enter the index of the task you want to edit: "))

    if 0 <= to_edit < len(to_do_list):
        new_description = input("Enter the new task description: ")
        to_do_list[to_edit] = new_description
        print("Task edited successfully.")
    else:
        print("Invalid task index. Please enter a valid index.")


def save_to_file():
    with open("to_do_list.txt", "w") as file:
        for task in to_do_list:
            file.write(task + "\n")


def load_from_file():
    try:
        with open("to_do_list.txt", "r") as file:
            for line in file:
                task = line.strip()
                to_do_list.append(task)
    except FileNotFoundError:
        print("No saved to-do list found.")


def main():
    load_from_file()  # Load tasks from file (if any).

    while True:
        print("This is your 'to-do list' application:")

        input_choice = input(
            'What you want to do? [List], [Add], [Remove], [Undo], [Edit], [Save], [Quit] -> ').lower()
        if input_choice == 'list':
            list_tasks()
        elif input_choice == "add":
            add_task()
        elif input_choice == 'remove':
            remove_task()
        elif input_choice == 'save':
            save_to_file()
            print("List saved to 'to_do_list.txt'.")
        elif input_choice == 'undo':
            undo_last_action()
        elif input_choice == 'edit':
            edit_task()
        elif input_choice == 'quit':
            print("See ya!")
            break

        else:
            print("Please enter a valid command :)")


if __name__ == "__main__":
    main()
