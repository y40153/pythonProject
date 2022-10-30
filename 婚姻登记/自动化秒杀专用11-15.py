import datetime
import json
import re
import smtplib
import threading
from email.mime.text import MIMEText
from email.utils import formataddr

import requests


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
            "fjdnan": "隐藏显示",
            "fjdnv": "隐藏显示",
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
        'x-ysshint': '462eacb0-4062-df5d-b2a7-6603e7d9e5e81662810716134',
        'dgd-pre-release': '0',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    txt = response.text
    # if os.name == 'posix':
    #
    #     with open('/Users/wang/Desktop/证件信息.txt', mode='a', encoding='utf‐8') as a_file:
    #         a_file.write(f'\n{datetime.datetime.now()}调用了秒杀{date}的号\n{x}\n{txt}\n')
    #         # 写字
    # else:
    #     with open(r'C:\Users\Administrator\Desktop\证件信息.txt', mode='a', encoding='utf‐8') as a_file:
    #         a_file.write(f'\n{datetime.datetime.now()}调用了秒杀{date}的号\n{x}\n{txt}\n')
    #         # 写字
    print('\033'f'[0:{colour}m', response.text, '\033[m')  # 31-37
    return txt


def seckill2(date, time, bianhao, dizhi, manname, manhao, phone, wumanname, wumanhao, phone2, colour):
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
            "sqrlbnv": "香港",
            "sfzjlbnan": "内地居民身份证",
            "sfzjlbnv": "香港居民身份证",
            "sfzjhmnan": f"{manhao}",
            "sfzjhmnv": f"{wumanhao}",
            "jrzjlbnan": "",
            "jrzjlbnv": "",
            "xmnan": f"{manname}",
            "xmnv": f"{wumanname}",
            "csrqnan": f'{manhao[6:10]}-{manhao[10:12]}-{manhao[12:14]}',
            "csrqnv": '',
            "gjnan": "中国",
            "gjnv": "中国",
            "mznan": "",
            "mznv": "",
            "zynan": "专业技术人员",
            "zynv": "国家机关，党群组织，企事业单位",
            "whcdnan": "博士研究生",
            "whcdnv": "硕士研究生",
            "fjdnan": "深圳龙岗区平湖街道白泥坑社区",
            "fjdnv": "香港",
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
            "area_provincenv": "",
            "area_citynan": "440300000000",
            "area_citynv": "",
            "area_countynan": f"{bianhao}000000",
            "area_countynv": "",
            "area_townnan": f"{bianhao}001000",
            "area_townnv": "",
            "area_communitynan": "",
            "area_communitynv": "",
            "ydbllx": "04",
            "jzd_provincenan": "440000000000",
            "jzd_provincenv": "",
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


# sj=datetime.datetime.strptime(shijian,'%Y-%m-%d')转时间的写法
def sendmail(name):
    my_sender = '401534863@qq.com'  # 发件人邮箱账号
    my_pass = 'dvymozvmmvbmcaff'  # 发件人邮箱密码

    def mail(my_user='15279101998@139.com'):
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
            # r = re.search('550', e)
            # if r is not None:
            #     my_user = '401534863@qq.com'  # 收件人邮箱账号，我这边发送给自己
            #     mail(my_user)
            ret = False
        return ret

    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")


def run():
    global s, yyrq

    time = datetime.datetime.now()  # 当前时间
    shijisj = str(time + datetime.timedelta(days=15))
    yjsj = f'2022-{yyrq}' + ' 08:00:00'  # 预警时间
    mubiaosj = f'2022-{yyrq}' + ' 08:29:59'  # 秒杀时间
    print('-' * 30)
    print('系统时间是：' + str(time))
    print('约号时间是：' + str(mubiaosj))
    print('预警时间是：' + str(yjsj))

    if shijisj >= yjsj:
        name = '激动时刻马上到来', shijisj, s
        if not s == 1:
            sendmail(name)
        s = 1
        print(name)
    else:
        print('时机尚未成熟', shijisj, s)
    jishiqi = threading.Timer(s, run)
    jishiqi.start()
    if shijisj >= mubiaosj:
        jishiqi.cancel()
        print('时机已到')
        data = seckill('2022-11-15', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                       '石灵波', '433122199705278019', '18274860848',
                       '谭梅', '433122199510227545', '17307487112',
                       34)
        while True:

            if re.search('剩余号源不够', data) is None:
                print('开始放号啦！加油冲')
                break
            else:
                print('不能秒，重来')
                data = seckill('2022-11-15', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                               '石灵波', '433122199705278019', '18274860848',
                               '谭梅', '433122199510227545', '17307487112',
                               34)
        # seckill('2022-10-24', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
        #         '黄焕彬', '440507199512230657', '15814034970',
        #         '杜奕萱', '130826200002038620', '13612868620',
        #         34)

        sendmail(data)

        input('输入任意字符退出程序')

    return


if __name__ == '__main__':
    yyrq = input('请设置约号日期如09-09')  # 小心跨年
    s = 1800
    run()
