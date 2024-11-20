import unittest
from tasks.task import Task


class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task("Learn Vue", "Personal", "2024-12-31", "Medium")
        self.assertEqual(task.name, "Learn Vue")
        self.assertEqual(task.category, "Personal")
        self.assertEqual(task.priority, "Medium")
        self.assertFalse(task.is_overdue())
        
    def test_task_overdue(self):
        task = Task("Finish Java Course", "Personal", "2024-11-01", "High")
        self.assertTrue(task.is_overdue())
        
if __name__ == "__main__":
    unittest.main()
