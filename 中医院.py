import datetime
import threading
import time

import requests


def run():
    jishiqi = threading.Timer(1, run)
    jishiqi.start()
    time1 = str(datetime.datetime.now())  # 当前时间
    mubiaosj = time1.split(' ')[0] + ' 21:00:02'
    print('系统时间是：' + str(time1))
    print('约号时间是：' + str(mubiaosj))
    if time1 >= mubiaosj:
        jishiqi.cancel()
        print('时机已到')
        global key
        key = 1
        while True:

            if key > 10:
                break
            chaxun()
            time.sleep(0.5)
            key += 1


def chaxun():

    url = "https://mp.med.gzhc365.com/api/register/schedulelist?_route=h34&a=1"

    payload = f"hisId=34&platformSource=1&platformId=34&scheduleDate=2022-{date}&deptId=103%2C68636&doctorId={doctorId}&subHisId=443&t=202209&sign=69BD0651A7BFB5CF90E0D8FDEB1DBB8B"
    print(payload)
    headers = {
        'uid': '4226892134098173964',
        'uuid': '5759a64e-f71d-4d26-b08a-1945c4b271fe',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6307062c)',
        'request-id': '799ec3ca-8b5b-4407-8655-ecd99de42c02',
        'Cookie': 'acw_tc=2f6a1fb416666159214431518e65083b5f203e3cc38c4edeed13464d600436; FE_MONITOR_USER_TRACE_ID=77c623a6-8926-48f8-8776-59401abd737e; COOKIE_JSESSIONID_34_1=1666615923051-B046CB99CAAE2C6E3E8868; FE_MONITOR_LEAVE_APP={"leaveAppTime":1666615923394}; JSESSIONID=FF2CC7858B4A037AC7542B39AD1E79D1; FE_MONITOR_LAST_PAGE={"page":"/register/docinfo","timeStamp":1666615957787}',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(response)
    ls = response['data']['itemList']

    if not ls:
        print('没有号')
    else:
        global key
        key=11
        print('来了秒杀')

        for lss in ls:
            if key==11:
                id = lss['scheduleId']
                url = "https://mp.med.gzhc365.com/api/register/generatororder?"
                payload = f"hisId=34&platformSource=1&platformId=34&subHisId=443&deptId=103%2C68636&doctorId={doctorId}&scheduleId" \
                          f"={id[:10]}_09%3A30&scheduleDate=2022-{date}&visitPeriod=1&visitBeginTime=11%3A00&visitEndTime=11%3A30" \
                          "&patientId=4227200701730684936&transParam=%7B%22regType%22%3A%20'1'%7D&extFields=%7B%7D "
                response = requests.request("POST", url, headers=headers, data=payload)
                print(payload)
                print(response.text)
                key+=1
            if lss['totalSource'] > 0:
                id = lss['scheduleId']
                url = "https://mp.med.gzhc365.com/api/register/generatororder?"
                payload = f"hisId=34&platformSource=1&platformId=34&subHisId=443&deptId=103%2C68636&doctorId={doctorId}&scheduleId" \
                          f"={id}&scheduleDate=2022-{date}&visitPeriod=1&visitBeginTime=11%3A00&visitEndTime=11%3A30" \
                          "&patientId=4227200701730684936&transParam=%7B%22regType%22%3A%20'1'%7D&extFields=%7B%7D "
                response = requests.request("POST", url, headers=headers, data=payload)
                print(payload)
                print(response.text)
                print(str(lss['scheduleId']))

if __name__ == '__main__':
    doctorId = 628
    # doctorId = 62317
    # doctorId = 60004

    date = '10-28'

    run()
