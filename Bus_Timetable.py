from selenium import webdriver as wd
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

UI_FORM = uic.loadUiType("Bus_Timetable.ui")[0]

class MyWindow(QMainWindow, UI_FORM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.pushButton.clicked.connect(self.get_number_and_timetable)

    def get_number_and_timetable(self):
        Bus_number = self.lineEdit.text()
        browser = wd.Chrome('[파일경로]/chromedriver.exe') #파일경로 부분은 본인이 chromedriver설치한 경로. 권한 거부 오류 시 실행파일명까지 쓰면 실행됨.
        url = "http://bus.jeju.go.kr/schedule/view/" + Bus_number
        browser.get(url)
        
    def timeout(self):
        current_time = QTime.currentTime()

        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간: " + text_time

        self.statusbar.showMessage(time_msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()




