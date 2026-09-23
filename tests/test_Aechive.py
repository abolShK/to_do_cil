import unittest
from Archive import add_archive
class TEST(unittest.TestCase):
    def test_add_archive(self):
        archiveList = {
            
        }
        taskList={
            "ali": {"status": "true", "priority": "Low", "pin": "false", "date": "2026-09-23", "RecurringTask": "none"},
            "ts": {"status": "true", "priority": "Low", "pin": "false", "date": "2026-09-15" , "RecurringTask" : "none"}
        }
        def fake(data) :
            pass
        add_archive(taskList , archiveList , [] , fake , "ts")
        self.assertIn("ts", archiveList)
        self.assertNotIn("ts", taskList)
            
        