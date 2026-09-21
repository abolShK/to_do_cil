from utils import vorody
from is_check_name_in_functins import is_check_name_in_function
from storage import (
    SaveTasks,
    SaveUndo,
    saveHistory
)
def deleting(items , undoList , history, command , saveCommand , name):
    if undoList:
        undoList.clear()
    deleted = is_check_name_in_function(name , "which task do you want delet :")            

    if(len(deleted) <= 0 ):
        print("you have to writing 1 word") 
        return 
    else : 
        if items.get(deleted) : 
            value = items[deleted]
            undoList["del"] = {deleted : value}
            # add deleted history 
            history.append({"deleted" : deleted})
            saveHistory(history)
            SaveUndo(undoList)
            items.pop(deleted)
            SaveTasks(items)        
            print(f"item {deleted} deleted")  
            command.append("delete") 
            saveCommand(command)       
        else : print("not find") 