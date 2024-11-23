from tasks.task import Task
import json
from utils.enums import Priority, Status


def log_call(func):
    """
    Decorator to log method calls.

    Args:
        func (function): Function to be wrapped.

    Returns:
        function: Wrapped function with logging.
    """
    def wrapper(*args, **kwargs):
        func_args = args[1:] if len(args) > 0 else args
        formatted_kwargs = ", ".join(f"{k}: {v}" for k, v in kwargs.items())
        print(
            f"calling {func.__name__} ",
            f"with args: {func_args}, kwargs: {{ {formatted_kwargs} }}"
        )
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


class TaskManager:
    __file_path = "tasks.json"
    __tasks = []

    @log_call
    def add_task(self, name, category, due_date, priority, status="Pending"):
        """
        Adds a new task to the task list.

        Args:
            name (str): Name of the task.
            category (str): Task category.
            due_date (str): Due date in 'YYYY-MM-DD' format.
            priority (str): Task priority.
            status (str): Initial status. Defaults to 'Pending'.
        """
        priority_enum = Priority(priority)
        status_enum = Status(status)
        task = Task(name, category, due_date, priority_enum, status_enum)
        self.__tasks.append(task)
        return task

    @log_call
    def update_task(self, task_id, **kwargs):
        """
        Updates an existing task.

        Args:
            task_id (str): ID of the task to update.
            **kwargs: Key-value pairs of attributes to update.

        Returns:
            bool: True if the task was updated, False otherwise.
        """
        task = self._find_task_by_id(task_id)
        if not task:
            return False

        for key, value in kwargs.items():
            if hasattr(task, key):
                if key == "priority":
                    value = Priority(value)
                elif key == "status":
                    value = Status(value)
                setattr(task, key, value)

        return True

    def delete_task(self, task_id):
        """
        Deletes a task by ID.

        Args:
            task_id (str): ID of the task to delete.

        Returns:
            bool: True if the task was deleted, False otherwise.
        """
        task = self._find_task_by_id(task_id)
        if task:
            self.__tasks.remove(task)
            return True
        return False

    def all_tasks(self):
        """
        Returns a list of all tasks.

        Returns:
            list: list of tasks.
        """
        return self.__tasks

    def save(self):
        """Serializes the list __tasks to the file."""
        with open(self.__file_path, "w") as f:
            json.dump([task.to_dict() for task in self.__tasks], f)

    def reload(self):
        """Deserializes the tasks inside file to the list __tasks."""
        try:
            with open(self.__file_path, "r") as f:
                tasks = json.load(f)
            self.__tasks = [Task.from_dict(task) for task in tasks]
        except FileNotFoundError:
            self.__tasks = []

    def filter_tasks(self, **criteria):
        """
        Filters tasks based on given criteria.

        Args:
            **criteria: Key-value pairs
            to filter tasks (e.g., status="Pending").

        Returns:
            list: List of tasks matching the criteria.
        """
        def matches(task):
            return all(
                getattr(task, key) == value for key, value in criteria.items()
            )

        return list(filter(matches, self.__tasks))

    def sort_tasks(self, key="due_date", reverse=False):
        """
        Sorts tasks by a specific key.

        Args:
            key (str): Attribute to sort by (default: "due_date").
            reverse (bool): Sort in descending order if True.

        Returns:
            list: Sorted list of tasks
        """
        if key not in ["due_date", "priority", "status", "name"]:
            raise ValueError(f"Cannot sort by invalid key: {key}")
        if key == "priority" or key == "status":
            return sorted(
                self.__tasks,
                key=lambda task: getattr(task, key).value,
                reverse=reverse
            )
        return sorted(
            self.__tasks, key=lambda task: getattr(task, key), reverse=reverse
        )

    def update_tasks_concurrently(self, updates):
        """
        Updates multiple tasks concurrently.

        Args:
            updates (list): List of tuples (task_id, {attribute updates}).

        Returns:
            list: List of booleans indicating success for each update.
        """
        from concurrent.futures import ThreadPoolExecutor

        def update_task(args):
            task_id, attrs = args
            return self.update_task(task_id, **attrs)

        with ThreadPoolExecutor() as executor:
            results = list(executor.map(update_task, updates))
        return results

    def _find_task_by_id(self, task_id):
        """Finds a task by its ID"""
        for task in self.__tasks:
            if task.task_id == task_id:
                return task
        return None
