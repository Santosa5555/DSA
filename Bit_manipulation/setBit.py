# set the ith bit


def set_bit(num,k):
    return (num | (1<<k))
if __name__== "__main__":
   num = int(input("Enter the number: "))
   k = int(input("Enter the bit position to set (k): "))
   
   print(f"the {k}th bit is set",set_bit(num,k))
