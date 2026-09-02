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
    addvazeat = vorody("what is vazeat task :")
    if(len(addNameTesk) <= 0 ):
        print("you have to writing 1 word")   
    else :
        if task_List.get(addNameTesk):
            print("not key rpate")
        else :    
            task_List[addNameTesk] = addvazeat
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
            vazeat  = vorody("what is new vazeat's tesk :")
            TeskList.pop(itemEdit)
            TeskList[newName] = vazeat
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
        
        
 
