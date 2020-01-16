import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

"""
QToolBar 공식문서
https://doc.qt.io/qt-5/qtoolbar.html
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

        editAction = QAction(QIcon('./imgs/edit.png'), 'Edit', self)
        editAction.setShortcut('Ctrl+E')
        editAction.setStatusTip('Edit')
        
        printAction = QAction(QIcon('./imgs/print.png'), 'Print', self)
        printAction.setShortcut('Ctrl+P')
        printAction.setStatusTip('Print')

        self.statusBar().showMessage('Ready')

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(editAction)
        self.toolbar.addAction(printAction)

        self.setWindowTitle('ToolBar') #창 이름
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(300, 300, 300, 200) #창의 위치와 크기 설정(x,y,width,hight)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_()) #없으면 바로 꺼짐