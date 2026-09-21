from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from utils import vorody
from is_check_name_in_functins import is_check_name_in_function
from storage import (
    SaveTasks,
    SaveUndo,
    saveHistory
)

def add_task(task_List , undoList , summery , savaSumery , history , archiveList , commandList , saveCommand , name):
    if undoList:
        undoList.clear()  
    addNameTesk = is_check_name_in_function(name , "what is task name :")
    if addNameTesk in task_List or addNameTesk in archiveList:
        print(f"you check archiveList or taskList , Because there is {addNameTesk} in the taskList or aarchiveList ")
        return
    if(len(addNameTesk) <= 0 and len(addStatus) <= 0 and len(addPriority) <= 0):
        print("you have to writing 1 word")
        return
    # Recurring Task
    addRecurringTask = vorody("do you wanna do this task (none or daily or weekly or monthly):")
    if addRecurringTask not in ("none" , "daily" ,"weekly" ,"monthly"):
        print("Erorr : you have to write Recurring (none or daily or weekly or monthly)")
        return 
    # DATA INPUT    
    dateInput = ""
    dateInput = timeValueDate(dateInput , addRecurringTask)                        
    addStatus = ""
    addStatus = statueValue(dateInput , addStatus)
    if addRecurringTask =="none":
        addStatus = "true"
    else : addStatus = "false"
    addPriority = vorody("what is priority task (High , Medium , Low):") 
    if addPriority not in ("High" , "Medium" , "Low"):
        print("Erorr : you have to write in the Statue (High or Medium or Low)")
        return
    addPinned = vorody("this task pin ? : (true or false):") 
    if addPinned not in ("true" , "false"):
        print("Erorr : you have to write pin (true or false)")
        return         
    if addPriority in summery:
        summery[addPriority] = summery.get(addPriority) + 1
    savaSumery(summery)        
    task_List[addNameTesk] = {"status" : addStatus , "priority" : addPriority , "pin" : addPinned , "date" : dateInput , "RecurringTask" : addRecurringTask }
    value = task_List[addNameTesk]
    # add history 
    history.append({"added" : addNameTesk})
    commandList.append("addTask")
    saveCommand(commandList)
    saveHistory(history)
    print(history)
    undoList["add"] = {addNameTesk : value}
    SaveUndo(undoList)
    print("task added") 
    SaveTasks(task_List)   
 
def timeValueDate (dateValue , RecurringTaskValue):
    today = datetime.now().date()
    if RecurringTaskValue == "none" :
        dateValue = today.strftime("%Y-%m-%d")
    elif RecurringTaskValue == "daily":
        dateValue = (today + timedelta(days=1)).strftime("%Y-%m-%d")
    elif RecurringTaskValue == "weekly":
        dateValue = (today + timedelta(weeks=1)).strftime("%Y-%m-%d")  
    elif RecurringTaskValue == "monthly":
        dateValue = (today + relativedelta(months=1)).strftime("%Y-%m-%d")
    return dateValue        

def statueValue (dateValue ,  statueValue):
    today = datetime.now().date().strftime("%Y-%m-%d")
    print(today)
    if not (dateValue == today):
        statueValue = "false"
    else : statueValue="true"
    
    return statueValue  
