import unittest
from filter import _FillterStatus
from sorting import SortKeyDisaen
from storage import saveCommand
from search import Search
from unittest.mock import patch
from io import StringIO
from undo_redo import UndoOption


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
        
                        
                           


if __name__ == "__main__":
    unittest.main()
    