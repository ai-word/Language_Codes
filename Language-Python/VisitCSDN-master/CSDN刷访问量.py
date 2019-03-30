import webbrowser as web
# from pymouse import PyMouse
import requests
from bs4 import BeautifulSoup
import time
import random

#需要访问的博客地址
blog_url = [
    'https://blog.csdn.net/weixin_42449444/article/details/85248669',
    'https://blog.csdn.net/weixin_42449444/article/details/84440760',
    'https://blog.csdn.net/weixin_42449444/article/details/82989917',
    'https://blog.csdn.net/weixin_42449444/article/details/82900905',
    'https://blog.csdn.net/weixin_42449444/article/details/84859910',
    'https://blog.csdn.net/weixin_42449444/article/details/86294714',
    'https://blog.csdn.net/weixin_42449444/article/details/86248248',
    'https://blog.csdn.net/weixin_42449444/article/details/86232692',
    'https://blog.csdn.net/weixin_42449444/article/details/85785671',
    'https://blog.csdn.net/weixin_42449444/article/details/84981665',
    'https://blog.csdn.net/weixin_42449444/article/details/84966158',
    'https://blog.csdn.net/weixin_42449444/article/details/84953351',
    'https://blog.csdn.net/weixin_42449444/article/details/84949680',
    'https://blog.csdn.net/weixin_42449444/article/details/84949693',
    'https://blog.csdn.net/weixin_42449444/article/details/86186192',
    'https://blog.csdn.net/weixin_42449444/article/details/86181257',
    'https://blog.csdn.net/weixin_42449444/article/details/86178278',
    'https://blog.csdn.net/weixin_42449444/article/details/86163191',
    'https://blog.csdn.net/weixin_42449444/article/details/85630499',
    'https://blog.csdn.net/weixin_42449444/article/details/83184083',
    'https://blog.csdn.net/weixin_42449444/article/details/83183639',
    'https://blog.csdn.net/weixin_42449444/article/details/82951487',
    'https://blog.csdn.net/weixin_42449444/article/details/82943656',
    'https://blog.csdn.net/weixin_42449444/article/details/82901678',
    'https://blog.csdn.net/weixin_42449444/article/details/84867642',
    'https://blog.csdn.net/weixin_42449444/article/details/84867564',
    'https://blog.csdn.net/weixin_42449444/article/details/84867215',
    'https://blog.csdn.net/weixin_42449444/article/details/84867268',
    'https://blog.csdn.net/weixin_42449444/article/details/84866104',
    'https://blog.csdn.net/weixin_42449444/article/details/84865945',
    'https://blog.csdn.net/weixin_42449444/article/details/84865834',
    'https://blog.csdn.net/weixin_42449444/article/details/84865634',
    'https://blog.csdn.net/weixin_42449444/article/details/84865691',
    'https://blog.csdn.net/weixin_42449444/article/details/85267630',
    'https://blog.csdn.net/weixin_42449444/article/details/85266144',
    'https://blog.csdn.net/weixin_42449444/article/details/83343843',
    'https://blog.csdn.net/weixin_42449444/article/details/84917553',
    'https://blog.csdn.net/weixin_42449444/article/details/85238893',
    'https://blog.csdn.net/weixin_42449444/article/details/85238984',
    'https://blog.csdn.net/weixin_42449444/article/details/84918853',
    'https://blog.csdn.net/weixin_42449444/article/details/84889087',
    'https://blog.csdn.net/weixin_42449444/article/details/82989917',
    'https://blog.csdn.net/weixin_42449444/article/details/86365386',
    'https://blog.csdn.net/weixin_42449444/article/details/86309368',
    'https://blog.csdn.net/weixin_42449444/article/details/86317508',
    'https://blog.csdn.net/weixin_42449444/article/details/86188179',
    'https://blog.csdn.net/weixin_42449444/article/details/86156602',
    'https://blog.csdn.net/weixin_42449444/article/details/86148588',
    'https://blog.csdn.net/weixin_42449444/article/details/85404271',
    'https://blog.csdn.net/weixin_42449444/article/details/85621946',
    'https://blog.csdn.net/weixin_42449444/article/details/85399238',
    'https://blog.csdn.net/weixin_42449444/article/details/85343561',
    'https://blog.csdn.net/weixin_42449444/article/details/85338047',
    'https://blog.csdn.net/weixin_42449444/article/details/85337673',
    'https://blog.csdn.net/weixin_42449444/article/details/85337497',
    'https://blog.csdn.net/weixin_42449444/article/details/85331082',
    'https://blog.csdn.net/weixin_42449444/article/details/85318582',
    'https://blog.csdn.net/weixin_42449444/article/details/85316236',
    'https://blog.csdn.net/weixin_42449444/article/details/85316127',
    'https://blog.csdn.net/weixin_42449444/article/details/85316003',
    'https://blog.csdn.net/weixin_42449444/article/details/85146975',
    'https://blog.csdn.net/weixin_42449444/article/details/85016221',
    'https://blog.csdn.net/weixin_42449444/article/details/85017022',
    'https://blog.csdn.net/weixin_42449444/article/details/85016712',
    'https://blog.csdn.net/weixin_42449444/article/details/85016619',
    'https://blog.csdn.net/weixin_42449444/article/details/85016465',
    'https://blog.csdn.net/weixin_42449444/article/details/85016265',
    'https://blog.csdn.net/weixin_42449444/article/details/84997106',
    'https://blog.csdn.net/weixin_42449444/article/details/84997039',
    'https://blog.csdn.net/weixin_42449444/article/details/85009447',
    'https://blog.csdn.net/weixin_42449444/article/details/84966850',
    'https://blog.csdn.net/weixin_42449444/article/details/84966799',
    'https://blog.csdn.net/weixin_42449444/article/details/84966738',
    'https://blog.csdn.net/weixin_42449444/article/details/84966643',
    'https://blog.csdn.net/weixin_42449444/article/details/84966703',
    'https://blog.csdn.net/weixin_42449444/article/details/84963453',
    'https://blog.csdn.net/weixin_42449444/article/details/84949551',
    'https://blog.csdn.net/weixin_42449444/article/details/84933947',
    'https://blog.csdn.net/weixin_42449444/article/details/84934014',
    'https://blog.csdn.net/weixin_42449444/article/details/84934038',
    'https://blog.csdn.net/weixin_42449444/article/details/84919835',
    'https://blog.csdn.net/weixin_42449444/article/details/84919386',
    'https://blog.csdn.net/weixin_42449444/article/details/84918765',
    'https://blog.csdn.net/weixin_42449444/article/details/84918152',
    'https://blog.csdn.net/weixin_42449444/article/details/84889188',
    'https://blog.csdn.net/weixin_42449444/article/details/84889149',
    'https://blog.csdn.net/weixin_42449444/article/details/84889122',
    'https://blog.csdn.net/weixin_42449444/article/details/84867752',
    'https://blog.csdn.net/weixin_42449444/article/details/84888936',
    'https://blog.csdn.net/weixin_42449444/article/details/84888960',
    'https://blog.csdn.net/weixin_42449444/article/details/84866400',
    'https://blog.csdn.net/weixin_42449444/article/details/84866000',
    'https://blog.csdn.net/weixin_42449444/article/details/84865737',
]

def getHTML(url):
    # 首页地址
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  #指定编码格式
        demo = r.text  # 获取网页的源代码
        # print('网页源代码获取成功！')
        return demo
    except:
        print('爬取失败。')

def getViews(): #获取总访问量
    url = 'https://blog.csdn.net/weixin_42449444'
    demo = getHTML(url)
    soup = BeautifulSoup(demo, 'html.parser')
    # print(soup.prettify())
    tag = soup.find_all('dl')
    # print(tag)
    count = int(tag[-3].contents[3]['title'])
    #print('博客当前访问量:' + str(count))
    return count

def Main():
    start = getViews()   #开始前的访问次数
    t1 = time.time()
    print('当前博客访问量:'+str(start))
    maxTime = eval(input('请输入需要访问的次数：'))
    count = 0 #当前打开的网页数
    for i in range(maxTime):
        time.sleep(1)  # 这个时间根据自己电脑处理速度设置，单位是s
        randomLink = random.choice(blog_url)
        print('已经访问了{}次了。这次随机访问的博客链接是{}'.format(i+1,randomLink))
        web.open_new_tab(randomLink)
        count += 1
        if count == 20:   #20个网页时就关闭浏览器,休息一下
            time.sleep(8)
            # PyMouse().click(1508, 8)  # 鼠标移动到(1535,0)处点击,即关闭浏览器
            count = 0
    # PyMouse().click(1535, 0)  #结束时,鼠标移动到(1535,0)处点击,即关闭浏览器
    end = getViews()    #结束时的访问次数
    t2 = time.time()
    count = end-start    #有效访问次数
    min,s = divmod(t2-t1,60)
    h,min = divmod(min,60)
    print('任务完成！总耗时为{}时{}分{:.2f}秒,总共访问次数为{},有效访问次数为{},有效访问率为{:.2f}%。'.format(h,min,s,maxTime,count,100*(count/maxTime)))
    print('当前博客访问量:'+str(end))

if __name__ == '__main__':
    Main()