from datetime import datetime
from uuid import uuid4
from utils.enums import Priority, Status, priority_map, status_map


class Task:
    def __init__(self, *args, **kwargs):
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
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            self.task_id = str(uuid4())
            self.name = args[0]
            self.category = args[1]
            try:
                self.due_date = datetime.strptime(
                    args[2], "%Y-%m-%d"
                ).isoformat().split('T')[0]
            except ValueError:
                raise ValueError(
                    f"Invalid due_date format: "
                    f"{args[2]}. Expected 'YYYY-MM-DD'"
                )
            self.priority = Priority.parse_priority(args[3])
            self.status = Status.parse_status(args[4])

    def to_dict(self):
        """Returns a dictionary that contains all attributes of the object"""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority.name,
            "status": self.status.name,
        }

    @classmethod
    def from_dict(cls, task_dict):
        """Returns an instance of Task class created with its key/values"""
        task_dict["priority"] = Priority[task_dict["priority"]]
        task_dict["status"] = Status[task_dict["status"]]
        return cls(**task_dict)

    def __str__(self):
        return (
            f"NAME: {self.name} | CATEGORY: {self.category} | "
            f"DUE: {self.due_date} | "
            f"PRIORITY: {priority_map.get(self.priority.value)} | "
            f"STATUS: {status_map.get(self.status.value)}"
        )

    def is_overdue(self):
        """Checks if the task is overdue."""
        return datetime.strptime(self.due_date, "%Y-%m-%d") < datetime.now()
