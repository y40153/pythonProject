import datetime
import json
import sys

import requests
from PyQt5 import QtWidgets, QtGui, QtCore


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
    data = response.json()  # 解读出接口返回的数据
    data = data['data']
    # GUI.printf(data)
    for d in data:
        GUI.printf(d)  # 打印出想要的数据

        if d['syyyl'] > 0:  # 秒杀准备，有号判断
            GUI.printf("<font size='4' color='red'>"+f'{shijian}快看啊，{d["yysj"]}这里有 {d["syyyl"]} 个号啦'+ "<font>"+"<font size='3' color='black'>"+'.'+ "<font>")
        else:
            GUI.printf("<font color='green'>"+'返回的数据里面，告诉你没有号'+ "<font>"+"<font color='black'>"+'.'+ "<font>")


class GUI(QtWidgets.QWidget):
    def __init__(self):
        #初始化————init__
        super().__init__()
        self.initGUI()
    def initGUI(self):
        #设置窗口大小
        self.resize(750,800)
        #设置窗口位置(下面配置的是居于屏幕中间)
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        #设置窗口标题和图标
        self.setWindowTitle('高效查询')
        self.setWindowIcon(QtGui.QIcon('婚姻登记/1.png'))
        #设置窗口提示
        # self.setToolTip('看清楚')
        #设置label信息
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(20, 10, 150, 60))
        self.label1.setText('请选择查询的区域')
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 70, 150, 60))
        self.label.setText('请选择查询的日期')
        # 设置label提示
        self.label.setToolTip('只显示可预约的15天')
        # 设置选择框
        ls=['福田','南山','罗湖','宝安','龙华','龙岗','光明','盐田','大棚','坪山']
        self.check=[]
        dic={'福田':'440304','南山':'440305','罗湖':'440303','宝安':'440306','龙华':'440309','龙岗':'440307','光明':'440311','盐田':'440308','大棚':'440396','坪山':'440310'}
        for x in range(10):
            self.check.append(x)
            self.check[x] = QtWidgets.QCheckBox(self)
            self.check[x].setGeometry(QtCore.QRect(20*(3*x+1), 60, 87, 20))
            self.check[x].setObjectName(f"{dic[ls[x]]}")
            self.check[x].setText(f'{ls[x]}')
            self.check[x].setToolTip(f'{self.check[x].text()}')
        # #设置输入框
        # self.textbox = Qt.QLineEdit(self)
        # self.textbox.resize(120, 20)
        # self.textbox.move(100, 70)

        # # 设置输入框提示
        # self.textbox.setToolTip('不知道输入什么吗？09-09啊')
        #设置按钮
        # self.btn =QtWidgets.QPushButton('确认',self)
        # self.btn.resize(80,20)
        # self.btn.move(250,70)

        time = datetime.datetime.now()  # 当前时间
        for i in range(15):
            shijisj = str(time + datetime.timedelta(days=i + 1))
            date = shijisj.split(' ')[0]
            # 设置按钮
            self.i = QtWidgets.QPushButton(f'{date}', self)
            self.i.resize(80, 30)
            if i <8:
                self.i.move(20 + i * 80, 120)
            else:
                self.i.move(-580 + i * 80, 150)
            # 设置按钮样式
            self.i.setStyleSheet(
                                   "font: 75 12pt \"Arial Narrow\";"
                                   )
            # 点击鼠标触发事件
            self.i.clicked.connect(lambda: self.clickbtn(self.sender()))
            # 设置按钮提示
            self.i.setToolTip('点击立即查询')
            self.i.setObjectName(f'{date}')
        # 设置按钮样式
        # self.btn1.setStyleSheet("background-color: rgb(254, 185, 255);"
        #                   "border-color: rgb(110, 150, 163);"
        #                   "font: 75 12pt \"Arial Narrow\";"
        #                   "color: rgb(246, 255, 46);")

        #点击鼠标触发事件
        # self.i.clicked.connect(self.clickbtn)

        # 设置txtbox
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(20, 200, 700, 500))
        self.textBrowser.setObjectName("textBrowser")
        #展示窗口
        self.show();

    #点击鼠标触发函数
    def clickbtn(self,trp):
        # 清空输入框信息
        self.textBrowser.setText('')
        #打印出输入框的信息
        # textboxValue = self.textbox.text()
        textboxValue=self.sender()
        GUI.printf(textboxValue.objectName())
        GUI.printf('————'*10)
        # 查找所有勾选框，已经勾选的就进行提交查询
        for x in range(10):
            if self.check[x].isChecked():
                GUI.printf(self.check[x].text())
                query(textboxValue.objectName(), self.check[x].objectName(), self.check[x].text())
        # QtWidgets.QMessageBox.question(self, "信息", '你输入的输入框内容为:' + textboxValue,QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)


        GUI.printf('————'*10)

        #清空输入框信息
        # self.textbox.setText('')
    # 关闭窗口事件重写
    # def closeEvent(self, QCloseEvent):
    #     reply = QtWidgets.QMessageBox.question(self, '警告',"确定关闭当前窗口?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         QCloseEvent.accept()
    #     else:
    #         QCloseEvent.ignore()

    def printf(self, mes):
        self.textBrowser.append(str(mes))  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = GUI()
    sys.exit(app.exec_())