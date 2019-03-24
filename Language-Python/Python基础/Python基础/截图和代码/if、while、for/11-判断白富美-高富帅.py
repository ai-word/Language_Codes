sex = input("请输入你的性别:")

#如果当前用户是男性的话,那么就输入判断女性的要求
if sex=="男":
    color = input("你白么?") #白 或者 黄
    money = int(input("请输入你的财产总和:")) #输入1000
    beautiful = input("你美么?")#美 或者 普通

    #if 白 并且 富 并且 美:
    #if 白 and 富 and 美:
    if color=="白" and money>1000000 and beautiful=="美":
        print("白富美....")
    else:
        print("矮矬穷....")
else:
    print("判断高富帅的信息在下面....")
