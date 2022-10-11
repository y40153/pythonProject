import datetime
import json
import os
import random
import re
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr

import ddddocr
import requests
from PIL import Image


def seckill(date, time, bianhao, dizhi, manname, manhao, phone, wumanname, wumanhao, phone2, colour):
    x = f'男名{manname}，男卡{manhao}，男号{phone}，女名{wumanname}，女卡{wumanhao}，女号{phone2}'
    url = "https://mmykm2.gdbs.gov.cn/ebus/huazi_gdhy/hunyin/api/mobile/marriage/create_reservation?"

    print(x)
    payload = json.dumps({
        "ywlx": "J",
        "bookDate": "",
        "bookCity": "",
        "sfzjhm": "",
        "slhzbh": "",
        "hydjEnty": {
            "id": "",
            "yyywlx": "",
            "slywlx": "",
            "sqrlbnan": "内地居民",
            "sqrlbnv": "内地居民",
            "sfzjlbnan": "内地居民身份证",
            "sfzjlbnv": "内地居民身份证",
            "sfzjhmnan": f"{manhao}",
            "sfzjhmnv": f"{wumanhao}",
            "jrzjlbnan": "",
            "jrzjlbnv": "",
            "xmnan": f"{manname}",
            "xmnv": f"{wumanname}",
            "csrqnan": f'{manhao[6:10]}-{manhao[10:12]}-{manhao[12:14]}',
            "csrqnv": f'{wumanhao[6:10]}-{wumanhao[10:12]}-{wumanhao[12:14]}',
            "gjnan": "中国",
            "gjnv": "中国",
            "mznan": "",
            "mznv": "",
            "zynan": "专业技术人员",
            "zynv": "国家机关，党群组织，企事业单位",
            "whcdnan": "博士研究生",
            "whcdnv": "硕士研究生",
            "fjdnan": "广东省深圳市福田区福田街道办事处",
            "fjdnv": "广东省深圳市福田区香蜜湖街道办事处",
            "lxdhnan": f"{phone}",
            "lxdhnv": f"{phone2}",
            "yyrq_id": "",
            "yyh": "",
            "yyrq": f"{date}",
            "yysj": f"{time}",
            "djjgbm": f"{bianhao}0A1000",
            "djjgmc": f"{dizhi}",
            "djjgdz": "深圳市福田区农园路30号香蜜公园西门。进入婚姻登记处需出示行程码、粤康码（绿码）、48小时内核酸检测阴性证明，行程码带星（*）的按照现行规定提供核酸检测阴性证明。",
            "djjgdh": "0755-82928049",
            "areacodenan": "",
            "areacodenv": "",
            "areatypenan": "",
            "areatypenv": "",
            "area_provincenan": "440000000000",
            "area_provincenv": "440000000000",
            "area_citynan": "440300000000",
            "area_citynv": "440300000000",
            "area_countynan": f"{bianhao}000000",
            "area_countynv": f"{bianhao}000000",
            "area_townnan": f"{bianhao}001000",
            "area_townnv": f"{bianhao}004000",
            "area_communitynan": "",
            "area_communitynv": "",
            "ydbllx": "01",
            "jzd_provincenan": "440000000000",
            "jzd_provincenv": "440000000000",
            "jzd_citynan": "",
            "jzd_citynv": "",
            "jzd_countynan": "",
            "jzd_countynv": ""
        },
        "hyzmEnty": None
    })
    headers = {
        'x-tif-did': '462eacb0-4062-df5d-b2a7-6603e7d9e5e8',
        'x-yss-page': 'hunyin/pages/marriage_step3_booktime/marriage_step3_booktime',
        'x-yss-city-code': '4400',
        'x-tif-sid': 'dbcf3fbd78fade94bc7b732ce4adbbb9f8',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk '
                      'MiniProgramEnv/Mac',
        'Referer': 'https://servicewechat.com/wx82d43fee89cdc7df/754/page-frame.html',
        'Connection': 'keep-alive',
        'x-ysshint': 'e6be642f-6d31-8aae-9871-352603d137fe1661747478128',
        'dgd-pre-release': '0',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    global name
    txt = response.text
    name = name + x + txt
    print('\033'f'[0:{colour}m', response.text, '\033[m')  # 31-37
    return


def sendmail(name):
    my_sender = '401534863@qq.com'  # 发件人邮箱账号
    my_pass = 'dvymozvmmvbmcaff'  # 发件人邮箱密码
    def mail(my_user = '15279101998@139.com'):
        ret = True
        try:
            msg = MIMEText(f'{name}', 'plain', 'utf-8')
            msg['From'] = formataddr(("秒杀监控系统", my_sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(("FK", my_user))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = f"{name[:5]}有号啦"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print(e)
            r = re.search('550', e)
            if r is not None:
                my_user = '401534863@qq.com'  # 收件人邮箱账号，我这边发送给自己
                mail(my_user)
            ret = False
        return ret

    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")


def recognize(name):
    ocr = ddddocr.DdddOcr()
    with open(f'./{name}', 'rb') as f:
        img_bytes = f.read()

    res = ocr.classification(img_bytes)

    return res


def yzm(cancel):
    payload = {}
    if cancel == None:  # 进行登录验证码破解
        headers = {
            'Referer': 'https://www.gdhy.gov.cn/wsyy/index.jsp'
        }
        response = requests.request("GET", "http://www.gdhy.gov.cn/common.do?do=getCaptchaImg", headers=headers,
                                    data=payload)
        aa = requests.utils.dict_from_cookiejar(response.cookies)  # 获取该请求的cookie
        values = aa['JSESSIONID']
        values2 = aa['openstack_cookie_insert']
    elif cancel == 1:
        print('秒杀来验证码')
        if os.name == 'posix':
            with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
                cookie = a_file.readline().rstrip()
        else:
            with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
                cookie = a_file.readline().rstrip()
        headers = {
            'Referer': 'https://www.gdhy.gov.cn/yyjh.do?do=preYyxxOper&yyrq=2022-08-30&djjg=4403040A1000&yysj=9:00-10:00&ydbllx=01',
            'Cookie': f'{cookie}'
        }
        url = f"https://www.gdhy.gov.cn/common.do?do=getCaptchaImg&random={random.random()}"
        print(url)
        response = requests.request("GET", url, headers=headers,
                                    data=payload)
    else:  # 进行取消
        if os.name == 'posix':
            with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
                cookie = a_file.readline().rstrip()
        else:
            with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
                cookie = a_file.readline().rstrip()
        headers = {
            'Referer': 'https://www.gdhy.gov.cn/wsyy/query/yyQuery.jsp?flag=2',
            'Cookie': f'{cookie}'
        }
        response = requests.request("GET", "https://www.gdhy.gov.cn/common.do?do=getCaptchaImg", headers=headers,
                                    data=payload)

    # text = response.content.decode('utf-8','ignore')#解决乱码
    open("./aa.gif", 'wb').write(response.content)  # 下载gif图片
    im = Image.open("./aa.gif")
    im.save(str(0) + '.png')  # 将png图片保存

    im.seek(2)
    im.save(str(2) + '.png')  # 将png图片保存
    im.seek(3)
    im.save(str(3) + '.png')  # 将png图片保存
    try:
        zhi = f"{recognize('3.png')[0]}{recognize('2.png')[1:2]}{recognize('3.png')[1:2]}{recognize('0.png')[-1]}"
    except Exception as e:
        zhi = 2341
        print(e)
        
        sendmail(f'验证码获取错误{e}')
        print('-' * 20, '【出错了】', '-' * 20)
        time.sleep(60)
    print(zhi)
    if cancel == None:

        if os.name == 'posix':

            with open('/Users/wang/Desktop/证件信息.txt', mode='w', encoding='utf‐8') as a_file:
                a_file.write(f'JSESSIONID={values};openstack_cookie_insert={values2}')
                # 写字
        else:
            with open(r'C:\Users\Administrator\Desktop\证件信息.txt', mode='w', encoding='utf‐8') as a_file:
                a_file.write(f'JSESSIONID={values};openstack_cookie_insert={values2}')
            # 写字
    return zhi


def denlu():
    payload = f'captcha={yzm(None)}'
    if os.name == 'posix':
        with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    else:
        with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    headers = {
        'Referer': 'https://www.gdhy.gov.cn/wsyy/yyjh.jsp',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{cookie}'
    }
    try:
        response = requests.request("POST", "https://www.gdhy.gov.cn/common.do?do=validateYzm", headers=headers,
                                    data=payload)
        print(response.text)
        if response.text == 'captchaCodeError':
            print("破解失败，重新尝试！！")
            denlu()
        else:
            print("成功破解验证码，登录成功！！")
            login()
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print('天呐他出现了')
        denlu()

    # captchaCodeRight


def login():
    payload = {}
    try:
        if os.name == 'posix':
            with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
                cookie = a_file.readline().rstrip()
        else:
            with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
                cookie = a_file.readline().rstrip()
    except:
        print('出错了，没有发现存储器，立马创建。。。')
        if os.name == 'posix':

            with open('/Users/wang/Desktop/证件信息.txt', mode='w', encoding='utf‐8') as a_file:
                a_file.write('')
                # 写字
        else:
            with open(r'C:\Users\Administrator\Desktop\证件信息.txt', mode='w', encoding='utf‐8') as a_file:
                a_file.write('')
                # 写字
        cookie = ''
        login()
    headers = {
        'Referer': 'https://www.gdhy.gov.cn/wsyy/yyjh.jsp',
        'Cookie': f'{cookie}'
    }
    print(headers)

    response = requests.request('GET',
                                "https://www.gdhy.gov.cn/common.do?do=getWdrqxx&yyrq=2022-09-09&blcs=440300000000&ywlx=J",
                                headers=headers, data=payload)

    if re.search('会话超时，请重新申请！', response.text) is None:
        print('没有异常，登录成功')
    else:
        print('登录过期')
        denlu()


def query(shijian, bianhao, weizhi):
    url = "https://www.gdhy.gov.cn/common.do?do=getYysjxx"
    if os.name == 'posix':
        with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    else:
        with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    payload = f'djjgbm={bianhao}0A1000&ywlx=J&rqDate={shijian}&ydbllx=01'
    print(f"正在查询{weizhi}的号：{payload}")
    headers = {
        'Host': 'www.gdhy.gov.cn',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Referer': 'https://www.gdhy.gov.cn/common.do?do=getWdrqxx&yyrq=2022-08-30&blcs=4403040A1000&ywlx=J',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '54',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': f'{cookie}'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except requests.exceptions.RequestException:
        
        sendmail('请求超时哦')
        print('-' * 20, '【出错了】', '-' * 20)
        time.sleep(60)
        response = requests.request("POST", url, headers=headers, data=payload)

    if re.search('会话超时，请重新申请！', response.text) == None:
        print('正常跳转查询成功')
        try:
            data = response.json()  # 解读出接口返回的数据
            global panduan, name
            panduan = False
            for d in data:

                print(d)  # 打印出想要的数据

                if d['syl'] > 0:  # 秒杀准备，有号判断
                    print('\033''[0:35m'  f'快看啊{d["yyrq"]}，{d["yysj"]}这里有 {d["syl"]} 个号啦:[{weizhi}]'  '\033[m')
                    panduan = True
                    name = f'[{weizhi}]{d["yyrq"]}，{d["yysj"]}这里有 {d["syl"]} 个号啦'
                    run(d["yyrq"], d["yysj"], f'{bianhao}', weizhi)
                else:
                    print('获取值为空', data)
        except:
            sendmail(f'{response.text}')
            time.sleep(60)
            pass
    else:
        print('登录过期')
        denlu()
    return panduan


def chaxun():
    dater = input("请输入预约日期如09-01:\n")
    date = f'2022-{dater}'
    print(date)
    zi = 1
    while True:
        key = query(date, '440304', '福田区')
        # key = query(date, '440396', '大鹏新区') + query(date, '440308', '盐田区') + query(date,'440307', '龙岗区') key =
        # query(date, '440305', '南山区') + query(date, '440306', '宝安区') + query(date, '440303', '罗湖区') key = query(
        # date, '440305', '南山区') + query(date, '440306', '宝安区') + query(date, '440304', '福田区')+ query(date, '440303',
        # '罗湖区')+ query(date,'440307', '龙岗区')+ query(date,'440311', '光明区')
        sj = datetime.datetime.now()  # 当前时间
        print(f'卢映敏{sj},第{zi}次轮询：有{key}个区有号')
        zi += 1
        if key > 0:
            global name
            print('发邮件哦', name)
            sendmail(name)
            mins = 300
        else:
            print('没有号，发不了')
            mins = 5
        time.sleep(mins)


def run(yyrq, shij, bianhao, diz):
    # seckill(f'{yyrq}', f'{shij}', f'{bianhao}', f'{diz}',
    #         '夏正', '421126199501101758', '13691777188',
    #         '李琳', '532128199610130346', '15764233924',
    #         32)
    # seckill(f'{yyrq}', f'{shij}', f'{bianhao}', f'{diz}',
    #         '潘卓钒', '441802199804110919', '15279101998',
    #         '黎静婷', '445381199803206021', '13168661477',
    #         32)
    # seckill(f'{yyrq}', f'{shij}', f'{bianhao}', f'{diz}',
    #         '黄凯', '441523199507176036', '15014049639',
    #         '马丽纯', '440582199501135849', '13202297256',
    #         32)
    seckill(f'{yyrq}', f'{shij}', f'{bianhao}', f'{diz}',
            '陈俊宇', '500101199212195251', '13392852295',
            '卢映敏', '441581199203163408', '13424425570',
            32)
    return


if __name__ == '__main__':
    login()
    chaxun()
