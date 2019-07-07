# coding=utf-8

import urllib.request
import json
import csv
import os

# 设置代理IP
proxy_addr = "122.241.72.191:808"
proxy_addr_1 = "113.121.255.0:808"


# 定义页面打开函数
def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


# 发帖数，粉丝数，性别，关注数
def get_userInfo(uid):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + uid
    data = use_proxy(url, proxy_addr)
    content = json.loads(data)
    msg = content.get('msg')
    if msg == '这里还没有内容':
        time = "none"
        guanzhu = "none"
        fensi = "none"
        filewriter = [uid, time, guanzhu, fensi]
        return filewriter
    fensi = content.get('data').get('userInfo').get('followers_count')
    guanzhu = content.get('data').get('userInfo').get('follow_count')
    # 时间另外一个数据包
    # 获取微博主页的containerid，爬取城市需要,存在两种不一样的数据表
    containerid = content.get('data').get('tabsInfo').get('tabs')[1].get('containerid')
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + uid + '&containerid=' + containerid
    data = use_proxy(url, proxy_addr_1)
    content = json.loads(data)
    msg = content.get('msg')
    if msg == '这里还没有内容':
        time = "none"
        filewriter = [uid, time, guanzhu, fensi]
        return filewriter
    cards = content.get('data').get('cards')
    time = cards[0].get('mblog').get('created_at')
    # print(statuses_count,fensi,gender,guanzhu,location)
    filewriter = [uid, time, guanzhu, fensi]
    return filewriter


if __name__ == '__main__':
    F1 = []
    F2 = []
    for i in range(16):
        for j in range(18):
            path1 = '../data/sample_whole_graph/' + 'uid' + str((i, j))
            path2 = '../data/sample_whole_graph/' + 'uid_' + str(i) + '_' + str(j)
            F1.append(path1)
            F2.append(path2)
    for m in range(225, len(F1)):
        print(F1[m])
        print(F2[m])
    #     F1 = './data/sample/uid(13, 13)'
    #     F2 = './data/sample/uid_13_13'
        if os.path.getsize(F1[m]):
            csvfile_r = open(F1[m], 'r', encoding='gbk')
            read = csv.reader(csvfile_r)
            csvfile_w = open(F2[m], 'w', newline='')
            writer = csv.writer(csvfile_w)
            # fileHeader = ['number', 'uid', 'time', '关注', '粉丝']
            # writer.writerow(fileHeader)
            i = 1
            t = 0
            for uid in read:
                uid = str(uid[0]).split('\t')
                print(uid)
                j = 0
                while j < 5:
                    try:
                        # term = get_userInfo(id[0], id[1])
                        term = get_userInfo(uid[0])
                        j = 10
                    except Exception as e:
                        j = j+1
                        print(e)
                        t = e
                if j == 5:
                    # term = [id[0], id[1], t]
                    term = [uid[0], t]
                writer.writerow(term)
                i = i+1
                if i % 200 == 0:
                    print(i)
            csvfile_r.close()
            csvfile_w.close()

