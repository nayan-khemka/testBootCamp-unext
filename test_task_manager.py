# test_task_manager.py
import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Test task")
        self.assertIn("Test task", self.manager.view_tasks())

    def test_add_empty_task_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")

    def test_add_non_string_task_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_task(123)

    def test_view_tasks(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.assertEqual(self.manager.view_tasks(), ["Task 1", "Task 2"])

    def test_delete_task(self):
        self.manager.add_task("Task to delete")
        self.manager.delete_task("Task to delete")
        self.assertNotIn("Task to delete", self.manager.view_tasks())

    def test_delete_non_existent_task_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task("Non-existent task")

    def test_add_multiple_tasks(self):
        tasks = ["Task 1", "Task 2", "Task 3"]
        for task in tasks:
            self.manager.add_task(task)
        self.assertEqual(self.manager.view_tasks(), tasks)

    def test_delete_multiple_tasks(self):
        tasks = ["Task 1", "Task 2", "Task 3"]
        for task in tasks:
            self.manager.add_task(task)
        self.manager.delete_task("Task 1")
        self.manager.delete_task("Task 2")
        self.assertEqual(self.manager.view_tasks(), ["Task 3"])

    def test_view_empty_tasks(self):
        self.assertEqual(self.manager.view_tasks(), [])

    def test_delete_task_from_empty_list_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task("Non-existent task")

if __name__ == "__main__":
    unittest.main()
