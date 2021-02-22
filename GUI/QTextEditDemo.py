'''

QTextEdit控件

'''

from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget) :
    def __init__(self):
        super(QTextEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('点一下看看')

        self.resize(300,320)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('先点这里')
        self.buttonHTML = QPushButton('再点这里')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)



        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)



    def onClick_ButtonText(self):
        self.textEdit.setPlainText('Hello World，姚远？')

    def onClick_ButtonHTML(self):
        self.textEdit.setPlainText('我的姚远宝贝，爱你哦')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())