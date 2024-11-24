import unittest
from tasks.task_manager import TaskManager
from utils.enums import Priority, Status


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.manager.add_task(
            "Task 1", "Work", "2024-11-26", "High", "Pending"
        )
        self.manager.add_task(
            "Task 2", "Personal",
            "2024-11-20", "Medium", "Completed"
        )

    def test_add_task(self):
        task = self.manager.add_task(
            "Task 3", "Urgent", "2024-12-01", "High", "Pending"
        )
        self.assertEqual(len(self.manager.all_tasks()), 3)
        self.assertEqual(task.name, "Task 3")

    def test_update_task(self):
        id = self.manager.all_tasks()[0].task_id
        updated = self.manager.update_task(id, Status.COMPLETED)
        self.assertTrue(updated)
        self.assertEqual(
            self.manager.all_tasks()[0].status, "Completed"
        )

    def test_delete_task(self):
        id = self.manager.all_tasks()[1].task_id
        deleted = self.manager.delete_task(id)
        self.assertTrue(deleted)
        self.assertEqual(len(self.manager.all_tasks()), 4)

    def test_filter_tasks(self):
        filtered = self.manager.filter_tasks(status=Status.COMPLETED)
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0].name, "Task 2")

    def test_sort_tasks(self):
        sorted_tasks = self.manager.sort_tasks(key="priority")
        self.assertEqual(sorted_tasks[0].name, "Task 1")

    def test_update_tasks_concurrently(self):
        id1 = self.manager.all_tasks()[0].task_id
        id2 = self.manager.all_tasks()[1].task_id
        updates = [
            (id1, {"status": Status.IN_PROGRESS}),
            (id2, {"priority": Priority.LOW})
        ]
        results = self.manager.update_tasks_concurrently(updates)
        self.assertEqual(results, [True, True])
        self.assertEqual(
            self.manager.all_tasks()[0].status.value, 2
        )
        self.assertEqual(self.manager.all_tasks()[1].priority, Priority.LOW)


if __name__ == "__main__":
    unittest.main()
