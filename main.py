# lst's start new project 
import json
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



checked = True
def vorody(testVoridy):
   return input(testVoridy)
def add_task(task_List , undoList , counts):
    if undoList:
        undoList.clear()     
    addNameTesk = vorody("what is name task :")
    if task_List.get(addNameTesk):
        print("not key rpate")
        return counts
    if(len(addNameTesk) <= 0 and len(addStatus) <= 0 and len(addPriority) <= 0):
        print("you have to writing 1 word")
        return counts
    addStatus = vorody("what is status task (true or false):")
    if addStatus not in ("true" ,  "false") :
        print("Erorr : you have to write in the Statue (true or false)") 
        return counts    
    addPriority = vorody("what is priority task (High , Medium , Low):") 
    if addPriority not in ("High" , "Medium" , "Low"):
        print("Erorr : you have to write in the Statue (High or Medium or Low)")
        return counts
    task_List[addNameTesk] = {"status" : addStatus , "priority" : addPriority}
    print("task added") 
    counts += 1        
    undoList.append(next(reversed(task_List.items())))
    SaveTasks(task_List)       
    print(undoList)
    return counts        
def showTesk(addTeskList):
    for k , v in addTeskList.items():
        print(k)
def deleting(items , undoList):
    if len(undoList) is not 0 :
        undoList.clear()     
    deleted = vorody("which delete you tesk : ")
    if(len(deleted) <= 0 ):
        print("you have to writing 1 word") 
        return 
    else : 
        if items.get(deleted) : 
            undoList.append(next(reversed(task_List.items()))) 
            items.pop(deleted)
            print(undoList)
            SaveTasks(items)        
            print(f"item {deleted} deleted")          
        else : print("not find")        
def EditTesk(TeskList ,undoList):
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
            undoList.append(next(reversed(task_List.items()))) 
            TeskList.pop(itemEdit)
            TeskList[newName] = {"status" : status , "priority" : priority }
            print(task_List)
            SaveTasks(TeskList)              
            print("Edit did")
def Search(teskList):
    itmeSearch = vorody("Are you looking for :")
    isCheckSeaech = False
    for k , v in teskList.items():
        if k[:len(itmeSearch)] == itmeSearch: 
            isCheckSeaech=True
            print(k)
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


def UndoOption(listTask , undoList , counts , redoList):
    if(len(undoList) <= 0 ) :
        print("this list is empy")
        return counts , redoList  
    if redoList : 
        redoList.clear()  
    is_right = undoList[-1][0]
    if is_right in listTask :
        k , v = listTask.popitem()
        redoList["add"] = {k:v}
        SaveTasks(listTask)             
    elif len(listTask) < counts:
        print("BEFORE:")
        print(len(listTask), counts)
        key, value = undoList.pop()
        listTask[key] = value
        redoList["del"] = {key : value}
        print(redoList)
        SaveTasks(listTask)       
        counts = len(listTask)
        print("AFTER:")
        print(len(listTask), counts)
    else : 
        key , value = undoList.pop()
        redokey , redovalue = listTask.popitem()
        listTask[key] = value
        redoList["Edit"] = {redokey : redovalue}
        SaveTasks(listTask)       
        print(listTask)
    return counts , redoList   
def Redo(tasklist , redo):
    if(len(redo) <= 0 ) :
        print("this list is empy")
        return
    k , v =redo.popitem() 
    if(k == "add") : 
        k2 , v2 = v.popitem() 
        tasklist[k2] = v2
        SaveTasks(tasklist)
        
        print(k , v , "                " , k2 , v2)
    elif k== "del" :
        keyDel ,valueDel = v.popitem()
        if tasklist.get(keyDel):
            tasklist.popitem()
            SaveTasks(tasklist)
        print(keyDel , valueDel)
    else:
        keyEdit ,valueEdit = v.popitem()
        tasklist.popitem()
        tasklist[keyEdit] = valueEdit
        SaveTasks(tasklist)
        print(keyEdit , valueEdit)                
def SaveTasks(task_List):
    file = open("tasks.json" ,"w")
    json.dump(task_List , file)
    file.close() 
def LoadTasks():
    file = open("tasks.json" , "r")
    data = json.load(file) 
    file.close()  
    return data 

# def SaveUndo(undoList):
#     file = open("undoList.json" , "w")
#     json.dump(undoList)
#     file.close()
# def LoadUndo():
#     with open("undoList.json", "r") as file:
#         if file.read().strip() == "":
#             return []

#         file.seek(0)
#         data = json.load(file)

#     return data  
                   
                    
task_List = LoadTasks()
UndoList =[]
RedoList = {}
count = len(task_List)               
                
            
        
            
        
                
    
            


while checked : 
    choose_task_option = input("you choose your option :")
    if(choose_task_option == "1"):
      count = add_task(task_List , UndoList , count)
    elif(choose_task_option == "2"):
        showTesk(task_List)
    elif(choose_task_option == "3"):
        deleting(task_List , UndoList)
    elif(choose_task_option == "4"):
        checked = False
    elif(choose_task_option == "5"):
        EditTesk(task_List , UndoList) 
    elif(choose_task_option == "6"):
        Search(task_List) 
    elif(choose_task_option == "7"):
         EditVazeat(task_List)
    elif(choose_task_option == "8"):
         Fillter(task_List) 
    elif(choose_task_option == "9"):
        SortKeyDisaen(task_List) 
    elif (choose_task_option == "10"):
        count , RedoList = UndoOption(task_List , UndoList , count , RedoList)
    elif (choose_task_option == "11"):
        Redo(task_List , RedoList)
                     
                                           
        
        
 
