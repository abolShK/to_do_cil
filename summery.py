from is_check_name_in_functins import is_check_name_in_function
def Summry (summry , command , saveCommand , name):
    summeruValue = is_check_name_in_function(name , "do you wanna weich summery(High, Medium, Low)")
    if summeruValue not in ("High" , "Medium" , "Low"):
        print("you have to choose in (High, Medium, Low)")
        return
    value = summry.get(summeruValue)  
    print(f"summmery {summeruValue} = {value}")  
    command.append("showSummery")
    saveCommand(command)
    return summry  