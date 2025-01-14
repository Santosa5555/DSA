
def binarySearch(list,low,high,x):
    lenlist=len(list)
    while(low<=high):
        mid=(low+high)//2;
        if(list[mid]==x):
            return mid
        elif(list[mid]>x):
            
            high=mid-1
    
        else:
            low=mid+1
    
    return -1

if __name__== '__main__':
    print("enter the sorted data:")
    data = list(map(int, input().split()))
    print("enter the element to be searched:")
    element = int(input())
    high=len(data)-1
    result = binarySearch(data,0,high, element)
    if(result==1):
        print("found the element at position",result)
    else:
        print("donot found the element ")
