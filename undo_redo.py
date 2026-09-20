from storage import SaveRedo, SaveTasks
def UndoOption(listTask , undoList  , redoList, command , saveCommand):
    if(len(undoList) <= 0 ) :
        print("this list is empy")
        return redoList  
    if redoList : 
        redoList.clear()  
    k , v =undoList.popitem() 
    if k == "add":
        keyadd , valueadd = listTask.popitem()
        redoList["add"] = {keyadd:valueadd}
        SaveRedo(redoList)
        SaveTasks(listTask)         
    elif k == "del":
        key, value = v.popitem()
        listTask[key] = value
        redoList["del"] = {key : value}
        SaveRedo(redoList)
        SaveTasks(listTask)       
    else : 
        key , value = v.popitem()
        redokey , redovalue = listTask.popitem()
        listTask[key] = value
        redoList["Edit"] = {redokey : redovalue}
        SaveRedo(redoList)
        SaveTasks(listTask) 
    command.append("Undo")
    saveCommand(command)          
    return redoList 
  
def Redo(tasklist , redo , command , saveCommand):
    if(len(redo) <= 0 ) :
        print("this list is empy")
        return
    k , v =redo.popitem() 
    if(k == "add") : 
        k2 , v2 = v.popitem() 
        tasklist[k2] = v2
        SaveTasks(tasklist)
    elif k == "del":
        keyDel, valueDel = v.popitem()

        if keyDel in tasklist:
            tasklist.pop(keyDel)
        SaveTasks(tasklist)
    else:
        keyEdit ,valueEdit = v.popitem()
        tasklist.popitem()
        tasklist[keyEdit] = valueEdit
        SaveTasks(tasklist) 
    command.append("Redo")
    saveCommand(command)  