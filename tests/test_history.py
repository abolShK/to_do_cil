from Show_history import ShowedHistory
import unittest
from unittest.mock import patch
import io

class TEST(unittest.TestCase):

    def test_history(self):
        historyList = [{"beforeEdited": "ali", "afterEdited": "alii"}]

        def fake(data):
            pass

        with patch("sys.stdout", new=io.StringIO()) as output:
            ShowedHistory(historyList, [], fake)

        print(output.getvalue())