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
    print('\033'f'[0:{colour}m', date_time, response.text, '\033[m')  # 31-37
    return txt


# sj=datetime.datetime.strptime(shijian,'%Y-%m-%d')转时间的写法


def run():
    jishiqi = threading.Timer(1, run)
    jishiqi.start()
    time = datetime.datetime.now()  # 当前时间
    shijisj = str(time + datetime.timedelta(days=15))
    mubiaosj = shijisj.split(' ')[0] + ' 08:29:58'
    print('系统时间是：' + str(time))
    print('约号时间是：' + str(mubiaosj))
    if shijisj >= mubiaosj:
        jishiqi.cancel()
        print('时机已到')
        data = seckill('2022-09-09', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                       '周伟', '44030119930208551X', '15219490212',
                       '贺敏', '440307199204270023', '18320755503',
                       32, shijisj)
        while True:

            if re.search('剩余号源不够', data) is None:
                print('开始放号啦！加油冲')
                break
            else:
                print('不能秒，重来')
                data = seckill('2022-09-09', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                               '周伟', '44030119930208551X', '15219490212',
                               '贺敏', '440307199204270023', '18320755503',
                               32, shijisj)
        seckill('2022-09-09', '10:00-11:00', '440304', '深圳市福田区民政局婚姻登记处',
                '陈嘉锋', '440582199405150117', '13410493627',
                '庄思琪', '441522199509014982', '13682351456',
                33, shijisj)
        seckill('2022-09-09', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                '郑丰洋', '430602199204112538', '17665328537',
                '张意敏', '420202199402090022', '18200700061',
                34, shijisj)
        seckill('2022-09-09', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                '邱川', '445281199902105239', '18319998644',
                '陈小琼', '445221200010281949', '15338861233',
                35, shijisj)
        seckill('2022-09-09', '16:30-17:00', '440304', '深圳市福田区民政局婚姻登记处',
                '王凯宁', '210603199210200513', '15013889171',
                '史艾欢', '445224199507260389', '13510392904',
                36, shijisj)
        seckill('2022-09-09', '14:00-14:30', '440304', '深圳市福田区民政局婚姻登记处',
                '林俊豪', '445224199703181899', '15819642757',
                '吴玉燕', '445224199508200943', '15766752181',
                32, shijisj)
        seckill('2022-09-09', '15:30-16:30', '440304', '深圳市福田区民政局婚姻登记处',
                '刘庭瑀', '445224199703181899', '15819642757',
                '甘晓英', '445224199508200943', '15766752181',
                33, shijisj)

        seckill('2022-09-09', '14:00-14:30', '440304', '深圳市福田区民政局婚姻登记处',
                '朱俊贤', '440306199401020211', '13632697015',
                '姚秋怡', '440306199310220824', '13510679978',
                32, shijisj)
        seckill('2022-09-09', '15:30-16:30', '440304', '深圳市福田区民政局婚姻登记处',
                '林益帆', '350724199002150011', '18575679235',
                '钟真', '430602199505253529', '15692095250',
                32, shijisj)
        seckill('2022-09-09', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
                '徐剑', '421123198310090810', '19523333542',
                '林小捷', '445222198805093323', '15889775846',
                32, shijisj)
        seckill('2022-09-09', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
                '常诚', '320103199705091775', '19129519367',
                '王希琛', '320705199702283566', '19129515397',
                32, shijisj)
        seckill('2022-09-09', '10:00-11:00', '440304', '深圳市福田区民政局婚姻登记处',
                '闻一龙', '330193198801260013', '18858277711',
                '刘瑶玥', '360602199512130027', '15711966886',
                32, shijisj)
        seckill('2022-09-09', '10:00-11:00', '440304', '深圳市福田区民政局婚姻登记处',
                '汤贤燊', '44180219950302761X', '13346460901',
                '何家琪', '44182719960228474X', '17722667448',
                32, shijisj)
        seckill('2022-09-09', '10:00-11:00', '440304', '深圳市福田区民政局婚姻登记处',
                '吴泽鹏', '440514199412253011', '13480630625',
                '陈钰美', '440582199507171522', '15279101998',
                32, shijisj)

        seckill('2022-09-09', '9:00-10:00', '440306', '深圳市宝安区民政局婚姻登记处',
                '关子杨', '440306199501230435', '13728763733',
                '庄翠红', '440305199609066028', '18566239969',
                32, shijisj)
        seckill('2022-09-09', '9:00-10:00', '440305', '深圳市南山区民政局婚姻登记处',
                '涂军', '421125199511021333', '15971327894',
                '刘艳', '421081199706253420', '15586005136',
                32, shijisj)
        seckill('2022-09-09', '14:00-14:30', '440304', '深圳市福田区民政局婚姻登记处',
                '李德爽', '370802199509053051', '15253736958',
                '孙璐', '130302199406241824', '15004258007',
                32, shijisj)
        seckill('2022-09-09', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
                '巨翔', '620102199201082714', '18680687757',
                '袁溢', '620121199105110526', '17793107266',
                32, shijisj)
        seckill('2022-09-09', '9:00-10:00', '440305', '深圳市南山区民政局婚姻登记处',
                '赖宇轩', '440882199008318218', '13434156462',
                '罗嘉欣', '441324199601063324', '15622733526',
                32, shijisj)
        seckill('2022-09-09', '16:30-17:00', '440304', '深圳市福田区民政局婚姻登记处',
                '叶小建', '440303198302085112', '13632688982',
                '陈林琳', '441522199202020683', '13480727215',
                32, shijisj)
        seckill('2022-09-09', '15:30-16:30', '440304', '深圳市福田区民政局婚姻登记处',
                '周彦松', '430481198710200055', '13392384309',
                '徐丽芸', '430481199509100786', '15211806667',
                32, shijisj)

        seckill('2022-09-09', '14:30-15:30', '440305', '深圳市南山区民政局婚姻登记处',
                '吴耿创', '445224199407083979', '13723788488',
                '黄程程', '441581199502258626', '15813813771',
                32, shijisj)
        seckill('2022-09-09', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
                '杨涛', '350681199707094736', '18060233303',
                '武延', '150105199509108323', '18647150719',
                32, shijisj)
        seckill('2022-09-09', '14:30-15:30', '440304', '深圳市福田区民政局婚姻登记处',
                '毛浥龙', '430528199503180010', '18207391678',
                '黄锦滨', '350211199501163520', '17600350067',
                32, shijisj)
        seckill('2022-09-09', '10:00-11:00', '440311', '深圳市光明区民政局婚姻登记处',
                '周鑫', '513822199405205799', '18708123645',
                '陈玉', '532128199610130346', '18487147597',
                32, shijisj)
        seckill('2022-09-09', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                '胡昊贤', '440182199509240051', '15622171772',
                '林安欣', '440509199607274022', '15820591044',
                32, shijisj)
        seckill('2022-09-09', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                '姚希伟', '441625199805167697', '13556826662',
                '马少慧', '440304199808250729', '13147022300',
                32, shijisj)
        seckill('2022-09-09', '9:00-10:00', '440304', '深圳市福田区民政局婚姻登记处',
                '龙振宇', '430903199512023011', '18824606890',
                '杨帆', '150927199511180326', '18899859942',
                32, shijisj)
        input('输入任意字符退出程序')

    return


if __name__ == '__main__':
    run()
