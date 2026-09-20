def showTesk(addTeskList , command , saveCommand):
    for k , v in addTeskList.items():
        if(v["pin"] == "true"):
            print(k)
    for k , v in addTeskList.items() :
        if v["pin"] == "false" : 
            print(k)
    command.append("showTask")
    saveCommand(command)  