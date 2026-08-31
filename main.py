# lst's start new project 
print("1 . add task")
print("2 . show task")
print("3 . Delet task")
print("4 . Exit task")
task_List = {}
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
            task_List[addNameTesk] = task_List
            print("task added")    
def showTesk(addTeskList):
    for i in addTeskList:
        print(i)
def deleting(items):
    deleted = vorody("which delete you tesk : ")
    if(len(deleted) <= 0 ):
        print("you have to writing 1 word")  
    else : 
        if items.get(deleted) : 
            items.pop(deleted)
            print(f"item {deleted} deleted")
        else : print("not find")        
    
            
            


while True : 
    choose_task_option = input("you choose your option :")
    if(choose_task_option == "1"):
       add_task(task_List)
    if(choose_task_option == "2"):
        showTesk(task_List)
    if(choose_task_option == "3"):
        deleting(task_List)
        
        
 
