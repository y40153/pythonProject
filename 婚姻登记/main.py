import json
import time
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

    print('\033'f'[0:{colour}m', response.text, '\033[m')  # 31-37
    return txt


def run(yyrq, shij, bianhao, diz):
    seckill(f'{yyrq}', f'{shij}', f'{bianhao}', f'{diz}',
            '夏正', '421126199501101758', '13691777188',
            '李琳', '532128199610130346', '15764233924',
            32)
    # seckill(f'{yyrq}', f'{shij}', f'{bianhao}', f'{diz}',
    #         '闻一龙', '330193198801260013', '18858277711',
    #         '刘瑶玥', '360602199512130027', '15711966886',
    #         32)
    return


if __name__ == '__main__':
    run()
