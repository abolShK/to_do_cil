from utils import vorody
def delwant(tasklist , savaTask , history, saveHistory , command , saveCommand , nameList):
    if not tasklist :
        print("task list  empyied")
        return
    if not nameList : 
        taskDelete = vorody("do you want delete task ?")
        if taskDelete in tasklist :
            tasklist.pop(taskDelete)
            history.append({"deleted" : taskDelete}) 
            saveHistory(history)
            print(f"this {taskDelete} deleted")
            savaTask(tasklist)
            command.append("dlewant")
            saveCommand(command)
            is_couinti = vorody("do you want continue : (yes,no)")
            if is_couinti not in ("yes" , "no"):
                print("vorody is  incorrect")
                return
            else:
                if is_couinti == "yes" : 
                    delwant(tasklist , savaTask ,history , saveHistory, command , saveCommand , nameList)
                else : 
                    return   
        else : 
            print("it is not find")
    else :  
        for nameDel in nameList: 
            if nameDel in tasklist :
                history.append({"deleted" : nameDel}) 
                saveHistory(history)
                print(f"this {nameDel} deleted")
                tasklist.pop(nameDel)
                savaTask(tasklist)
                command.append("dlewant")
                saveCommand(command)
            else : 
                print(f"not found {nameDel} task")
                continue                 
                                        