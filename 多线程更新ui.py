import sys
import time

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
        # 无限循环，每秒钟传递一次时间给UI
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_data.emit(str(currentTime))
            time.sleep(1)


class DemoWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 100)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(400, 100)

        # 创建子线程
        self.subThread = UpdateThread()
        # 将子线程中的信号与timeUpdate槽函数绑定
        self.subThread.update_data.connect(self.timeUpdate)
        # 启动子线程（开始更新时间）
        self.subThread.start()

        # 添加窗口标题
        self.setWindowTitle("SubThreadDemo")

    # 被子线程的信号触发，更新一次时间
    def timeUpdate(self, data):
        self.lineEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/icon.ico"))
    # 创建一个主窗口
    mainWin = DemoWin()
    # 显示
    mainWin.show()
    # 主循环
    sys.exit(app.exec_())