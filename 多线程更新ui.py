import sys
import time

from PyQt5 import QtWidgets, QtCore
# 导入QT,其中包含一些常量，例如颜色等
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QDateTime
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLineEdit
# 使用调色板等
from PyQt5.QtGui import QIcon


# 创建一个子线程
class UpdateThread(QThread):
    # 创建一个信号，触发时传递当前时间给槽函数
    update_data = pyqtSignal(str)

    def run(self):
        # 无限循环，调用一次传递一次给UI

            self.update_data.emit(str('这里放你要的动态参数'))
            time.sleep(1)


class DemoWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 800)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(400, 100)

        # 创建子线程
        self.subThread = UpdateThread()
        # 将子线程中的信号与printf槽函数绑定
        self.subThread.update_data.connect(self.printf)
        # 启动子线程（开始更新时间）
        self.subThread.start()

        # 添加窗口标题
        self.setWindowTitle("SubThreadDemo")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(20, 300, 400, 510))
        self.textBrowser.setObjectName("textBrowser")

    # 被子线程的信号触发，更新一次时间
    def printf(self,mes, name=''):
        self.textBrowser.append(str(mes) + name)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/icon.ico"))
    # 创建一个主窗口
    mainWin = DemoWin()
    # 显示
    mainWin.show()
    # 主循环
    sys.exit(app.exec_())