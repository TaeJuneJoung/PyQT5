import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

"""
QMenuBar 공식문서
https://doc.qt.io/qt-5/qmenubar.html
"""

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('./imgs/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q') #단축키 설정
        exitAction.setStatusTip('Exit application') #status창에 hover시, 해당 내용 출력
        exitAction.triggered.connect(qApp.quit) #클릭시 종료로 연결

        self.statusBar().showMessage('Ready')

        menuBar = self.menuBar() #메뉴바 생성
        menuBar.setNativeMenuBar(False)
        fileMenu = menuBar.addMenu('&File') #`&`는 간편하게 단축키 설정 / File의 F와 함께 'Alt+F'가 File메뉴의 단축키
        fileMenu.addAction(exitAction)


        QToolTip.setFont(QFont('SansSerif', 10)) #ToolTip의 (폰트, 폰트 크기 설정)
        self.setToolTip('This is a <b>QWidget</b> widget') #창의 Body영역에 ToolTips적용

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget') #버튼에 ToolTips적용
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('MenuBar') #창 이름
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(300, 300, 300, 200) #창의 위치와 크기 설정(x,y,width,hight)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) #QApplication 공식문서 : https://doc.qt.io/qt-5/qapplication.html
    ex = MyApp()
    sys.exit(app.exec_()) #없으면 바로 꺼짐