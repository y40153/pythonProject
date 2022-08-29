import json
import os
import re
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
import random
import ddddocr
import requests
from PIL import Image


def sendmail(name):
    my_sender = '401534863@qq.com'  # 发件人邮箱账号
    my_pass = 'dsjkwumnsdlybiad'  # 发件人邮箱密码
    my_user = '15279101998@139.com'  # 收件人邮箱账号，我这边发送给自己

    def mail():
        ret = True
        try:
            msg = MIMEText(name, 'plain', 'utf-8')
            msg['From'] = formataddr(("FromRunoob", my_sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(("FK", my_user))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = f"{name[-5:]}有号啦"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
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
    im.seek(1)
    im.save(str(1) + '.png')  # 将png图片保存
    im.seek(2)
    im.save(str(2) + '.png')  # 将png图片保存
    im.seek(3)
    im.save(str(3) + '.png')  # 将png图片保存
    zhi = f"{recognize('3.png')[0]}{recognize('2.png')[1:2]}{recognize('3.png')[1:2]}{recognize('0.png')[-1]}"
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


def queryz(shijian):
    if os.name == 'posix':
        with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    else:
        with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()

    url = f'https://www.gdhy.gov.cn/common.do?do=getWdrqxx&yyrq={shijian}&blcs=440300000000&ywlx=J'

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': f'{cookie}',
        'Host': 'www.gdhy.gov.cn',
        'Referer': 'https://www.gdhy.gov.cn/common.do?do=getWdrqxx&yyrq=2022-08-31&blcs=440300000000&ywlx=J',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    # if re.search('会话超时，请重新申请！', response.text) == None:
    #     print('正常跳转查询成功')
    #     data = json.loads(response.text)  # 解读出接口返回的数据
    #     global panduan, name
    #     for c, b in enumerate(data):
    #         if c == 'data':
    #             data = b  # 找到数据里面想要的data
    #     for d in data:
    #
    #         print(d)  # 打印出想要的数据
    #
    #         if d['syl'] > 0:  # 秒杀准备，有号判断
    #             print('\033''[0:35m'  f'快看啊{d["yyrq"]}，{d["yysj"]}这里有 {d["syl"]} 个号啦:[{weizhi}]'  '\033[m')
    #             panduan = True
    #             name = f'快看啊{d["yyrq"]}，{d["yysj"]}这里有 {d["syl"]} 个号啦:[{weizhi}]'
    #
    #         else:
    #             panduan = False
    #             print(data)
    # else:
    #     print('登录过期')
    #     denlu()
    return


def query(shijian, bianhao, weizhi):
    url = "https://www.gdhy.gov.cn/common.do?do=getYysjxx"

    if os.name == 'posix':
        with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    else:
        with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    payload = f'djjgbm={bianhao}0A1000&ywlx=J&rqDate={shijian}&ydbllx=01'
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

    response = requests.request("POST", url, headers=headers, data=payload)

    if re.search('会话超时，请重新申请！', response.text) == None:
        print('正常跳转查询成功')
        data = json.loads(response.text)  # 解读出接口返回的数据
        global panduan, name
        for c, b in enumerate(data):
            if c == 'data':
                data = b  # 找到数据里面想要的data
        for d in data:

            print(d)  # 打印出想要的数据

            if d['syl'] > 0:  # 秒杀准备，有号判断
                print('\033''[0:35m'  f'快看啊{d["yyrq"]}，{d["yysj"]}这里有 {d["syl"]} 个号啦:[{weizhi}]'  '\033[m')
                panduan = True
                name = f'快看啊{d["yyrq"]}，{d["yysj"]}这里有 {d["syl"]} 个号啦:[{weizhi}]'

            else:
                panduan = False
                print(data)
    else:
        print('登录过期')
        denlu()
    return panduan


def chaxun():
    global panduan
    panduan = False
    # name = ''
    dater = input("请输入预约日期如09-01:\n")
    date = f'2022-{dater}'
    print(date)
    dz = input('请输入预约区域如4:')
    while True:
        key=query(date, f'44030{dz}', '福田区')

        if key > 0:
            print('发邮件哦', name)
            # sendmail(name)
            mins = 300
        else:
            print('没有号，发不了')
            mins = 60
        time.sleep(mins)


def quxiao(nan, nv, yyrq):
    if os.name == 'posix':
        with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    else:
        with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    url = "https://www.gdhy.gov.cn/common.do?do=getYyInfos"

    payload = f'sfzjhmnan={nan}&sfzjhmnv={nv}&yyh=&yyrq={yyrq}&captcha={yzm(2)}&flag=2'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{cookie}'
    }
    try:  # 改下面切记报错会循环
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)#出问题再打印
        if re.search('name="id_box" value=', response.text) is not None:
            print('没有异常，登录成功')
            r = re.search('<input type="checkbox" name="id_box" value="(.*)"/>', response.text)
            e = re.search('<input type="hidden" name="yyrqid" value="(.*)"/>', response.text)
            a = r.group(1) + str(':1:') + e.group(1)
            print(a)
            xq = re.findall('<td align="center" class="EOS_table_oddrow" >(.*)</td>', response.text)
            print(xq)
            que = input("你确定要取消吗y/n")
            if que == 'y':
                url = 'https://www.gdhy.gov.cn/common.do?do=revokeYyInfos'
                payload = f'ids={a}'
                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
        elif re.search('没有符合条件的记录', response.text) is not None:
            print('这天没有约号')

        else:
            print('验证码错了？没有数据')
            quxiao(nan, nv, yyrq)
    except:
        print("程序出错！检查一下不然会循环，主要防验证码大写错误")
        quxiao(nan, nv, yyrq)


def miaosha():
    url1 = "https://www.gdhy.gov.cn/yyjh.do?do=hjFormValidate&vatow=04"
    if os.name == 'posix':
        with open('/Users/wang/Desktop/证件信息.txt', 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    else:
        with open(r"C:\Users\Administrator\Desktop\证件信息.txt", 'r', encoding='utf‐8') as a_file:
            cookie = a_file.readline().rstrip()
    payload = 'creator_id=%20&creator_name=%20&creator_orgid=%20&create_time=%20&slywlx=%20&id=%20&oper=%20&jszjhmnan=%20&jszjhmnv=%20&djnlnan=%20&djnlnv=%20&blzt=%20&blsj=%20&hidcitynan=%20&hidcitynv=%20&yyywlx=1&sqrlbnan=%E5%86%85%E5%9C%B0%E5%B1%85%E6%B0%91&sqrlbnv=%E5%86%85%E5%9C%B0%E5%B1%85%E6%B0%91&gjnan=%E4%B8%AD%E5%9B%BD&gjnv=%E4%B8%AD%E5%9B%BD&area_provincenan=440000000000&area_provincenv=440000000000&area_citynan=440300000000&area_citynv=440300000000&area_countynan=440304000000&area_countynv=440304000000&area_townnan=440304002000&area_townnv=440304006000&fjdnan=%E9%87%91%E9%B8%A1&fjdnv=%E6%B7%B1%E5%9C%B3%E5%B8%82&jzd_provincenan=440000000000&jzd_provincenv=440000000000&jzd_citynan=%20&jzd_citynv=%20&jzd_countynan=%20&jzd_countynv=%20&jzd_townnan=%20&jzd_townnv='
    headers = {
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '1024',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Host': 'www.gdhy.gov.cn',
        # 'Origin': 'https://www.gdhy.gov.cn',
        'Referer': 'https://www.gdhy.gov.cn/yyjh.do?do=preYyxxOper&yyrq=2022-08-30&djjg=4403040A1000&yysj=9:00-10:00&ydbllx=01',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest',
        'Cookie': f'{cookie}'
    }
    response = requests.request("POST", url1, headers=headers, data=payload)
    print(response.text, 'hjFormValidate')

    url1 = "https://www.gdhy.gov.cn/yyjh.do?do=nextOper"
    requests.request("POST", url1, headers=headers, data=payload)
    url1 = 'https://www.gdhy.gov.cn/common.do?do=getYysjxx'
    requests.request("POST", url1, headers=headers, data=payload)
    print(response.text, 'getYysjxx')
    url1 = 'https://www.gdhy.gov.cn/framework/jsp/tag/selectonedict/selectOneDictService.jsp'
    requests.request("POST", url1, headers=headers, data=payload)
    print(response.text, 'selectOneDictService')

    url3 = "https://www.gdhy.gov.cn/yyjh.do?do=formValidate"
    url6 = 'https://www.gdhy.gov.cn/common.do?do=checkSfzjhmInYyhmd'
    url4 = 'https://www.gdhy.gov.cn/yyjh.do?do=completeOper'
    url5 = 'https://www.gdhy.gov.cn/yyjh.do?do=checkSfzjh'

    def completeOper():
        # global headers
        payload = f'creator_id=%20&creator_name=%20&creator_orgid=%20&create_time=%20&slywlx=%2001&id=%20&oper=%20' \
                  f'&jszjhmnan=%20&jszjhmnv=%20&djnlnan=%20&djnlnv=%20&blzt=%20&blsj=%20&hidcitynan=%20&hidcitynv=%20' \
                  f'&yyrq=2022-08-30&yysj=9%3A00-10%3A00&djjg=4403040A1000&sqrlbnan=%E5%86%85%E5%9C%B0%E5%B1%85%E6%B0' \
                  f'%91&sqrlbnv=%E5%86%85%E5%9C%B0%E5%B1%85%E6%B0%91&xmnan=%E5%90%B4%E6%99%93%E5%BD%AC&xmnv=%E6%BD%98' \
                  f'%E8%8E%B9%E8%8E%B9&sfzjlbnan=%E5%86%85%E5%9C%B0%E5%B1%85%E6%B0%91%E8%BA%AB%E4%BB%BD%E8%AF%81' \
                  f'&sfzjlbnv=%E5%86%85%E5%9C%B0%E5%B1%85%E6%B0%91%E8%BA%AB%E4%BB%BD%E8%AF%81&sfzjhmnan' \
                  f'=440582199309086397&sfzjhmnv=440981199610152846&csrqnan=1993-09-08&csrqnv=1996-10-15&whcdnan=%E7%A1' \
                  f'%95%E5%A3%AB%E7%A0%94%E7%A9%B6%E7%94%9F&whcdnv=%E7%A1%95%E5%A3%AB%E7%A0%94%E7%A9%B6%E7%94%9F&zynan' \
                  f'=%E5%86%9C%E3%80%81%E6%9E%97%E3%80%81%E7%89%A7%E3%80%81%E6%B8%94%E3%80%81%E6%B0%B4%E5%88%A9%E4%B8' \
                  f'%9A%E7%94%9F%E4%BA%A7%E4%BA%BA%E5%91%98&zynv=%E5%8A%9E%E4%BA%8B%E4%BA%BA%E5%91%98%E5%92%8C%E6%9C%89' \
                  f'%E5%85%B3%E4%BA%BA%E5%91%98&lxdhnan=15279101998&lxdhnv=15279101998&captcha={yzm(1)}'
        try:
            response = requests.request("POST", url3, headers=headers, data=payload)
            print(response.text, 'formValidate')
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的
            print('天呐他出现了')
            completeOper()

        print(payload)
        payload = 'flag=J&sfzjhmnan=440582199309086397&sfzjhmnv=440981199610152846'
        response = requests.request("POST", url6, headers=headers, data=payload)
        print(response.text, 'checkSfzjhmInYyhmd')
        payload = 'sfzjhmnan=440582199309086397&sfzjhmnv=440981199610152846&yyrq=2022-08-30'
        response = requests.request("POST", url5, headers=headers, data=payload)
        print(response.text, 'checkSfzjh')

        payload = 'rq=2022-08-30&sj=9%3A00-10%3A00'
        response = requests.request("POST", url4, headers=headers, data=payload)
        print(response.text, 'completeOper')
        if response.text == 'captchaCodeError':
            print("破解失败，重新尝试！！")
            completeOper()
        else:
            print("成功破解验证码，登录成功！！")

    completeOper()


if __name__ == '__main__':
    login()
    # miaosha()

    # queryz('2022-09-09')

    # chaxun()
    quxiao('440582199309086397','440981199610152846','2022-08-26')#取消
