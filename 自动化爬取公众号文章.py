import base64
import json
import re
import time

import requests
from lxml import etree
from io import BytesIO


def xuanzhe(list, names):
    key = 0
    for org in list:
        name = org[names]
        key += 1
        print('——' * 30)
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
    key = pancuo('请输入您需要登录的客户序号:')
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


def pancuo(inputs):
    while True:
        try:
            a = int(input(inputs))
            break
        except:
            # a=int(input('请输入正确的格式，重新输入：'))
            print('请输入正确的格式，重新输入')
    return a


def write(bt, zw, logo,date):
    print('——' * 30)

    id = pancuo('资源爬取完成，请问您是要新增资讯还是要编辑，新增请输入0，编辑请输入资讯id:')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=utf8',
        'Cookie': f'language=0; JSESSIONID={token}'
    }

    print('——' * 30)

    url = 'https://mufans.tech/admin/setting/dictionary/listMine?dictType=10000'

    response = requests.request("POST", url, headers=headers).json()
    typec = response['data']['list']
    xuanzhe(typec, 'name')
    if id == 0:
        key = pancuo('请输入创建资讯所属类别的序号:')
        url = 'https://mufans.tech/admin/article/add'
        payload = json.dumps(
            {"entity": {"name": f"{bt}",
                        "logo": f"{logo}",
                        "description": f"{zw}","showTime":f"{date}"}, "clientTypes": [{"id": 0, "name": "用户版H5端"}],
             "type": {"id": typec[key - 1]['id']}, "game": {}, "league": {}})
    else:
        url = f'https://mufans.tech/admin/article/query?id={id}'
        response = requests.request("POST", url, headers=headers).json()
        print('——' * 30)
        print('——' * 30)
        print('请确认编辑的资讯：', response['data']['query']['entity']['name'])
        print('——' * 30)
        key = pancuo('（可输入0取消编辑）请输入编辑资讯所属类别的序号:')
        if key == 0:
            write(bt, zw, logo)
        else:
            url = f'https://mufans.tech/admin/article/changeStatus?id={id}&status=3'
            data = json.dumps(
                [])
            response = requests.request("POST", url, headers=headers, data=data).text
            print('下架成功，开始编辑', response)
            url = 'https://mufans.tech/admin/article/modify'
            payload = json.dumps(
                {"entity": {"id": f"{id}", "name": f"{bt}",
                            "logo": f"{logo}",
                            "description": f"{zw}","showTime":f"{date}"}, "clientTypes": [{"id": 0, "name": "用户版H5端"}],
                 "type": {"id": typec[key - 1]['id']}, "game": {}, "league": {}})

    req = requests.request("POST", url, headers=headers, data=payload).text

    # print(payload)

    print('编辑完成', req)


def pawx():

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
    # 找时间
    r = re.search('\{e\(0,"(.*)\("publish_time"\)', content)
    date = r.group(1).split('\"')[0]
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(date)))
    print('抓到显示时间',date)
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
    ls = re.findall('img src="(.*?)"', ts)

    for base in ls:
        # 获取链接后缀名,判断异常格式不进行处理
        img = base.split('=')[1].split('&')[0]
        if len(img) > 5:
            print('【检测到有异常格式，如视频格式，需要运营自行解决，目前版本暂时跳过处理】：',img)
            continue
        # 删除样式控制
        qie = base.split('?')
        r = re.search(f'{qie[0]}(.*?)>', ts)
        print('自动适应mufans富文本，删除微信样式\n' + r.group(1))
        ts = ts.replace(f'{r.group(1)}', f'?{qie[1]}"')
        # 图片处理
        r = requests.get(base).content
        ls_f = base64.b64encode(BytesIO(r).read())  # 读取文件内容到内存，转换为base64编码
        name = str(ls_f).split('/')[-5][-13:].replace('+', '')
        img = name + '.' + img
        print('——' * 30)
        print(img)
        # 查询已经传过的图片
        url = query(name)
        if url == 1:
            print('全新图片爬取上传至素材库中。。。')
            # 下载新图片
            try:
                aixx(r, f'./{img}', 'wb')
            except:
                print('【检测到有异常格式，如视频格式，需要运营自行解决，目前版本暂时跳过处理】')
                continue
            # 上传新图片
            url = updata(img)
            print('上传成功，获得url=', url)

        # 替换链接给富文本
        ts = ts.replace(f'{base}', f'{url}')

    # 爬取文章logo
    r = re.search('var msg_cdn_url = "(.*)"; // 首图idx=0时2.35:1', content)
    logo = r.group(1)

    r = requests.get(logo)
    ls_f = base64.b64encode(BytesIO(r.content).read())  # 读取文件内容到内存，转换为base64编码
    base = 'data:image/png;base64,' + str(ls_f).split('\'')[1]
    write(text, ts, base,date)
    print('爬取资讯已经结束，可以关闭程序，或者继续爬取')
    print('——' * 30)
    pawx()


if __name__ == '__main__':
    login()
    pawx()
