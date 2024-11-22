from datetime import datetime
from uuid import uuid4


class Task:
    def __init__(self, name, category, due_date, priority, status="pending"):
        """
        Represents a task with its attributes.

        Args:
            task_id (str): Unique identifier for the task.
            name (str): Name of the task.
            category (str): Task category (e.g., Work, Personal).
            due_date (str): Due date in 'YYYY-MM-DD' format.
            priority (str): task priority (e.g., High, Medium, Low).
            status (str): Current status of the task. Defaults to 'Pending'.
        """
        self.task_id = str(uuid4())
        self.name = name
        self.category = category
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").isoformat().split('T')[0]
        self.priority = priority
        self.status = status

    def __str__(self):
        return (
            f"NAME: {self.name} | CATEGORY: {self.category} | "
            f"DUE: {self.due_date} | PRIORITY: {self.priority} | "
            f"STATUS: {self.status}"
        )

    def is_overdue(self):
        """Checks if the task is overdue."""
        return self.due_date < datetime.now()
