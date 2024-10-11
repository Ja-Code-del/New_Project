class Task:
    counter = 0

    def __init__(self, title, text, moment):
        Task.counter += 1
        self.task_id = Task.counter
        self.title = title
        self.text = text
        self.moment = moment


    def show_task(self):
        print("------------------------------------------")
        print(self.title)
        print(self.text)
        print("------------------------------------------")

    def modify_task(self, id, new_text):
        self.text = new_text

    def counter(self):
        self.counter += 1