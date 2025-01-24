if __name__ == "__main__":
    data=list(map(int,input("enter the list of input leaving one lonley interger:").split()))
    data_len=len(data);
    
    res=data[0]
    for i in range(1,data_len):
        res^=data[i]
        
    print("The lonely integer is :",res)
    
