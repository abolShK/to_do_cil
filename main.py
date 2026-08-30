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

    
while True : 
    choose_task_option = input("you choose your option :")
    if(choose_task_option == "1"):
        add_task(task_List)
 
