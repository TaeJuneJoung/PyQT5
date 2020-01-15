import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

"""
QPushButton
http://codetorial.net/pyqt5/widget/qpushbutton.html
"""

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit) #현재 인스턴스 종료

        self.setWindowTitle('Close Btn Program') #창 이름
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(300, 300, 300, 200) #창의 위치와 크기 설정(x,y,width,hight)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) #QApplication 공식문서 : https://doc.qt.io/qt-5/qapplication.html
    ex = MyApp()
    sys.exit(app.exec_()) #없으면 바로 꺼짐