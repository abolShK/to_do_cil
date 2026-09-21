import json


def SaveTasks(task_List):
    with open("tasks.json", "w") as file:
        json.dump(task_List, file)


def LoadTasks():
    with open("tasks.json", "r") as file:
        return json.load(file)


def SaveUndo(undoList):
    with open("undoListing.json", "w") as file:
        json.dump(undoList, file)


def LoadUndo():
    try:
        with open("undoListing.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def SaveRedo(redoList):
    with open("RedoList.json", "w") as file:
        json.dump(redoList, file)


def LoadRedo():
    try:
        with open("RedoList.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def saveHistory(history):
    with open("historyTask.json", "w") as file:
        json.dump(history, file)


def Loadhistory():
    try:
        with open("historyTask.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def saveArchive(archiveList):
    with open("acchiveList.json", "w") as file:
        json.dump(archiveList, file)


def LoadArchive():
    try:
        with open("acchiveList.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def saveCommand(command):
    with open("CommandHistory.json", "w") as file:
        json.dump(command, file)


def LoadCommand():
    try:
        with open("CommandHistory.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def SaveSummery(summery):
    with open("summery.json", "w") as file:
        json.dump(summery, file)


def LoadSummery():
    try:
        with open("summery.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}