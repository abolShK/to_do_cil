# lst's start new project 
import json
from datetime import datetime, timedelta , date
from dateutil.relativedelta import relativedelta
from sorting import SortKeyDisaen 
from filter import Fillter
from search import Search
from storage import LoadArchive , saveCommand , LoadCommand , saveHistory , Loadhistory , SaveTasks , LoadTasks ,SaveRedo,LoadRedo,SaveSummery,LoadSummery,SaveUndo,LoadUndo
from undo_redo import UndoOption , Redo
from Show_history import ShowedHistory
from Archive import add_archive
from summery import Summry
from add_task import add_task
from showTask import showTesk
from deleteTask import deleting
from Editing import EditTesk 
from UpdateWant import upatedStateAfew 
from deleteWant import delwant
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

def showCommnd(commandList): 
    for command in commandList[-10:]:
        print(command)
         
            
HistoryTask = Loadhistory()
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
        Summrys = Summry(Summrys , command_History ,saveCommand , is_name(name))  
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
                 
                     
                                           
        
        
 
