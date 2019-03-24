color = input("你白么?") #白 或者 黄
money = int(input("请输入你的财产总和:")) #输入1000
beautiful = input("你美么?")#美 或者 普通

#if 白 并且 富 并且 美:
#if 白 and 富 and 美:
if color=="白" and money>1000000 and beautiful=="美":
    print("白富美....")
else:
    print("矮矬穷....")
