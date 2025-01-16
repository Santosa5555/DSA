#   program to check if k-th bit of a given number is set or not
def bit_set(num,k):
    if num & (1<<k):
        return True
    else:
       return False  
        #  or num & (1*(2**k))


if __name__== "__main__":
   num = int(input("Enter the number: "))
   k = int(input("Enter the bit position (k): "))
   if bit_set(num,k):
        print(f"the {k}th bit is set")
   else:
        print(f"the {k}th bit is not set")