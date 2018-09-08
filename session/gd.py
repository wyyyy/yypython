import requests
import re
from time import sleep
with requests.session() as s:
    login_url = "https://cas.gzhu.edu.cn/cas_server/login"
    #login_url = "https://119.97.194.18:4503/Default.aspx"
    wzh=requests.get(login_url.strip())
    first = s.get(login_url.strip())
    lt = re.findall(r'name="lt" value="(.*?)"', first.text)
    print(lt[0])
    cookie = first.headers["Set-Cookie"]
    # print cookie
    Js = re.findall(r"(JSESSIONID=.*?);", cookie)
    print(Js[0])
    s.headers = {
        # "Host": "cas.gzhu.edu.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://cas.gzhu.edu.cn/cas_server/login?service=https://cas.gzhu.edu.cn:443/shunt/index.jsp",
        "Cookie": Js[0],
        "Connection": "keep-alive"
    }
    Data = {
        "username": "",
        "password": "",
        "captcha": "",
        "warn": "true",
        "lt": lt,
        "execution": "e1s1",
        "_eventId": "submit",
    }

    # 登陆
    new = s.post(login_url, data=Data)
    print(new.url)
