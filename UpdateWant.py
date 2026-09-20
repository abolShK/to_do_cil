from utils import vorody
def upatedStateAfew(listTask , saveTask , command , saveCommand , name): 
    if not name :  
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
                command.append("UpdateWant")
                saveCommand(command)
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
    else : 
        for nameUpdateStatus in name : 
            if nameUpdateStatus in listTask :
                newStateTask = vorody(f"what do you new state task {nameUpdateStatus}:(true or false)")
                if newStateTask not in ("true" , "false") : 
                    print("new status have to true or false")
                    return
                listTask[nameUpdateStatus]["status"]=newStateTask
                saveTask(listTask)
                command.append("UpdateWant")
                saveCommand(command)
            else :
                print("it is not find")
                continue 
                          