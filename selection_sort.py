def selection_sort(lst):
    for i in range(len(lst)):
        min_index=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min_index]:
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst

datalst=list(map(int,input("enter the list of numbers:").split()))
print(f"unsorted list:{datalst}\n")
print(f"sorted list:{selection_sort(datalst)}")