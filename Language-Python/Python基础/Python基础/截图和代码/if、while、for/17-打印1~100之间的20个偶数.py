i = 1
num = 0
while i<=100:
    #if i是个偶数:
    if i%2==0:
        print(i)
        num+=1

    if num==20:
        #break的作用 用来结束while循环,
        #即 如果在while执行的过程中,不想循环了,可以用break来做到这个效果0:
        break

    i+=1
