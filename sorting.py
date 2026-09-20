def SortKeyDisaen(listSort, command , saveCommand):
     items = list(listSort.items())
     SortKey(items , 0  , len(listSort) - 1)  
     listSort.clear()
     listSort.update(items)  
     command.append("sort")
     saveCommand(command)
def SortKey(List_sort , start , end):
    if start >= end  :  return
    boundery = partition(List_sort , start , end )
    SortKey(List_sort , start , boundery -1)
    SortKey(List_sort , boundery + 1 , end)
       
def partition(items , start , end):
    piovt = items[end][0]
    boundary = start 
    for itemsSort in range(start ,end):
        if items[itemsSort][0] <= piovt :
            boundary+=1
            swap(items , itemsSort , boundary) ##ببین تو این خط میخوام عمیلات صورت رو روی تاپل انجام بده برای همین مشخص نکردم key باش یا value     
    swap(items , boundary , end)
    return boundary 
            
            
def swap(array , index1 , index2):
    teamp = array[index1]
    array[index1] = array[index2]
    array[index2] = teamp 