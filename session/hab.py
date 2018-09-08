import requests
import re
import os
import time

from time import sleep
with requests.session() as s:
    #login_url = "https://cas.gzhu.edu.cn/cas_server/login"
    login_url = "http://119.97.194.18:4503/Default.aspx"
    userAgent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    s.headers = {
        'User-Agent': userAgent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Host": "119.97.194.18:4503",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip, deflate"
    }
    first = s.get(login_url.strip())
    #first = 's.get(login_url.strip())'
    __VIEWSTATE = re.findall(r'id="__VIEWSTATE" value="(.*?)"', first.text)
    __EVENTVALIDATION = re.findall(
        r'id="__EVENTVALIDATION" value="(.*?)"', first.text)
    cookie = first.headers["Set-Cookie"]
    # print cookie
    Js = re.findall(r"(ASP.NET_SessionId=.*?);", cookie)
    print(Js[0])
    # get code
    code_url = 'http://119.97.194.18:4503/ImageCode.aspx'
    s.headers = {
        # "Host": "cas.gzhu.edu.cn",
        "User-Agent": userAgent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": login_url,
        "Cookie": Js[0],
        "Connection": "keep-alive"
    }
    code = s.get(code_url.strip())
    img_content = code.content
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))+'.jpg'
    dir_path = os.path.dirname(os.path.curdir + '/jiandan/')
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    try:
        with open(os.path.join(dir_path, rq), 'wb') as f:
            f.write(img_content)
    except Exception as e:
        print(e)

    code = input('pls input the code-image:')
    s.headers = {
        "User-Agent": userAgent,
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": login_url,
        "Cookie": Js[0],
        "Connection": "keep-alive"
    }
    Data = {
        "txtUserName": "111",
        "txtPassWord": "222",
        "__VIEWSTATE": __VIEWSTATE[0],
        "__EVENTVALIDATION": __EVENTVALIDATION[0],
        "hidUserScreenWidth": 1536,
        "txtImgCode": code,
        "ibtnOK": "submit",
    }

    # 登陆
    new = s.post(login_url, data=Data)
    print(new.url)
