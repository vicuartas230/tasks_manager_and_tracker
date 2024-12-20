import unittest
from tasks.task import Task
from utils.enums import Priority


class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task(
            "Learn Vue", "Personal", "2024-12-31",
            "Medium", "Pending"
        )
        self.assertEqual(task.name, "Learn Vue")
        self.assertEqual(task.category, "Personal")
        self.assertEqual(task.priority, Priority.MEDIUM)
        self.assertFalse(task.is_overdue())

    def test_task_overdue(self):
        task = Task(
            "Finish Java Course", "Personal", "2024-11-01",
            "High", "Pending"
        )
        self.assertTrue(task.is_overdue())


if __name__ == "__main__":
    unittest.main()
