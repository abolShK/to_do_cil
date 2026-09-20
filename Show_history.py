def ShowedHistory(history , command , saveCommand):
    for task in history:
        if "added" in task:
            print(f"this {task["added"]} task is added on the task list")
        elif "beforeEdited" and "afterEdited" in task :
            print(f"before Edited :{task["beforeEdited"]} and after :{task["afterEdited"]}")  
        else : 
            print(f"this {task["deleted"]} is deleted on the task List")  
    command.append("showHistory")
    saveCommand(command)                