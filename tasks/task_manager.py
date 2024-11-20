from tasks.task import Task
from datetime import datetime


class TaskManager:
    def __init__(self):
        """Initializes an empty list to store tasks."""
        self.tasks = []
        
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
        task = Task(name, category, due_date, priority, status)
        self.tasks.append(task)
        return task
    
    def update_task(self, task_id, **kwargs):
        """
        Updates an existing task.
        
        Args:
            task_id (UUID): ID of the task to update.
            **kwargs: Key-value pairs of attributes to update.
            
        Returns:
            bool: True if the task was updated, False otherwise.
        """
        task = self._find_task_by_id(task_id)
        if not task:
            return False
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        return True
    
    def delete_task(self, task_id):
        """
        Deletes a task by ID.
        
        Args:
            task_id (UUID): ID of the task to delete.
            
        Returns:
            bool: True if the task was deleted, False otherwise.
        """
        task = self._find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
    
    def view_tasks(self):
        """
        Returns a list of all tasks.
        
        Returns:
            list: list of tasks.
        """
        return self.tasks
    
    def filter_tasks(self, **criteria):
        """
        Filters tasks based on given criteria.
        
        Args:
            **criteria: Key-value pairs to filter tasks (e.g., status="Pending").
            
        Returns:
            list: List of tasks matching the criteria.
        """
        filtered_tasks = self.tasks
        for key, value in criteria.items():
            filtered_tasks = [task for task in filtered_tasks if getattr(task, key) == value]
        return filtered_tasks
    
    def _find_task_by_id(self, task_id):
        """Finds a task by its ID"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
