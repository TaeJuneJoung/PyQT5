import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center()
        self.show()

    def center(self): #창을 가운데 위치하게 만드는 메서드 구현
        qr = self.frameGeometry() #창의 위치와 크기 정보를 가져옴
        cp = QDesktopWidget().availableGeometry().center() #사용하는 모니터 화면의 가운데 위치 파악
        qr.moveCenter(cp) #창의 직사각형 위치를 화면의 중심의 위치로 이동
        self.move(qr.topLeft()) #현재 창을, 화면의 중심으로 이동했던 직사각형의 위치로 이동

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())