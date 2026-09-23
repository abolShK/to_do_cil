import unittest
from Editing import EditTesk
class TEST(unittest.TestCase):
    def test_Edit(self):
        taskList = {
            "ali": {"status": "true", "priority": "Low", "pin": "false", "date": "2026-09-23", "RecurringTask": "none"}
        }
        def fake(date):
            pass
        EditTesk(taskList , {},[],[],fake,"ali")
        self.assertEqual(taskList , {"alii": {"status": "true", "priority": "Low", "pin": "false", "date": "2026-09-23", "RecurringTask": "none"}})