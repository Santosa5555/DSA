# num&(1<<0) for 0th bit check set or not and return 1 if set
def countSetBit(num):
    count=0            
    while(num>0):
        if(num&(1<<0)):
            count+=1
        num=num>>1
    return count    

if __name__== "__main__":
   num = int(input("Enter the number: "))
   print("The number of set bit is:",countSetBit(num))

