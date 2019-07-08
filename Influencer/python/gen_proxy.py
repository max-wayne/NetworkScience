# coding=utf-8
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
url = 'http://www.xicidaili.com/nn/1'
s = requests.get(url, headers=headers)
soup = BeautifulSoup(s.text, 'lxml')
ips = soup.select('#ip_list tr')
with open('../data/host', 'w') as write_f:
    for i in ips:
        try:
            ipp = i.select('td')
            ip = ipp[1].text
            host = ipp[2].text
            proxy = 'http://' + ip + ':' + host
            write_f.write('%s\t%s\n' % (ip, host))
        except Exception as e:
            print(e)
            print('Failed')
