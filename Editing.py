from utils import vorody
from is_check_name_in_functins import is_check_name_in_function
from storage import (
    SaveTasks,
    SaveUndo,
    saveHistory
)
from add_task import (
    timeValueDate,
    statueValue,
)
def EditTesk(TeskList ,undoList , history, command , saveCommand , name):
    if undoList:
        undoList.clear()  
    itemEdit = is_check_name_in_function(name , "which task do you want Edit:")
    if(len(itemEdit) <= 0 ):
        print("you have to writing 1 word") 
        return
    else:             
        if(not(TeskList.get(itemEdit))):
            print("this tesk is'nt in the tesk list")
            return
        else:
            newName  = vorody("what is new name's tesk :")
            if len(newName) == 0 and newName in TeskList:
                print("vorody dont have to empty or your newName are in the taskList")
                return
            addRecurringTask = vorody("do you want Edit this task (none or daily or weekly or monthly):")
            if len(addRecurringTask) == 0 and  addRecurringTask not in ("none" , "daily" ,"weekly" ,"monthly"):
                print("Erorr : you have to write Recurring (none or daily or weekly or monthly)")
                return             
            dateInput = ""
            dateInput = timeValueDate(dateInput , addRecurringTask)
            status  = ""  
            status = statueValue(dateInput , status)        
            priority  = vorody("what is new status's tesk (High , Medium , Low):")
            if len(priority) == 0 and status not in ("High", "Medium", "Low"):
                print("vorody dont have to empty or your vorody are not High or Medium or Low ") 
                return
            pined  = vorody("what is new pin's tesk (true or false):")
            if len(pined) == 0 and pined not in ("true", "false"):
                print("vorody dont have to empty or your vorody are not High or Medium or Low ") 
                return                         
            value = TeskList.pop(itemEdit)
            key = itemEdit
            undoList["Edit"] ={key : value}
            # add edited history 
            history.append({"beforeEdited" : itemEdit , "afterEdited" : newName})
            saveHistory(history)
            print(history)
            TeskList[newName] = {"status" : status , "priority" : priority ,"pin" : pined , "date" :dateInput ,"RecurringTask" : addRecurringTask }
            SaveTasks(TeskList)
            SaveUndo(undoList)    
            command.append("Edit")
            saveCommand(command)          
            print("Edit did") 