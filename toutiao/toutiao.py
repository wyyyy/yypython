import requests
import re, json
import sys, os, time
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
    url = 'https://www.toutiao.com/search_content/?'
    html = http.get_resp(url, para=payload)
    j = json.loads(json.dumps(html.json()))
    #print(j)
    print(j['count'])
    datas = j['data']
    for item in datas:
        yield {
            'title': item.get('title'),
            'gallery_pic_count': item.get('gallery_pic_count'),
            'large_image_url': item.get('large_image_url')
        }
        pass
    # "gallery_pic_count":4,
    # "large_image_url":"http://p3.pstatp.com/large/pgc-image/15304510603559bc49581f1",
    # /#p=2
    write_to_file(html.json())
    return html.json()


def get_imgs_url(items):
    imgs_info = []
    for itme in items:
        title, gallery_pic_count, large_image_url = itme
        imgs_single = []
        for i in range(len(gallery_pic_count)):
            imgs_single.append(large_image_url + '/#p=' + str(i+1))
        imgs_info.append((imgs_single))
        # imgs_info.append((title, imgs_single))
    yield imgs_info


def display_imgs_url(imgs_infos):
    for item in imgs_infos:
        print(item)
        pass
    print('all url')


def write_to_file(content):
    with open('result12.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()
        pass


if __name__ == '__main__':
    display_imgs_url(get_imgs_url((get_page(20))))
    # main(20)