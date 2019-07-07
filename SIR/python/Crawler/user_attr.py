import urllib.request
import json
import csv

input_file = 'D:/Projects/Pycharm/SIR/Data/55/4167944869092927/uid'
output_file = 'D:/Projects/Pycharm/SIR/Data/55/4167944869092927/uid_loc'

#设置代理IP
proxy_addr="122.241.72.191:808"
proxy_addr_1 = "113.121.255.0:808"


#定义页面打开函数
def use_proxy(url,proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


#发帖数，粉丝数，性别，关注数
def get_userInfo(id):
    judge = 1
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
    while judge == 1:
        try:
            data = use_proxy(url,proxy_addr)
            judge = 0
        except Exception as e:
            print(1)
    try:
        content = json.loads(data)
    except Exception as e:
        print(2)
        filewriter = [id, e]
        return filewriter
    statuses_count = content.get('data').get('userInfo').get('statuses_count')
    fensi = content.get('data').get('userInfo').get('followers_count')
    gender = content.get('data').get('userInfo').get('gender')
    guanzhu = content.get('data').get('userInfo').get('follow_count')
    #城市另外一个数据包
    # 获取微博主页的containerid，爬取城市需要,存在两种不一样的数据表
    try:
        containerid = content.get('data').get('tabsInfo').get('tabs')[0].get('containerid')
    except Exception as e:
        print(3)
        filewriter = [id,e]
        return filewriter
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + str(id) + '&containerid=' + str(containerid)
    #print(containerid)
    judge = 1
    while judge == 1:
        try:
            data = use_proxy(url, proxy_addr_1)
            judge = 0
        except Exception as e:
            print(4)
    content = json.loads(data)
    #print(content)
    cards = content.get('data').get('cards')
    #print(cards)
    location = cards[0].get('card_group')[0].get('item_content')
    #print(statuses_count,fensi,gender,guanzhu,location)
    filewriter = [id, statuses_count, fensi, gender, guanzhu, location]
    return filewriter


if __name__ == '__main__':
    csvfile_r = open(input_file, "r", encoding='gbk')#输入
    read = csv.reader(csvfile_r)
    csvfile_w = open(output_file, "w", newline='')#输出
    writer = csv.writer(csvfile_w)
    fileHeader = ["UID", "发帖数", "粉丝数", "性别", "关注数", "城市"]
    writer.writerow(fileHeader)
    i = 1
    for uid in read:
        j = 0
        while j < 3:
            try:
                term = get_userInfo(uid[0])
                j = 5
            except Exception as e:
                j = j + 1
                print(e)
        if j == 3:
            term = [id]
        writer.writerow(term)
        i = i+1
        if i % 200 == 0:
            print(i)
    csvfile_r.close()
    csvfile_w.close()
