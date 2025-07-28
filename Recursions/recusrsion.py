def recusriveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        # if you want to print in descending order print before recursive function
        #print(n)
        recusriveMethod(n-1)
        # if you want to print in ascending order print after recursive function
        print(n)


recursive function
recusriveMethod(20)