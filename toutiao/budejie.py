import requests
import re, json
import sys, os, time
from bs4 import BeautifulSoup
from multiprocessing import Pool
sys.path.append(os.path.join(os.getcwd(), 'sys-http'))
sys.path.append(os.path.join(os.getcwd(), 'sys-logge'))
from httpget import Webrequests
from mylog import MyLog
http = Webrequests()


def get_page(offset):
    payload = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from': 'gallery',
    }
    url = 'http://www.budejie.com/pic/' + str(offset)
    html = http.get_resp(url)
    Soup = BeautifulSoup(html.text, 'lxml')
    img_hashs = Soup.select('div.j-r-list-c-desc')
    for i in img_hashs:
        #i.get_text()
        print(i.get_text())
        write_to_file(i.get_text())


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(content)
        f.close()
        pass


if __name__ == '__main__':
    get_page(2)
    # main(20)