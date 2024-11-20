from datetime import datetime

class task:
    def __init__(self, task_id, name, category, due_date, priority, status="pending"):
        """
        Represents a task with its attributes.
        
        Args:
            task_id (int): Unique identifier for the task.
            name (str): Name of the task.
            category (str): Task category (e.g., Work, Personal).
            due_date (str): Due date in 'YYYY-MM-DD' format.
            priority (str): task priority (e.g., High, Medium, Low).
            status (str): Current status of the task. Defaults to 'Pending'.
        """
        self.task_id = task_id
        self.name = name
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status
