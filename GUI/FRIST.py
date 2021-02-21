import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)  #创建QApplication类的实例

W = QWidget()  #创建一个窗口

W.resize(300,150)  #设置窗口尺寸
W.move(300,300)  #移动窗口

W.setWindowTitle('第一个窗口')  #设置标题

W.show()   #显示窗口

#进入程序的主循环，并通过exit函数确保主循环安全结束

sys.exit(app.exec())