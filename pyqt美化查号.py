#-*-coding:utf-8-*-
#作者--宋春风
#时间：2019-03-05
'''
1.这里说明我为什不用from XXX import XXX
因为我做项目需要打包成exe，from XXX import XXX打包总失败
2.循环传值解决重要两个条件：1.button是list 2.sender接收你按钮上的字，再做为传入你的事件的值
3.这里写的已经比较清楚了，但是还不是很全面，希望能帮到和我一样遇到过懒得复制粘贴，
想循环创建多个按钮，然后直接连接事件的朋友
4.直接上代码，没有写文字解释，有看不懂的可以评论留言-------------------------
'''
import PyQt5.QtCore as Qt
import PyQt5.QtWidgets as widgets
# import PyQt5.QtWebEngineWidgets as QtWeb
import PyQt5.QtGui as gui
import sys
class Sign(widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()
        #self.grid_layout()
    def __initUI__(self):
        #窗口大小
        self.resize(400,200)
        self.hoxlayout = widgets.QHBoxLayout(self)
        #创建一个按钮，想循环传值必须是列表（内容可以试其他我只试过数字--感兴趣可以试试其他）
        self.button1 = []
        #根据自己的要求自己设置按钮上的字---这里很重要，这些字将会做为传递参数的依据
        self.x = ['a','b','c','d']
        for j in range(0, len(self.x)):
            #将数字j加进button
            self.button1.append(j)
            self.button1[j] = widgets.QPushButton(self)
            self.button1[j].setFixedSize(50, 50)
            self.button1[j].setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
            #此处将字放到按钮上
            self.button1[j].setText(self.x[j])
            self.hoxlayout.addWidget(self.button1[j])
            #传达参数--重要，这里sender将接收你点击的字并传入函数
            self.button1[j].clicked.connect(lambda :self.table(self.sender().text()))
        #因为我这使用的是QMainWindow，所以要创建一个Widget,才能显示所有的按钮
        self.widget = widgets.QWidget()
        self.widget.setLayout(self.hoxlayout)
        self.setCentralWidget(self.widget)
    def table(self,n):
        #用于测试，因为只是测试，所有仅仅用打印来证明不是只是最后一个按钮有效，每次点击都会不同
        #解决pyqt5循环生成按钮并且直接连接事件，但是点击按钮的时候只是响应最后一个事件
        print(n)
if __name__ == "__main__":
    app = widgets.QApplication(sys.argv)
    window = Sign()
    window.show()
    sys.exit(app.exec_())