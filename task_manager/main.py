from task import Task

print("T A S K   M A N A G E R")
choice = input("new choice?/ yes or no")
if choice == 'yes':
    task_title = input("Give the task's a title")
    task_text = input("Give the task's a text")
    new_task = Task(task_title, task_text)
    new_task.show_task()
    inp
