def insertion_sort(lst):
    for i in range(1,len(lst)):
        temp=lst[i]
        j=i-1
        while j>=0 and lst[j]>temp:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=temp
    return lst

datalst=list(map(int,input("enter the list of numbers:").split()))
print(f"unsorted list:{datalst}\n")
print(f"sorted list:{insertion_sort(datalst)}")