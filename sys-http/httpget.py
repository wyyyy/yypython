import requests
import json
import random
from fake_useragent import UserAgent
from requests import ConnectionError
from requests.exceptions import RequestException
ua = UserAgent()


# __author__ = 'wzh'
class Webrequests(object):
    def __init__(self):
        # pc+ie
        #agent = random.choice(userAgents.UserAgent_List),
        self.userAgent = (ua.random)

    def set_para(self, para):
        self.params = para

    def set_header(self, head):
        headers = {'User-Agent': self.userAgent}
        self.paheadersrams = headers

    def get_resp(self, url, para=None, header=None):
        try:
            if header == None:
                header = {'User-Agent': self.userAgent}
            resp = requests.get(url, params=para, headers=header)
            #  r.raise_for_status()
            if resp.status_code == 200:
                return resp
            return None
        except ConnectionError:
            print('ConnectionError-Error.')
            return None

    def post_html(self, url, para, headers):
        try:
            r = requests.post(url, data=para, headers=headers)
            print("获取返回的状态码", r.status_code)
            json_r = r.json()
            print("json类型转化成python数据类型", json_r)
        except BaseException as e:
            print("请求失败！", str(e))

    def post_json(self, url, para, headers):
        try:
            data = para
            data = json.dumps(data)  #python数据类型转化为json数据类型
            r = requests.post(url, data=data, headers=headers)
            print("获取返回的状态码", r.status_code)
            json_r = r.json()
            print("json转换为python数据类型：", json_r)
        except BaseException as e:
            print("请求失败！", str(e))

    def getUserAgent(self):
        #ie浏览器的user agent
        print(ua.ie)

        #opera浏览器
        print(ua.opera)

        #chrome浏览器
        print(ua.chrome)

        #firefox浏览器
        print(ua.firefox)

        #safri浏览器
        print(ua.safari)

        #最常用的方式
        #写爬虫最实用的是可以随意变换headers，一定要有随机性。支持随机生成请求头
        print(ua.random)
        print(ua.random)
        print(ua.random)


if __name__ == '__main__':
    mylog = Webrequests()
    '''
    from mylog import MyLog
    ml=MyLog()
    ml.debug('')
    '''
