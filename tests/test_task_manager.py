import unittest
from tasks.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.manager.add_task("Task 1", "Work", "2024-11-26", "High")
        self.manager.add_task("Task 2", "Personal", "2024-11-20", "Medium", "Completed")
        
    def test_add_task(self):
        task = self.manager.add_task("Task 3", "Urgent", "2024-12-01", "High")
        self.assertEqual(len(self.manager.view_tasks()), 3)
        self.assertEqual(task.name, "Task 3")
        
    def test_update_task(self):
        id = self.manager.tasks[0].task_id
        updated = self.manager.update_task(id, status="Completed")
        self.assertTrue(updated)
        self.assertEqual(self.manager.view_tasks()[0].status, "Completed")
        
    def test_delete_task(self):
        id = self.manager.tasks[1].task_id
        deleted = self.manager.delete_task(id)
        self.assertTrue(deleted)
        self.assertEqual(len(self.manager.view_tasks()), 1)
        
    def test_filter_tasks(self):
        filtered = self.manager.filter_tasks(status="Completed")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].name, "Task 2")
        
if __name__ == "__main__":
    unittest.main()
