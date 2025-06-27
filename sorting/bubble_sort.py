# <!-- optimized bubble sort -->
def bubblesort(lstitems):
    for i in range(len(lstitems)):
        swapped=False
        for j in range(len(lstitems)-i-1):
            if lstitems[j]>lstitems[j+1]:
                lstitems[j],lstitems[j+1]=lstitems[j+1],lstitems[j]
                swapped=True
        if not swapped:
            break;
    
    return lstitems
datalst=list(map(int,input("Enter the list of numbers:").split()))
print(f"unsorted list:{datalst}\n")
print(f"sorted list:{bubblesort(datalst)}")