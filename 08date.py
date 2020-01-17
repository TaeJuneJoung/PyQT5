import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt, QTime, QDateTime

"""
[QDate 공식 문서]
https://doc.qt.io/qt-5/qdate.html
[QTime 공식 문서]
https://doc-snapshots.qt.io/qt5-5.12/qtime.html
[QDateTime 공식 문서]
https://doc.qt.io/qt-5/qdatetime.html
"""

# 날짜 출력 - QDate
now = QDate.currentDate()
print(now.toString()) #금 1 17 2020
print(now.toString('d.M.yy')) #17.1.20
print(now.toString('dd.MM.yyyy')) #17.01.2020
print(now.toString('ddd.MMMM.yyyy')) #금.1월.2020

print(now.toString(Qt.ISODate)) #2020-01-17
print(now.toString(Qt.DefaultLocaleLongDate)) #2020년 1월 17일 금요일
print(now.toString(Qt.DefaultLocaleShortDate)) #2020-01-17

# 시간 출력 - QTime
time = QTime.currentTime()
print(time.toString()) #19:06:28
print(time.toString('h.m.s')) #19.7.49
print(time.toString('hh.mm.ss')) #19.07.49
print(time.toString('hh.mm.ss.zzz')) #19.07.49.620

print(time.toString(Qt.DefaultLocaleLongDate)) #오후 7:07:49
print(time.toString(Qt.DefaultLocaleShortDate)) #오후 7:07

# 날짜와 시간 출력 - QDateTime
datetime = QDateTime.currentDateTime()
print(datetime.toString()) #금 1 17 19:10:41 2020
print(datetime.toString('d.M.yy hh:mm:ss')) #17.1.20 19:10:51
print(datetime.toString('dd.MM.yyyy, hh:mm:ss')) #17.01.2020, 19:10:51
print(datetime.toString(Qt.DefaultLocaleLongDate)) #2020년 1월 17일 금요일 오후 7:10:51
print(datetime.toString(Qt.DefaultLocaleShortDate)) #2020-01-17 오후 7:10

# 상태 표시줄에 날짜 표시하기
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        
        self.setWindowTitle('Date')
        self.setGeometry(300,300,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())