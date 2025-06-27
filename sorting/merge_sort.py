def merge_sort(lst):
    if len(lst)==1:
        return
    m=len(lst)//2
    left_arr=lst[:m]
    right_arr=lst[m:]
    merge_sort(left_arr)
    merge_sort(right_arr)

    merge(left_arr,right_arr,lst)

    return lst

def merge(L,R,lst):
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            lst[k]=L[i]
            i+=1
        else:

            lst[k]=R[j]
            j+=1
        k+=1
    while i< len(L):
        lst[k]=L[i]
        k+=1
        i+=1

    while j< len(R):
        lst[k]=R[j]
        k+=1
        j+=1






datalst=list(map(int,input("enter the list of numbers:").split()))
print(f"unsorted list:{datalst}\n")
print(f"sorted list:{merge_sort(datalst)}")