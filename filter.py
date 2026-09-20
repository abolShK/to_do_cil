from main import vorody
def _FillterStatus(listFillter):
    print("1 . all show")
    print("2 . done show")
    print("3 . not done show")
    chooseShowTeskFillter = vorody("do you choose :")
    if chooseShowTeskFillter not in ("1","2","3"): 
        print("this number is incorract")
    else :     
        for key , value in listFillter.items() : 
            if chooseShowTeskFillter == "1" or chooseShowTeskFillter == "all show":
                print(key)
            elif chooseShowTeskFillter == "2" or chooseShowTeskFillter =="done show" and value["status"] == "true":
                    print(key)
            elif chooseShowTeskFillter == "3" or "not done show" and value["status"] == "false":
                    print(key)                  
def _FiltterPriority(listFillter):
    print("1 . High")
    print("2 . Medium")
    print("3 . Low")
    chooseShowTeskFillter = vorody("do you choose :")
    if chooseShowTeskFillter not in ("1","2","3"): 
        print("this number is incorract")
    else :    
        for key , value in listFillter.items() : 
            if chooseShowTeskFillter == "1" or "High" and value["priority"] == "High":
                print(key)
            elif chooseShowTeskFillter == "2" or "medium" and value["priority"] == "Medium":
                print(key)
            elif chooseShowTeskFillter == "3" or "Low" and value["priority"] == "Low":
                print(key)    
        if chooseShowTeskFillter not in ("1","2","3"): 
            print("this number is incorract")
def Fillter(listFilter , command , saveCommand):
    print("1 . fillter priority")
    print("2 . Fillter status")    
    chooseMethodFilltering = vorody("you choose wiche method fillters :")
    if chooseMethodFilltering == "1" or chooseMethodFilltering == "fillter priority" :
        _FiltterPriority(listFilter)
        command.append("fillterPriority")
    elif chooseMethodFilltering == "2"or chooseMethodFilltering == "fillter status" : 
        _FillterStatus(listFilter)
        command.append("fillterStatus")
    else : print("this number is'en in the Selection list") 
    
    saveCommand(command) 