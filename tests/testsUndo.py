import unittest
from filter import _FillterStatus
from sorting import SortKeyDisaen
from storage import saveCommand


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


if __name__ == "__main__":
    unittest.main()
    