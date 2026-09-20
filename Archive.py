from is_check_name_in_functins import is_check_name_in_function
from storage import saveArchive , SaveTasks
def add_archive(taskList , archiveList , command , saveCommand , name):
    name_archive = is_check_name_in_function(name,"you choose weich task for added archive:")
    if not(name_archive) : 
        print("this vorody is a word on the in it")
        return
    if name_archive in (archiveList) : 
        print(f"there is {name_archive} in the taskList or archiveList ")
        return
    if name_archive in taskList :
        archiveitemDelete = taskList.pop(name_archive)
        archiveList[name_archive] = archiveitemDelete
        saveArchive(archiveList)
        SaveTasks(taskList)
        command.append("addArchive")
        saveCommand(command)
    else : 
        print(f"there is not {name_archive} on the taskList") 
        return 