from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon

class Qbuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUL()

    def initUL(self):
        self.setWindowTitle("设置伙伴关系")

        namelabel = QLabel('&name', self)  # 标签1
        namelineedit = QLineEdit(self)  # 文本输入框1
        namelineedit.setInputMask('NNNNNNNNNNNNN;_')
        namelabel.setBuddy(namelineedit)   # 设置伙伴控件

        passwordlabel = QLabel('&password', self)  # 标签2
        passwordlineedit = QLineEdit(self)  # 文本输入框2
        passwordlabel.setBuddy(passwordlineedit)  # 设置伙伴控件

        butOK = QPushButton("&OK")
        butCancel = QPushButton("&Cancel")

        mainlayout = QGridLayout(self)

        mainlayout.addWidget(namelabel, 0, 0)
        mainlayout.addWidget(namelineedit, 0, 1, 1, 2)

        mainlayout.addWidget(passwordlabel, 1, 0)
        mainlayout.addWidget(passwordlineedit, 1, 1, 1, 2)

        mainlayout.addWidget(butOK, 2, 0)
        mainlayout.addWidget(butCancel, 2, 1)

        #self.resize(800, 600)
        self.setWindowIcon(QIcon('D:\EXE\github\src\controls\images\Game Board.ico'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Qbuddy()
    main.show()
    sys.exit(app.exec_())
    print(1)