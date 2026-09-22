import unittest
from filter import _FillterStatus
from sorting import SortKeyDisaen
from storage import saveCommand
from search import Search
from unittest.mock import patch
from io import StringIO
from undo_redo import UndoOption
from add_task import add_task


class Test(unittest.TestCase):
    def test_filter_status(self):
        tasks = {
            "ali": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "hos": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "li": {
                "status": "false",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            }        
        }

        result = _FillterStatus(tasks)

        self.assertEqual(result, tasks)
    def test_sort(self):
        tasks = {
            "ali": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "hos": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "li": {
                "status": "false",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            }
        }

        SortKeyDisaen(tasks, [], saveCommand)

        self.assertEqual(tasks, {
            "ali": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "hos": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "li": {
                "status": "false",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
                }
            }) 
    def test_search(self):
        tasks = {
            "lii": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "hos": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "li": {
                "status": "false",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            }
        }
        name = "l"
        with patch("sys.stdout", new=StringIO()) as output:
            Search(tasks, [], saveCommand, name)

        result = output.getvalue()
        self.assertIn("lii", result)
        self.assertIn("li", result)
    def test_undo_add(self):
        tasks = {
            "hos": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "li": {
                "status": "false",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "ali": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-20",
                "RecurringTask": "none"
            }
        }

        undo_list = {
            "add": {
                "ali": {
                    "status": "true",
                    "priority": "Low",
                    "pin": "true",
                    "date": "2026-09-20",
                    "RecurringTask": "none"
                }
            }
        }

        redo_list = {}
        command = []

        UndoOption(tasks, undo_list, redo_list, command, saveCommand)

        self.assertEqual(tasks, {
            "hos": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "li": {
                "status": "false",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            }
        }) 
    def test_addTask(self):
        taskList = {
            "hos": {
                "status": "true",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            },
            "li": {
                "status": "false",
                "priority": "Low",
                "pin": "true",
                "date": "2026-09-14"
            }
        }

        def fake_save(data):
            pass

        add_task(
            taskList,
            {},
            {},
            fake_save,
            [],
            {},
            [],
            fake_save,
            ""
        )
        self.assertIn("ali", taskList)
    def test_addTask_duplicate(self):
        taskList = {
            "ali": {
                "status": "true",
                "priority": "Low",
                "pin": "false",
                "date": "2026-09-22",
                "RecurringTask": "none"
            }
        }

        def fake_save(data):
            pass

        add_task(
            taskList,
            {},
            {},
            fake_save,
            [],
            {},
            [],
            fake_save,
            ""
        )

        self.assertEqual(len(taskList), 1)
    def test_Addtask_in_Archive(self):     
        archiveList ={"ali": {"status": "true", "priority": "Low", "pin": "false", "date": "2026-09-22", "RecurringTask": "none"}}

        taskList = {}

        def fake_save(data):
            pass

        add_task(
            taskList,
            {},
            {},
            fake_save,
            [],
            archiveList,
            [],
            fake_save,
            ""
        )

        self.assertEqual(len(taskList), 0)          
              
        
        
        
                        
                           


if __name__ == "__main__":
    unittest.main()
    