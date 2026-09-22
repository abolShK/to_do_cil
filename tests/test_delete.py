import unittest
from deleteTask import deleting
class Test(unittest.TestCase):
    def test_delete(self):
        taskList = {
            "ali": {"status": "true", "priority": "Low", "pin": "false", "date": "2026-09-22", "RecurringTask": "none"}
        }
        def fake(date):
            pass
        deleting(taskList ,{} ,[],[],fake,"")
        self.assertEqual(taskList,{})
        
        
        