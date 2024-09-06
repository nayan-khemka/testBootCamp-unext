# task_manager.py
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, str) or not task:
            raise ValueError("Task must be a non-empty string")
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            raise ValueError("Task not found")

if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Buy groceries")
    manager.add_task("Read a book")
    print("Tasks:", manager.view_tasks())
    manager.delete_task("Buy groceries")
    print("Tasks after deletion:", manager.view_tasks())
