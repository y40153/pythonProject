import json

import requests


def query(shijian, bianhao, dizhi):
    url = "https://mmykm1.gdbs.gov.cn/ebus/huazi_gdhy/hunyin/api/mobile/marriage/list_times?"
    payload = json.dumps({
        "ywlx": "J",
        "bookDate": f"{shijian}",
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
            "sfzjlbnv": "",
            "sfzjhmnan": "441424199504101179",
            "sfzjhmnv": "",
            "jrzjlbnan": "",
            "jrzjlbnv": "",
            "xmnan": "张伟峰",
            "xmnv": "",
            "csrqnan": "1995-04-10",
            "csrqnv": "",
            "gjnan": "中国",
            "gjnv": "中国",
            "mznan": "",
            "mznv": "",
            "zynan": "其他从业人员",
            "zynv": "",
            "whcdnan": "大专",
            "whcdnv": "",
            "fjdnan": "广东省梅州市梅州市五华县梅州市五华县郭田镇",
            "fjdnv": "",
            "lxdhnan": "13922069284",
            "lxdhnv": "",
            "yyrq_id": "",
            "yyh": "",
            "yyrq": "2022-05-20",
            "yysj": "",
            "djjgbm": f"{bianhao}0A1000",
            "djjgmc": f"{dizhi}",
            "djjgdz": "深圳市福田区农园路30号香蜜公园西门（原市农科中心）",
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
            "area_countynv": f"{bianhao}00000",
            "area_townnan": f"{bianhao}000000",
            "area_townnv": f"{bianhao}000000",
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
    data = json.loads(response.text)  # 解读出接口返回的数据
    ydata = json.loads(payload)  # 获取提交的json数据
    shijian = ydata['bookDate']
    if __name__ == '__main__':
        for c, b in data.items():
            if c == 'data':
                data = b  # 找到数据里面想要的data
        for d in data:

            print(d)  # 打印出想要的数据

            if d['syyyl'] > 0:  # 秒杀准备，有号判断
                print('\033''[0:35m'  f'{shijian}快看啊，{d["yysj"]}这里有 {d["syyyl"]} 个号啦'  '\033[m')
            else:
                print('检查一下结果出问题了')


if __name__ == '__main__':
    date = '2022-09-13'
    query(date, '440304', "深圳市福田区民政局婚姻登记处")
    print('-' * 90)
    # query(date, '440305', "深圳市南山区民政局婚姻登记处")
