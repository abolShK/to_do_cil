# lst's start new project 
print("1 . add task")
print("2 . show task")
print("3 . Delet task")
print("4 . Exit task")
print("5 . Edit task")
print("6 . Search task")
print("7 . Edit vazeat's task")
print("8 . Fillter task")
task_List = {}
checked = True
def vorody(testVoridy):
   return input(testVoridy)
def add_task(task_List):
    addNameTesk = vorody("what is name task :")
    addStatus = vorody("what is status task (true or false):")
    addPriority = vorody("what is priority task (High , Medium , Low):")
    if(len(addNameTesk) <= 0 and len(addStatus) <= 0 and len(addPriority) <= 0):
        print("you have to writing 1 word")   
    else :
        if task_List.get(addNameTesk):
            print("not key rpate")
        else :    
            task_List[addNameTesk] = {"status" : addStatus , "addpriority" : addPriority}
            print("task added")    
def showTesk(addTeskList):
    for k , v in addTeskList.items():
        print(k)
def deleting(items):
    deleted = vorody("which delete you tesk : ")
    if(len(deleted) <= 0 ):
        print("you have to writing 1 word")  
    else : 
        if items.get(deleted) : 
            items.pop(deleted)
            print(f"item {deleted} deleted")
        else : print("not find")
def EditTesk(TeskList):
    itemEdit = vorody("which do yot tesk Edit :")
    if(len(itemEdit) <= 0 ):
        print("you have to writing 1 word") 
    else:             
        if(not(TeskList.get(itemEdit))):
            print("this tesk is'nt in the tesk list")
        else:
            newName  = vorody("what is new name's tesk :")
            status  = vorody("what is new status's tesk (true or false):")
            priority  = vorody("what is new status's tesk (High , Medium , Low):")
            TeskList.pop(itemEdit)
            TeskList[newName] = {"status" : status , "priority" : priority }
            print(task_List)
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
def Fillter(listFillter):
    print("1 . all show")
    print("2 . done show")
    print("3 . not done show")
    chooseShowTeskFillter = vorody("do you choose :")
    for key , value in listFillter.items() : 
        if chooseShowTeskFillter == "1":
            print(key)
        elif chooseShowTeskFillter == "2":
            if value == "true" : 
                print(key)
        elif chooseShowTeskFillter == "3":
            if value == "false" : 
                print(key)  
    else : print("this number is incorract") 

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

                
            
                     
                
            
        
            
        
                
    
            


while checked : 
    choose_task_option = input("you choose your option :")
    if(choose_task_option == "1"):
       add_task(task_List)
    elif(choose_task_option == "2"):
        showTesk(task_List)
    elif(choose_task_option == "3"):
        deleting(task_List)
    elif(choose_task_option == "4"):
        checked = False
    elif(choose_task_option == "5"):
        EditTesk(task_List) 
    elif(choose_task_option == "6"):
        Search(task_List) 
    elif(choose_task_option == "7"):
         EditVazeat(task_List)
    elif(choose_task_option == "8"):
         Fillter(task_List) 
    elif(choose_task_option == "9"):
        SortKeyDisaen(task_List)   
                                           
        
        
 
