
def quick_sort(lst):
    n = len(lst)
    if n <= 1:  
        return lst

    pivot_index = n - 1  
    i = -1
    j = 0

    while j < pivot_index:  
        if lst[j] < lst[pivot_index]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]  
        j += 1

    lst[i + 1], lst[pivot_index] = lst[pivot_index], lst[i + 1]
    pivot = i + 1

    quick_sort(lst[:pivot])
    quick_sort(lst[pivot + 1:])

    return lst

if __name__ == "__main__":
    datalst = list(map(int, input("Enter the list of numbers: ").split()))
    print(f"Unsorted list: {datalst}\n")
    print(f"Sorted list: {quick_sort(datalst)}")
















































    