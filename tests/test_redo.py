import unittest
from undo_redo import Redo
class TEST(unittest.TestCase) :
    def test_Redo(self):
        taskList = {"ali": {"status": "true", "priority": "Low", "pin": "false", "date": "2026-09-23", "RecurringTask": "none"}}
        RedoList={"add": {"alii": {"status": "true", "priority": "Low", "pin": "true", "date": "2026-09-20", "RecurringTask": "none"}}}
        def fake(data) : 
            pass
        Redo(taskList , RedoList,[],fake)
        self.assertIn( "alii" , taskList)
        self.assertNotIn("alii",RedoList)
        
        
            
        