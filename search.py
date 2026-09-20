from datetime import datetime , date
from is_check_name_in_functins import is_check_name_in_function

def Search(teskList , command , saveCommand , name):
    itmeSearch = is_check_name_in_function(name , "which task are you loking :")
    isCheckSeaech = False
    for k , v in teskList.items():
        if k[:len(itmeSearch)] == itmeSearch: 
            isCheckSeaech=True
            print(k)
            input_date = datetime.strptime(
                v["date"],
                "%Y-%m-%d"
            ).date()
            if date.today() > input_date:
                print("date is in the past")
            elif date.today() < input_date : 
                print("date is not the past")
            else : "today is last day to do it"        
            
    if isCheckSeaech == False:         
        print("anyting is'ent name")
    else :
        command.append("serach")
        saveCommand(command)  