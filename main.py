# lst's start new project 
print("1 . add task")
print("2 . show task")
print("3 . Delet task")
print("4 . Exit task")
print("5 . Edit task")
print("6 . Search task")
task_List = {}
checked = True
def vorody(testVoridy):
   return input(testVoridy)
def add_task(task_List):
    addNameTesk = vorody("what is name task :")
    if(len(addNameTesk) <= 0 ):
        print("you have to writing 1 word")   
    else :
        if task_List.get(addNameTesk):
            print("not key rpate")
        else :    
            task_List[addNameTesk] = addNameTesk
            print("task added")    
def showTesk(addTeskList):
    for k , v in addTeskList.items():
        print(v)
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
            TeskList.pop(itemEdit)
            TeskList[newName] = newName
            print(task_List)
            print("Edit did")
def Search(teskList):
    itmeSearch = vorody("Are you looking for :")
    isCheckSeaech = False
    for k , v in teskList.items():
        if v[:len(itmeSearch)] == itmeSearch: 
            isCheckSeaech=True
            print(v)
    if isCheckSeaech == False:         
        print("anyting is'ent name")            
                
            
        
            
        
                
    
            


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
        
        
 
