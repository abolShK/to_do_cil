# lst's start new project 
print("1 . add task")
print("2 . show task")
print("3 . Delet task")
print("4 . Exit task")
task_List = {}
def add_task(task_List):
    name_task = input("what is name task :")
    if(len(name_task) <= 0 ):
        print("you have to writing 1 word")   
    else :
        if task_List.get(name_task):
            print("not key rpate")
        else :    
            task_List[name_task] = task_List
            print("task added")    
def showTesk(addTeskList):
    for i in addTeskList:
        print(i)
def deleting(items):
    deleted = input("what is deleted tesk")
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
        
        
 
