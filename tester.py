from tasks.task import Task
from tasks.task_manager import TaskManager


manager = TaskManager()

manager.add_task("Finish Capstone", "Work", "2024-11-25", "High")
manager.add_task("Buy Groceries", "Personal", "2024-11-20", "Medium")

print(manager.view_tasks())
