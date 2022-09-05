import datetime
import json
import re
import threading

import requests


def seckill(date, time, bianhao, dizhi, manname, manhao, phone, wumanname, wumanhao, phone2, colour, date_time):
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
            "csrqnan": "1995-10-25",
            "csrqnv": "1994-08-29",
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
        'x-tif-did': 'e6be642f-6d31-8aae-9871-352603d137fe',
        'x-yss-page': 'hunyin/pages/marriage_step3_booktime/marriage_step3_booktime',
        'x-yss-city-code': '4400',
        'x-tif-sid': 'cfd897b4a66be3b187d3b96b07b9da6984',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk '
                      'MiniProgramEnv/Mac',
        'Referer': 'https://servicewechat.com/wx82d43fee89cdc7df/754/page-frame.html',
        'Connection': 'keep-alive',
        'x-ysshint': 'e6be642f-6d31-8aae-9871-352603d137fe1660702016256',
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
    print('\033'f'[0:{colour}m', date_time, response.text, '\033[m')  # 31-37
    return txt


# sj=datetime.datetime.strptime(shijian,'%Y-%m-%d')转时间的写法


def run():
    jishiqi = threading.Timer(1, run)
    jishiqi.start()
    time = datetime.datetime.now()  # 当前时间
    shijisj = str(time + datetime.timedelta(days=15))
    mubiaosj = shijisj.split(' ')[0] + ' 08:29:59'
    print('系统时间是：' + str(time))
    print('约号时间是：' + str(mubiaosj))
    if shijisj >= mubiaosj:
        jishiqi.cancel()
        print('时机已到')
        data = seckill('2022-09-21', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
                       '黄林波', '44528119960111211X', '13418542421',
                       '蔡佳敏', '445222199604134365', '13543270060',
                       32, shijisj)
        while True:

            if re.search('剩余号源不够', data) is None:
                print('开始放号啦！加油冲')
                break
            else:
                print('不能秒，重来')
                data = seckill('2022-09-21', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
                               '黄林波', '44528119960111211X', '13418542421',
                               '蔡佳敏', '445222199604134365', '13543270060',
                               32, shijisj)
        seckill('2022-09-21', '9:00-10:00', '440305', '深圳市南山区民政局婚姻登记处',
                '廖梓豪', '440301199710165690', '13726270771',
                '丁铭', '500105199711280624', '18822824015',
                34, shijisj)
        seckill('2022-09-21', '10:00-11:00', '440304', '深圳市福田区民政局婚姻登记处',
                '胡杨', '420203198908182559', '15807141544',
                '刘黎玲', '420203198911023727', '13530110208',
                35, shijisj)
        seckill('2022-09-21', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
                '曹杰', '430723199609090012', '18574840949',
                '孙瑞鑫', '430722199805012680', '18165708009',
                36, shijisj)

        input('输入任意字符退出程序')

    return


if __name__ == '__main__':
    run()
