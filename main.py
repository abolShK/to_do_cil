# lst's start new project 
import json
from datetime import datetime, timedelta , date
from dateutil.relativedelta import relativedelta
from sorting import SortKeyDisaen 
from filter import Fillter
from utils import vorody
from is_check_name_in_functins import is_check_name_in_function
from search import Search
from storage import saveArchive , LoadArchive , saveCommand , LoadCommand , saveHistory , Loadhistory , SaveTasks , LoadTasks ,SaveRedo,LoadRedo,SaveSummery,LoadSummery,SaveUndo,LoadUndo
from undo_redo import UndoOption , Redo
from Show_history import ShowedHistory
from Archive import add_archive
print("1 . add task")
print("2 . show task")
print("3 . Delet task")
print("4 . Exit task")
print("5 . Edit task")
print("6 . Search task")
print("7 . Fillter task")
print("8 . Sort task")
print("9 . undo task")
print("10 . Redo task")
print("11 . show summery task")
print("12 . delete A few task")
print("13 . Change A few task")
print("14 . ShowedHistory")
print("15 . add archive")
print("16 . show command")



checked = True
def add_task(task_List , undoList , summery , savaSumery , history , archiveList , commandList , saveCommand , name):
    if undoList:
        undoList.clear()  
    addNameTesk = is_check_name_in_function(name , "what is task name")
    if addNameTesk in (task_List and archiveList):
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
        
           
        
def showTesk(addTeskList , command , saveCommand):
    for k , v in addTeskList.items():
        if(v["pin"] == "true"):
            print(k)
    for k , v in addTeskList.items() :
        if v["pin"] == "false" : 
            print(k)
    command.append("showTask")
    saveCommand(command)            
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

def Summry (summry , command , saveCommand):
    summeruValue = vorody("do you wanna weich summery(High, Medium, Low)")
    if summeruValue not in ("High" , "Medium" , "Low"):
        print("you have to choose in (High, Medium, Low)")
        return
    value = summry.get(summeruValue)  
    print(f"summmery {summeruValue} = {value}")  
    command.append("showSummery")
    saveCommand(command)
    return summry   
def delwant(tasklist , savaTask , history, saveHistory , command , saveCommand , nameList):
    if not tasklist :
        print("task list  empyied")
        return
    if not nameList : 
        taskDelete = vorody("do you want delete task ?")
        if taskDelete in tasklist :
            tasklist.pop(taskDelete)
            history.append({"deleted" : taskDelete}) 
            saveHistory(history)
            print(f"this {taskDelete} deleted")
            savaTask(tasklist)
            command.append("dlewant")
            saveCommand(command)
            is_couinti = vorody("do you want continue : (yes,no)")
            if is_couinti not in ("yes" , "no"):
                print("vorody is  incorrect")
                return
            else:
                if is_couinti == "yes" : 
                    delwant(tasklist , savaTask ,history , saveHistory)
                else : 
                    return   
        else : 
            print("it is not find")
    else :  
        for nameDel in nameList: 
            if nameDel in tasklist :
                history.append({"deleted" : nameDel}) 
                saveHistory(history)
                print(f"this {nameDel} deleted")
                tasklist.pop(nameDel)
                savaTask(tasklist)
                command.append("dlewant")
                saveCommand(command)
            else : 
                print(f"not found {nameDel} task")
                continue                 
                            
def upatedStateAfew(listTask , saveTask , command , saveCommand , name): 
    if not name :  
        isTrue = True
        while isTrue : 
            targetTaskChange = vorody("do you want to change state's task :")
            if targetTaskChange in listTask : 
                newStateTask = vorody("what do you new state task :(true or false)")
                if newStateTask not in ("true" , "false"):
                    print("state has to true or false")
                    return
                listTask[targetTaskChange]["status"]=newStateTask
                saveTask(listTask)
                command.append("UpdateWant")
                saveCommand(command)
                is_couinti = vorody("do you want continue : (yes,no)")
                if is_couinti not in ("yes" , "no"):
                    print("we don't have this vorody")
                else : 
                    if is_couinti == "yes" :
                        continue
                    else :
                        return 
            else: 
                print("it is not find")
                return 
    else : 
        for nameUpdateStatus in name : 
            if nameUpdateStatus in listTask :
                newStateTask = vorody(f"what do you new state task {nameUpdateStatus}:(true or false)")
                if newStateTask not in ("yes" , "true") : 
                    print("new status have to true or false")
                    return
                listTask[nameUpdateStatus]["status"]=newStateTask
                saveTask(listTask)
                command.append("UpdateWant")
                saveCommand(command)
            else :
                print("it is not find")
                continue 
                                              
HistoryTask = Loadhistory()

def showCommnd(commandList): 
    for command in commandList[-10:]:
        print(command)
         
            

command_History = LoadCommand()
    
                   
task_List = LoadTasks()
UndoList =LoadUndo()
RedoList = LoadRedo()  
arhciveList = LoadArchive()
Summrys = LoadSummery() if LoadSummery() else {
    "High": 0,
    "Medium": 0,
    "Low": 0
}

def appointedDay(day , task):
    if day == "none":
        print(task)
    




                
            
        
            
        
                
    
            
def is_name(name):
    if len(name) > 1 :
        return name[1]
    else :  return ""

while checked : 
    choose_task_option = input("you choose your option :")
    name  =choose_task_option.split()
    if(choose_task_option == "1" or name[0] == "add"):
      add_task(task_List , UndoList , Summrys , SaveSummery , HistoryTask , arhciveList ,command_History , saveCommand , is_name(name))
    elif(choose_task_option == "2" or choose_task_option == "show"):
        showTesk(task_List , command_History ,saveCommand)
    elif(choose_task_option == "3" or name[0] == "delete"):
        deleting(task_List , UndoList , HistoryTask, command_History ,saveCommand , is_name(name))
    elif(choose_task_option == "4" or choose_task_option == "Exit"):
        checked = False
        command_History.append("Exit")
        saveCommand(command_History)
    elif(choose_task_option == "5" or name[0] == "Edit"):
        EditTesk(task_List , UndoList , HistoryTask ,command_History ,saveCommand , is_name(name)) 
    elif(choose_task_option == "6" or name[0] == "search"):
        Search(task_List , command_History ,saveCommand , is_name(name)) 
    elif(choose_task_option == "7" or name[0] == "fillter"):
         Fillter(task_List , command_History ,saveCommand) 
    elif(choose_task_option == "8" or name[0] == "sort"):
        SortKeyDisaen(task_List , command_History ,saveCommand) 
    elif (choose_task_option == "9" or name[0] == "undo"):
        RedoList = UndoOption(task_List , UndoList , RedoList , command_History ,saveCommand)
    elif (choose_task_option == "10" or name[0] == "Redo"):
        Redo(task_List , RedoList , command_History ,saveCommand)
    elif (choose_task_option == "11" or name[0] == "summery"):
        Summrys = Summry(Summrys , command_History ,saveCommand)  
    elif (choose_task_option == "12" or name[0] == "delwant"):
        delwant(task_List , SaveTasks ,  HistoryTask , saveHistory , command_History ,saveCommand , name[1:]) 
    elif (choose_task_option == "13" or name[0] == "updateWant"):
        upatedStateAfew(task_List , SaveTasks , command_History ,saveCommand , name[1:])   
    elif(choose_task_option == "14" or name[0] == "showHistory"):
        ShowedHistory(HistoryTask , command_History ,saveCommand)
    elif(choose_task_option == "15" or name[0] == "addArchive"):
        add_archive(task_List , arhciveList , command_History ,saveCommand , is_name(name))
    elif(choose_task_option == "16" or name[0] == "showCommend"):
        showCommnd(command_History)                      
                 
                     
                                           
        
        
 
