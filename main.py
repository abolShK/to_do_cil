# lst's start new project 
print("1 . add task")
print("2 . show task")
print("3 . Delet task")
print("4 . Exit task")
task_List = []
def add_task(task_List):
    name_task = input("what is name task :")
    if(len(name_task) <= 0 ):
        print("you have to writing 1 word")   
    else :
        task_List.append(name_task)
        print("task added")
    return task_List    
def showTesk(addTeskList):
    for i in addTeskList:
        print(i)
            

    
while True : 
    returnedAddtesk
    choose_task_option = input("you choose your option :")
    if(choose_task_option == "1"):
       returnedAddtesk =  add_task(task_List)
    if(choose_task_option == "2"):
        showTesk(returnedAddtesk)
 
