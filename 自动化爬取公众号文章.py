import base64
import json
import os
import re
import requests
from lxml import etree
from io import BytesIO


def xuanzhe(list, names):
    key = 0
    for org in list:
        name = org[names]
        key += 1
        print('——'*30)
        print(f'序号【{key}】:{name}')
    return


def login():
    url = 'https://mufans.tech/admin/home/login?password=ycwjz123&account=ycwjz123'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    req = requests.request("POST", url, headers=headers).json()
    global token
    token = req['data']['token']
    print('——' * 30)
    print('登录mufans运营端成功获取token：' + token)
    orgs = req['data']['orgs']
    xuanzhe(orgs, 'clientTitle')
    key = int(input('请输入您需要登录的客户序号:'))
    url = f'https://mufans.tech/admin/home/choose?orgId={orgs[key - 1]["orgId"]}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID={token}'
    }
    response = requests.request("POST", url, headers=headers).text
    print('——' * 30)
    print(f'登录{orgs[key - 1]["clientTitle"]}\n', response)
    return token


def aixx(name, path, x):
    with open(f'{path}', mode=x) as a_file:
        a_file.write(name)
        # 写字


def updata(path):
    pathxf = path.split(".")
    url = 'https://mufans.tech/admin/media/add'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID={token}'
    }
    payload = json.dumps(
        {"entity": {"name": f"{pathxf[0]}"}})
    req = requests.request("POST", url, headers=headers, data=payload).json()
    id = req['data']['id']
    url = f"https://mufans.tech/admin/media/upload?id={id}"
    payload = {}
    files = {
        'file': (f'{path}', open(f'./{path}', 'rb'), f'image/{pathxf[1]}')
    }

    headers = {
        'Cookie': f'language=0; JSESSIONID={token}'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files).json()
    print(response)
    return response['data']['url']


def query(name):

    url = f'https://mufans.tech/admin/media/list?pageNum=1&pageSize=50&name={name}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID={token}'
    }

    req = requests.request("POST", url, headers=headers).json()
    print('——' * 30)
    print('正在检索服务器库存素材')
    try:
        a = req['data']['list']['content'][0]['entity']['ossUrl']
        print('智能学习判断已存在素材，节省资源提取原有url:', a)
        print('——' * 30)

    except:
        print('——' * 30)
        print('数据库未录入，重新上传')
        a = 1
    return a


def write(bt, zw, logo):
    url = 'https://mufans.tech/admin/setting/dictionary/listMine?dictType=10000'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID={token}'
    }
    response = requests.request("POST", url, headers=headers).json()
    typec = response['data']['list']
    xuanzhe(typec, 'name')
    key = int(input('请输入创建资讯所属类别的序号:'))
    url = 'https://mufans.tech/admin/article/add'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID={token}'
    }
    payload = json.dumps(
        {"entity": {"name": f"{bt}",
                    "logo": f"{logo}",
                    "description": f"{zw}"}, "clientTypes": [{"id": 0, "name": "用户版H5端"}],
         "type": {"id": typec[key - 1]['id']}, "game": {}, "league": {}})
    req = requests.request("POST", url, headers=headers, data=payload).text

    # print(payload)

    print(req)


def pawx():
    # url = ('https://mp.weixin.qq.com/s/4tvsaD25I72kgpP4-ucIjQ')
    # url = ('https://mp.weixin.qq.com/s/SIpP_3GBjP8G7SOJrZmSHQ')
    # url = ('https://mp.weixin.qq.com/s/WmmCCnVx_K3xQ-RK8kl7dg')
    # url = ('https://mp.weixin.qq.com/s/M300ML2nwwnfpOiKZphyZQ')
    url = input('请输入您要爬取的公众号文章网页地址：\n')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    req = requests.get(url=url, headers=headers)
    content = req.content.decode('utf-8')
    # print(content)

    get = etree.HTML(content)
    text = get.xpath('//*[@id="activity-name"]/text()')[0].strip()
    print('——' * 30)
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
    # ls = re.findall('img src="(.*?)" data-type', ts)
    ls = re.findall('img src="(.*?)"', ts)

    for base in ls:
        r = requests.get(base).content

        ls_f = base64.b64encode(BytesIO(r).read())  # 读取文件内容到内存，转换为base64编码
        name = str(ls_f).split('/')[-5][-13:].replace('+', '')
        img = base.split('=')[1].split('&')[0]
        img = name + '.' + img
        print('——' * 30)
        print(img)
        # 查询已经传过的图片
        url = query(name)
        if url == 1:
            print('全新图片爬取上传至素材库中。。。')
            # 下载新图片
            aixx(r, f'./{img}', 'wb')
            # 上传新图片
            url = updata(img)
            print('上传成功，获得url=', url)

        # 替换链接给富文本
        ts = ts.replace(f'{base}', f'{url}')

    # 爬取文章logo
    r = re.search('var cdn_url_1_1 = "(.*)"; // 1:1比例的封面图', content)
    logo = r.group(1)

    r = requests.get(logo)
    ls_f = base64.b64encode(BytesIO(r.content).read())  # 读取文件内容到内存，转换为base64编码
    base = 'data:image/png;base64,' + str(ls_f).split('\'')[1]
    write(text, ts, base)
    print('爬取资讯已经结束，可以关闭程序，或者继续爬取')
    print('——' * 30)
    pawx()


if __name__ == '__main__':
    login()
    pawx()
