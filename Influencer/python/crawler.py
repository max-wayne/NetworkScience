# coding=utf-8
# -------Create at 2018/07/30 by Wayne-----------
import urllib.request
import json
import csv
import datetime
import random

proxy_path = '../data/host'
proxy = []

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]


# 设置代理IP
def load_proxy(path):
    with open(path, 'r') as read_f:
        for row in read_f:
            row = row.strip('\n').split('\t')
            s = row[0] + ':' + row[1]
            proxy.append(s)


# 定义页面打开函数
def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    # req.add_header("User-Agent", random.choice(my_headers))
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


# 发帖数，粉丝数，性别，关注数
def get_userInfo(s):
    id = s[0]
    uid = s[1]
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + uid
    data = use_proxy(url, random.choice(proxy))
    content = json.loads(data)
    msg = content.get('msg')
    if msg == '这里还没有内容':
        time = "none"
        guanzhu = "none"
        fensi = "none"
        filewriter = [id, uid, time, guanzhu, fensi]
        return filewriter
    fensi = content.get('data').get('userInfo').get('followers_count')
    guanzhu = content.get('data').get('userInfo').get('follow_count')
    statuses_count = content.get('data').get('userInfo').get('statuses_count')
    verified = content.get('data').get('userInfo').get('verified')
    gender = content.get('data').get('userInfo').get('gender')
    urank = content.get('data').get('userInfo').get('urank')
    mbrank = content.get('data').get('userInfo').get('mbrank')
    # 时间另外一个数据包
    # 获取微博主页的containerid，爬取城市需要,存在两种不一样的数据表
    containerid_loc = content.get('data').get('tabsInfo').get('tabs')[0].get('containerid')
    url_loc = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + uid + '&containerid=' + containerid_loc
    data_loc = use_proxy(url_loc, random.choice(proxy))
    content_loc = json.loads(data_loc)
    cards_loc = content_loc.get('data').get('cards')
    location = cards_loc[0].get('card_group')[0].get('item_content')
    containerid = content.get('data').get('tabsInfo').get('tabs')[1].get('containerid')
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + uid + '&containerid=' + containerid
    data = use_proxy(url, random.choice(proxy))
    content = json.loads(data)
    msg = content.get('msg')
    if msg == '这里还没有内容':
        time = "none"
        filewriter = [id, uid, time, guanzhu, fensi, statuses_count, verified, gender, urank, mbrank, location]
        return filewriter
    cards = content.get('data').get('cards')
    time = cards[0].get('mblog').get('created_at')
    filewriter = [id, uid, time, guanzhu, fensi, statuses_count, verified, gender, urank, mbrank, location]
    return filewriter


if __name__ == '__main__':
    load_proxy(proxy_path)
    m = 940001
    n = 960000
    print('m=', m)
    print('n=', n)
    start_time = datetime.datetime.now()
    interval = 10000
    with open('../data/user_check', 'r') as read_f:
        i = 0
        LIST = []
        for row in read_f:
            i += 1
            if i in range(m, n+1):
                if i % 1000 == 0:
                    print('i=', i)
                row = row.strip('\n')
                row = row.split('\t')
                j = 0
                while j < 5:
                    try:
                        term = get_userInfo(row)
                        break
                    except Exception as e:
                        j = j+1
                        print(e)
                        t = e
                if j == 5:
                    term = [row[0], row[1], t]
                LIST.append(term)
            elif i > n:
                break
    path = '../data/user_tmp/' + str(int(i/interval))
    csvfile_w = open(path, 'w', encoding='utf-8', newline='')
    writer = csv.writer(csvfile_w)
    fileHeader = ['id', 'uid', 'time', 'fos', 'fas', 'statuses_count', 'verified', 'gender', 'urank', 'mbrank', 'location']
    writer.writerow(fileHeader)
    for item in LIST:
        writer.writerow(item)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

