# lst's start new project 
import json
import datetime
print("1 . add task")
print("2 . show task")
print("3 . Delet task")
print("4 . Exit task")
print("5 . Edit task")
print("6 . Search task")
print("7 . Edit vazeat's task")
print("8 . Fillter task")
print("9 . Sort task")
print("10 . undo task")
print("11 . Redo task")
print("12 . show summery task")
print("13 . delete A few task")
print("14 . Change A few task")






checked = True
def vorody(testVoridy):
   return input(testVoridy)
def add_task(task_List , undoList , summery , savaSumery , history):
    if undoList:
        undoList.clear()     
    addNameTesk = vorody("what is name task :")
    if task_List.get(addNameTesk):
        print("not key rpate")
        return
    if(len(addNameTesk) <= 0 and len(addStatus) <= 0 and len(addPriority) <= 0):
        print("you have to writing 1 word")
        return
    addStatus = vorody("what is status task (true or false):")
    if addStatus not in ("true" ,  "false") :
        print("Erorr : you have to write in the Statue (true or false)") 
        return
    addPriority = vorody("what is priority task (High , Medium , Low):") 
    if addPriority not in ("High" , "Medium" , "Low"):
        print("Erorr : you have to write in the Statue (High or Medium or Low)")
        return
    addPinned = vorody("this task pin ? : (true or false):") 
    if addPinned not in ("true" , "false"):
        print("Erorr : you have to write pin (true or false)")
        return    
    # DATA INPUT    
    dateInput = vorody("what date : (2020-10-20):") 
    try:
        datetime.datetime.strptime(dateInput, "%Y-%m-%d")
    except ValueError:
        print("Invalid date") 
        return       
    if addPriority in summery:
        summery[addPriority] = summery.get(addPriority) + 1
    savaSumery(summery)        
    task_List[addNameTesk] = {"status" : addStatus , "priority" : addPriority , "pin" : addPinned , "date" : dateInput}
    value = task_List[addNameTesk]
    # add history 
    history.append({"added" : addNameTesk})
    saveHistory(history)
    print(history)
    undoList["add"] = {addNameTesk : value}
    SaveUndo(undoList)
    print("task added") 
    SaveTasks(task_List)   
    
        
def showTesk(addTeskList):
    for k , v in addTeskList.items():
        if(v["pin"] == "true"):
            print(k)
    for k , v in addTeskList.items() :
        if v["pin"] == "false" : 
            print(k)        
def deleting(items , undoList , history):
    if len(undoList) is not 0 :
        undoList.clear()     
    deleted = vorody("which delete you tesk : ")
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
        else : print("not find")        
def EditTesk(TeskList ,undoList , history):
    if len(undoList) is not 0 :
        undoList.clear()  
    itemEdit = vorody("which do yot tesk Edit :")
    if(len(itemEdit) <= 0 ):
        print("you have to writing 1 word") 
        return
    else:             
        if(not(TeskList.get(itemEdit))):
            print("this tesk is'nt in the tesk list")
            return
        else:
            newName  = vorody("what is new name's tesk :")
            if(len(newName) is 0 and newName in TeskList) :
                print("vorody dont have to empty or your newName are in the taskList")
                return
            status  = vorody("what is new status's tesk (true or false):")
            if(len(newName) is 0 and status not in ("treu" , "false")) :
                print("vorody dont have to empty or your vorody arent ture or false") 
                return           
            priority  = vorody("what is new status's tesk (High , Medium , Low):")
            if(len(newName) is 0 and status not in("High","Medium","Low")) :
                print("vorody dont have to empty or your vorody are not High or Medium or Low ") 
                return
            pined  = vorody("what is new pin's tesk (true or false):")
            if(len(newName) is 0 and pined not in("true","false")) :
                print("vorody dont have to empty or your vorody are not High or Medium or Low ") 
                return 
                # DATA INPUT    
            newdate = vorody("what date : (2020-10-20):") 
            try:
                datetime.datetime.strptime(newdate, "%Y-%m-%d")
            except ValueError:
                print("Invalid date") 
                return                          
            value = TeskList.pop(itemEdit)
            key = itemEdit
            undoList["Edit"] ={key : value}
            # add edited history 
            history.append({"beforeEdited" : itemEdit , "afterEdited" : newName})
            saveHistory(history)
            print(history)
            TeskList[newName] = {"status" : status , "priority" : priority ,"pin" : pined , "date" :newdate }
            SaveTasks(TeskList)
            SaveUndo(undoList)              
            print("Edit did")
def Search(teskList):
    itmeSearch = vorody("Are you looking for :")
    isCheckSeaech = False
    for k , v in teskList.items():
        if k[:len(itmeSearch)] == itmeSearch: 
            isCheckSeaech=True
            print(k)
            input_date = datetime.datetime.strptime(v["date"], "%Y-%m-%d").date()
            if datetime.date.today() > input_date:
                print("date is in the past")
            elif datetime.date.today() < input_date : 
                print("date is not the past")
            else : "today is last day to do it"        
            
    if isCheckSeaech == False:         
        print("anyting is'ent name")  
def EditVazeat(targetItem): 
    nameEditVazeat = vorody("wiche item do you wanna change vazeat :")
    if targetItem.get(nameEditVazeat):
        newVazeat = vorody("your new veazt writer :")
        targetItem[nameEditVazeat] = newVazeat
        print(targetItem)
    else : 
        print("tere is'ent this vazeat")
def FillterStatus(listFillter):
    print("1 . all show")
    print("2 . done show")
    print("3 . not done show")
    chooseShowTeskFillter = vorody("do you choose :")
    if chooseShowTeskFillter not in ("1","2","3"): 
        print("this number is incorract")
    else :     
        for key , value in listFillter.items() : 
            if chooseShowTeskFillter == "1":
                print(key)
            elif chooseShowTeskFillter == "2" and value["status"] == "true":
                    print(key)
            elif chooseShowTeskFillter == "3" and value["status"] == "false":
                    print(key)  
def FiltterPriority(listFillter):
    print("1 . High")
    print("2 . Medium")
    print("3 . Low")
    chooseShowTeskFillter = vorody("do you choose :")
    if chooseShowTeskFillter not in ("1","2","3"): 
        print("this number is incorract")
    else :    
        for key , value in listFillter.items() : 
            if chooseShowTeskFillter == "1" and value["priority"] == "High":
                print(key)
            elif chooseShowTeskFillter == "2" and value["priority"] == "Medium":
                print(key)
            elif chooseShowTeskFillter == "3" and value["priority"] == "Low":
                print(key)  
        if chooseShowTeskFillter not in ("1","2","3"): 
            print("this number is incorract")
def Fillter(listFilter):
    print("1 . Fitter priority")
    print("2 . Fillter status")    
    chooseMethodFilltering = vorody("you choose wiche method fillters :")
    if chooseMethodFilltering == "1" :FiltterPriority(listFilter)
    elif chooseMethodFilltering == "2" : FillterStatus(listFilter)
    else : print("this number is'en in the Selection list")     
             
    

def SortKeyDisaen(listSort):
     items = list(listSort.items())
     SortKey(items , 0  , len(listSort) - 1)  
     listSort.clear()
     listSort.update(items)  
def SortKey(List_sort , start , end):
    if start >= end  :  return
    boundery = partition(List_sort , start , end )
    SortKey(List_sort , start , boundery -1)
    SortKey(List_sort , boundery + 1 , end)
       
def partition(items , start , end):
    piovt = items[end][0]
    boundary = start 
    for itemsSort in range(start ,end):
        if items[itemsSort][0] <= piovt :
            boundary+=1
            swap(items , itemsSort , boundary) ##ببین تو این خط میخوام عمیلات صورت رو روی تاپل انجام بده برای همین مشخص نکردم key باش یا value     
    swap(items , boundary , end)
    return boundary 
            
            
def swap(array , index1 , index2):
    teamp = array[index1]
    array[index1] = array[index2]
    array[index2] = teamp             


def UndoOption(listTask , undoList  , redoList):
    if(len(undoList) <= 0 ) :
        print("this list is empy")
        return redoList  
    if redoList : 
        redoList.clear()  
    k , v =undoList.popitem() 
    if k == "add":
        keyadd , valueadd = listTask.popitem()
        redoList["add"] = {keyadd:valueadd}
        SaveRedo(redoList)
        SaveTasks(listTask)         
    elif k == "del":
        key, value = v.popitem()
        listTask[key] = value
        redoList["del"] = {key : value}
        SaveRedo(redoList)
        SaveTasks(listTask)       
    else : 
        key , value = v.popitem()
        redokey , redovalue = listTask.popitem()
        listTask[key] = value
        redoList["Edit"] = {redokey : redovalue}
        SaveRedo(redoList)
        SaveTasks(listTask)       
    return redoList 
def SaveUndo(task_List):
    file = open("undoListing.json" ,"w")
    json.dump(task_List , file)
    file.close() 
def LoadUndo():
    file = open("undoListing.json" , "r")
    data = json.load(file) 
    file.close()  
    return data   
def Redo(tasklist , redo):
    if(len(redo) <= 0 ) :
        print("this list is empy")
        return
    k , v =redo.popitem() 
    if(k == "add") : 
        k2 , v2 = v.popitem() 
        tasklist[k2] = v2
        SaveTasks(tasklist)
    elif k== "del" :
        keyDel ,valueDel = v.popitem()
        if tasklist.get(keyDel):
            tasklist.popitem()
            SaveTasks(tasklist)
    else:
        keyEdit ,valueEdit = v.popitem()
        tasklist.popitem()
        tasklist[keyEdit] = valueEdit
        SaveTasks(tasklist) 
def SaveRedo(task_List):
    file = open("RedoList.json" ,"w")
    json.dump(task_List , file)
    file.close() 
def LoadRedo():
    file = open("RedoList.json" , "r")
    data = json.load(file) 
    file.close()  
    return data                        
def SaveTasks(task_List):
    file = open("tasks.json" ,"w")
    json.dump(task_List , file)
    file.close() 
def LoadTasks():
    file = open("tasks.json" , "r")
    data = json.load(file) 
    file.close()  
    return data 

def Summry (summry):
    summeruValue = vorody("do you wanna weich summery(High, Medium, Low)")
    if summeruValue not in ("High" , "Medium" , "Low"):
        print("you have to choose in (High, Medium, Low)")
        return
    value = summry.get(summeruValue)  
    print(f"summmery {summeruValue} = {value}")  
    return summry   
def SaveSummery(summery):
    file = open("undoList.json", "w")
    json.dump(summery, file)
    file.close()
def LoadSummery():
    file = open("undoList.json" , "r")
    data = json.load(file)
    file.close()
    return data 
def delwant(tasklist , savaTask , history, saveHistory):
    if not tasklist :
        print("task list  empyied")
        return
    taskDelete = vorody("do you want delete task ?")
    if taskDelete in tasklist :
        tasklist.pop(taskDelete)
        history.append({"deleted" : taskDelete}) 
        saveHistory(history)
        print(f"this {taskDelete} deleted")
        savaTask(tasklist)
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
def upatedStateAfew(listTask , saveTask):  
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
def ShowedHistory(history):
    for task in history:
        if "added" in task:
            print(f"this {task["added"]} task is added on the task list")
        elif "beforeEdited" and "afterEdited" in task :
            print(f"before Edited :{task["beforeEdited"]} and after :{task["afterEdited"]}")  
        else : 
            print(f"this {task["deleted"]} is deleted on the task List")      
def saveHistory(history):
    file = open("historyTask.json" , "w")
    json.dump(history , file)
    file.close()
def Loadhistory():
    file = open("historyTask.json" , "r")
    data = json.load(file)
    file.close() 
    return data   
HistoryTask = Loadhistory()


                  
         
                                 
        


        

                   
task_List = LoadTasks()
UndoList =LoadUndo()
RedoList = LoadRedo()  
Summrys = LoadSummery() if LoadSummery() else {
    "High": 0,
    "Medium": 0,
    "Low": 0
}




                
            
        
            
        
                
    
            


while checked : 
    choose_task_option = input("you choose your option :")
    if(choose_task_option == "1"):
      add_task(task_List , UndoList , Summrys , SaveSummery , HistoryTask)
    elif(choose_task_option == "2"):
        showTesk(task_List)
    elif(choose_task_option == "3"):
        deleting(task_List , UndoList , HistoryTask)
    elif(choose_task_option == "4"):
        checked = False
    elif(choose_task_option == "5"):
        EditTesk(task_List , UndoList , HistoryTask) 
    elif(choose_task_option == "6"):
        Search(task_List) 
    elif(choose_task_option == "7"):
         EditVazeat(task_List)
    elif(choose_task_option == "8"):
         Fillter(task_List) 
    elif(choose_task_option == "9"):
        SortKeyDisaen(task_List) 
    elif (choose_task_option == "10"):
        RedoList = UndoOption(task_List , UndoList , RedoList)
    elif (choose_task_option == "11"):
        Redo(task_List , RedoList)
    elif (choose_task_option == "12"):
        Summrys = Summry(Summrys)  
    elif (choose_task_option == "13"):
        delwant(task_List , SaveTasks ,  HistoryTask , saveHistory) 
    elif (choose_task_option == "14"):
        upatedStateAfew(task_List , SaveTasks)   
    elif(choose_task_option == "15"):
        ShowedHistory(HistoryTask)   
                 
                     
                                           
        
        
 
