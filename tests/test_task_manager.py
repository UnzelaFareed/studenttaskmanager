
import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    # Test 1: Add Task
    def test_add_task(self):
        task = self.manager.add_task("Study Python")

        self.assertEqual(task["title"], "Study Python")
        self.assertFalse(task["completed"])

    # Test 2: Complete Task
    def test_complete_task(self):
        self.manager.add_task("Study Python")

        result = self.manager.complete_task(1)

        self.assertTrue(result)
        self.assertTrue(self.manager.display_tasks()[0]["completed"])

    # Test 3: Delete Task
    def test_delete_task(self):
        self.manager.add_task("Study Python")

        result = self.manager.delete_task(1)

        self.assertTrue(result)
        self.assertEqual(self.manager.display_tasks(), [])


if __name__ == "__main__":
    unittest.main()
