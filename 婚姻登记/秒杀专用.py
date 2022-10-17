import datetime
import json
import re
import threading

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
        data = seckill('2022-09-17', '14:00-14:30', '440304', '深圳市福田区民政局婚姻登记处',
                       '吴晓彬', '440582199309086397', '15279101998',
                       '潘莹莹', '440981199610152846', '15279101998',
                       34)
        # while True:
        #
        #     if re.search('剩余号源不够', data) is None:
        #         print('开始放号啦！加油冲')
        #         break
        #     else:
        #         print('不能秒，重来')
        #         data = seckill('2022-09-27', '10:00-11:00', '440304', '深圳市福田区民政局婚姻登记处',
        #                        '叶灿明', '441202198201154018', '15820285059',
        #                        '姚凤兰', '431022199007054280', '18818560254',
        #                        34)
        # seckill('2022-09-27', '10:00-11:00', '440304', '深圳市福田区民政局婚姻登记处',
        #         '董贺楠', '23233019930527461X', '17620311677',
        #         '严冬', '441284199410070047', '13760088888',
        #         32)
        #
        # seckill('2022-09-27', '14:00-14:30', '440304', '深圳市福田区民政局婚姻登记处',
        #         '陈凌锋', '441323199402078519', '15986763618',
        #         '陈婉玲', '44522419951214522X', '18503066997',
        #         34)

        input('输入任意字符退出程序')

    return


if __name__ == '__main__':
    run()
