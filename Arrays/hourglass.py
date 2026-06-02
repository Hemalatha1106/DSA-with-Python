s="RADAR"
for i in range(len(s)):
    if i==0 or i==len(s)-1:
        for i in range(len(s)):
            print("*",end="")
        print(" ")    
    if i==1 or i==3:
        for i in range(len(s)):
            if i%2:
                print("*",end="")
            else:
                print(" ",end="")
        print("")        
    elif i==2:
        for i in range(len(s)):
            if i==2:
                print("*",end="")
            else:
                print(" ",end="")  
        print("")                                  