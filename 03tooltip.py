import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

"""
QToolTip 공식문서
https://doc.qt.io/qt-5/qtooltip.html
"""

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10)) #ToolTip의 (폰트, 폰트 크기 설정)
        self.setToolTip('This is a <b>QWidget</b> widget') #창의 Body영역에 ToolTips적용

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget') #버튼에 ToolTips적용
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips') #창 이름
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(300, 300, 300, 200) #창의 위치와 크기 설정(x,y,width,hight)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) #QApplication 공식문서 : https://doc.qt.io/qt-5/qapplication.html
    ex = MyApp()
    sys.exit(app.exec_()) #없으면 바로 꺼짐