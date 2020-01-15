import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') #창 이름
        self.setWindowIcon(QIcon('logo.png'))
        self.move(300, 300) #켜지는 좌표x, y
        self.resize(400, 200) #가로, 세로 - 기본 크기 있음
        # self.setGeometry(300, 300, 300, 200) #창의 위치와 크기 설정(x,y,width,hight)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) #QApplication 공식문서 : https://doc.qt.io/qt-5/qapplication.html
    ex = MyApp()
    sys.exit(app.exec_()) #없으면 바로 꺼짐