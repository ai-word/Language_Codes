color = input("你白么?") #白 或者 黄
money = int(input("请输入你的财产总和:")) #输入1000
beautiful = input("你美么?")#美 或者 普通

if color=="白" and money>1000000 and beautiful=="美":
    print("白富美....")
    print("好羡慕......")
else:
    print("矮矬穷....")

#下面的代码 不会因为上面第5行的if条件满足或者不满足而不一样,即 他们之间没有任何关系
print("矮矬穷....")
print("矮矬穷....")
print("矮矬穷....")
