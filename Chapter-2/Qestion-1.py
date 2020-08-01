for i in range(1950,2051):
    #print(i)
    if(i % 4 == 0):
        if(i % 100 != 0):
            print(i, end=" ")
        if(i % 100 == 0) and (i % 400 == 0):
            print(i, end=" ")
