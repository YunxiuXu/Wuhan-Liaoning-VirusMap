from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

import ssl

#当使用urllib.urlopen打开一个 https 链接时，会验证一次 SSL 证书。而当目标网站使用的是自签名的证书时就会抛出异常 解决方法：全局取消证书验证
info_txt = ""
def getLiaoningCity():
    global info_txt
    ssl._create_default_https_context = ssl._create_unverified_context
    # if has Chinese, apply decode()
    html = urlopen("http://wsjk.ln.gov.cn/wst_wsjskx/").read().decode('gb2312')
    soup = BeautifulSoup(html, features='lxml')

    links = []


    for i in soup.find_all('a', text = re.compile('疫情情况')):
        links.append(i)

    #for i in links:
        #print(i)
        #print(i.get('href'))

    #以上为爬取全部的疫情信息公告链接，link[0]即为最新疫情信息

    html2 = urlopen("http://wsjk.ln.gov.cn/wst_wsjskx/" + str(links[0].get('href'))).read().decode('gb2312')#0号为最先
    soup2 = BeautifulSoup(html2, features='lxml')

    #print(soup2.find_all('p')[2])
    #print(soup2.find_all('p', class_='MsoNormal')[1])

    info = soup2.find_all('p', class_='MsoNormal')[1]#MsoNormal我也不知道是什么 只有疫情信息使用了这个样式 故算作特征
    info_txt = info.text#只留下字符
    print(info_txt )

    city = ['沈阳市', '大连市', '鞍山市', '抚顺市', '本溪市', '丹东市', '锦州市', '营口市', '阜新市', '辽阳市', '铁岭市', '朝阳市', '盘锦市', '葫芦岛市']
    city_dict = {'沈阳市':0, '大连市':1, '鞍山市':2, '抚顺市':3, '本溪市':4, '丹东市':5, '锦州市':6, '营口市':7, '阜新市':8, '辽阳市':9, '铁岭市':10, '朝阳市':11, '盘锦市':12, '葫芦岛市':13}
    city_num = []#从沈阳开始依次的城市确诊数量


    for i in city:
        str1 = i + '\d+' + '例' #正则表达式写法 市名+数字
        str_city = re.findall(str1, info_txt)#从文字中提取所有城市+数字 例:'本溪市9例' 正则表达式 '例' 可以省略
        #print(str_city)
        if(len(str_city) > 0):#如果这个城市非0
            city_num.append(int(re.findall('\d+', str_city[0])[0]))
        else:
            city_num.append(0)
    print(city_num)
    #nums = re.findall(r'本溪市\d+', info_txt)#从文字中提取所有数字 前提是他们发的文章文体不变
    #print(nums)
    return city_num

def writeEnd():#在末尾追加原文
    f = open("liaoning.html", 'a')
    ultstr = "<p><font size = \"5\">" + info_txt + "</font></p>" + "数据来源：辽宁省卫健委 <a href = http://wsjk.ln.gov.cn/wst_wsjskx/>http://wsjk.ln.gov.cn/wst_wsjskx/</a>"
    lab213 = "<p>网站归属于:<a href = http://lab213.cn/>http://Lab213.cn/</a></p>"
    f.write(ultstr)
    f.write(lab213)