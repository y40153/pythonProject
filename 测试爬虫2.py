import base64
import json
import os
import re
import requests
from lxml import etree
from io import BytesIO


def login():
    url = 'http://10.0.1.20:8092/admin/home/login?password=ycwjz123&account=ycwjz123'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    req = requests.request("POST", url, headers=headers).json()
    token = req['data']['token']
    print('登录成功获取token：' + token)
    return token
    # aa = requests.utils.dict_from_cookiejar(req.cookies)  # 获取该请求的cookie
    # values = aa['JSESSIONID']
    # print(values)


def aixx(name, path, x):
    with open(f'{path}', mode=x) as a_file:
        a_file.write(name)
            # 写字

def updata(path):
    pathxf = path.split(".")
    url = 'http://10.0.1.20:8092/admin/media/add'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID=dccaed00-655f-48c4-8697-bc78c0cd9e09'
    }
    payload = json.dumps(
        {"entity": {"name": f"{pathxf[0]}"}})
    req = requests.request("POST", url, headers=headers, data=payload).json()
    id = req['data']['id']
    url = f"http://10.0.1.20:8092/admin/media/upload?id={id}"
    payload = {}
    files = {
        'file': (f'{path}', open(f'./{path}', 'rb'), f'image/{pathxf[1]}')
    }

    headers = {
        'Cookie': f'language=0; JSESSIONID=dccaed00-655f-48c4-8697-bc78c0cd9e09'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files).json()
    print(response)
    return response['data']['url']
def query(name):
    name = name.replace('+', '%2B')

    url = f'http://10.0.1.20:8092/admin/media/list?pageNum=1&pageSize=50&name={name}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID=dccaed00-655f-48c4-8697-bc78c0cd9e09'
    }

    req = requests.request("POST", url, headers=headers).json()
    print('正在检索服务器库存素材')
    try:
        a=req['data']['list']['content'][0]['entity']['ossUrl']
    except:
        print('数据库未录入，重新上传')
        a=1
    return a
def write(bt, zw, id, logo):
    url = 'http://10.0.1.20:8092/admin/article/modify?domain=szfc'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID=dccaed00-655f-48c4-8697-bc78c0cd9e09'
    }
    payload = json.dumps(
        {"entity": {"id": f"{id}", "name": f"{bt}",
                    "logo": f"{logo}",
                    "description": f"{zw}",
                    "showTime": "2022-09-13 18:34:11"}, "clientTypes": [{"id": 0, "name": "用户版H5端"}],
         "type": {"id": 20}, "game": {}, "league": {}})
    req = requests.request("POST", url, headers=headers, data=payload).text

    # print(payload)

    print(req)


def pawx():
    # url = ('https://mp.weixin.qq.com/s/4tvsaD25I72kgpP4-ucIjQ')

    url = ('https://mp.weixin.qq.com/s/SIpP_3GBjP8G7SOJrZmSHQ')
    # url = ('https://mp.weixin.qq.com/s/WmmCCnVx_K3xQ-RK8kl7dg')
    # url = ('https://mp.weixin.qq.com/s/M300ML2nwwnfpOiKZphyZQ')
    # url = input('请输入您要爬取的公众号文章网页地址：\n')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    req = requests.get(url=url, headers=headers)
    content = req.content.decode('utf-8')
    # print(content)

    get = etree.HTML(content)
    text = get.xpath('//*[@id="activity-name"]/text()')[0].strip()
    print('标题是：', text)
    # 爬取微信原装富文本样式
    ts = get.xpath('//*[@id="js_content"]/@style')[0]
    try:
        r = re.search(f'{ts}">(.*?)</div>', content)
        ts = r.group(1)
    except:
        r = re.search(f'{ts}">(.*?)\n', content)
        r2 = re.search(f'{r.group(0)[-5:]}(.*?)</div>', content)
        ts = r.group(1) + r2.group(1)

    # 替换关键词适应mufans
    ts = ts.replace('data-src', 'img src')
    # 关键点查找富文本图片进行替换
    ls = re.findall('img src="(.*?)" data-type', ts)

    for base in ls:
        r = requests.get(base).content

        ls_f = base64.b64encode(BytesIO(r).read())  # 读取文件内容到内存，转换为base64编码
        name = str(ls_f).split('/')[3][:9]
        img= base[-5:].split('=')[1]
        img=name+'.'+img
        print(img)
        # 给她记录已经传过的图片

        try:
            with open('./人工智能AI学习数据.txt', 'r', encoding='utf‐8') as a_file:
                for aa in a_file.readlines():
                    aa=aa.rstrip()
                    if aa == img:
                        aa=aa.split('.')[0]
                        url=query(aa)
                        print('智能学习判断已存在素材，节省资源提取原有url:',url)
                        key=1
                        break
                    else:
                        key=0
            if key==0:
                aixx('\n' + img, './人工智能AI学习数据.txt', 'a')
                # 下载新图片
                aixx(r, f'./{img}', 'wb')
                # 上传新图片
                url = updata(img)
        except:
            print('出错了，没有发现存储器，立马创建。。。')
            aixx(img, './人工智能AI学习数据.txt', 'a')
            aixx(r, f'./{img}', 'wb')
            # 出错不上传新图片
            # url = updata(img)

        # 替换链接给富文本
        ts = ts.replace(f'{base}', f'{url}')

    # 爬取文章logo
    r = re.search('var cdn_url_1_1 = "(.*)"; // 1:1比例的封面图', content)
    logo = r.group(1)

    r = requests.get(logo)
    ls_f = base64.b64encode(BytesIO(r.content).read())  # 读取文件内容到内存，转换为base64编码
    base = 'data:image/png;base64,' + str(ls_f).split('\'')[1]
    write(text, ts, 32, base)


if __name__ == '__main__':
    pawx()
