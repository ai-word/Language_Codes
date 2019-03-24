i = 1

while i<=9:

    j = 1
    while j<=i:
        print("%d*%d=%d\t"%(j,i,i*j), end="")
        j+=1

    print("")

    i+=1
