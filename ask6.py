import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

import threading
import random


import io

import threading

from PyQt5.QtCore import Qt, QBasicTimer

dimension=40
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.usingCPUValue = 0
        self.maxFans = 15
        self.start = True
        self.valueCPU = 0
        self.tempCChangeUp = 45
        self.tempCChangeDown = 15
        self.numberOfFans = 0
        self.powerFans = 0
        self.temperature = 0
        self.zapychacz = 0
        self.cannotChangeFans = False
        self.changedFansCount = 0
        self.userON = 0
        self.initUI()

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.repaint()
        else:
            super.timerEvent(event)



    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.repaint()
        else:
            super.timerEvent(event)

    def paintEvent(self, *args, **kwargs):
        try:
            self.zapychacz = 0
            # self.tempC.display(self.temperature)
            # self.usingCPU.setValue(self.valueCPU)
            # print("refresh")


            # rand = random.randint(-1, 1)
            # temp = self.usingCPU.value() + rand
            # self.value = temp
            # self.usingCPU.setValue(self.value)


        except:
            pass

    def tempCLCD(self):

            temp = random.uniform(8.5, 9)
            if(self.valueCPU == 0 ):
                self.temperature = 0
            else:
                self.temperature = temp * self.valueCPU / 4 - self.numberOfFans * 10
                if(self.temperature<3):
                    self.temperature = random.randint(3,8)

            #
            tempDif = self.tempCChangeUp - self.temperature
            if(tempDif !=0):
                if(self.numberOfFans != 0):
                    if (tempDif > 30 ):
                        self.powerFans = random.randint(5, 20)
                    elif (tempDif < 30 and tempDif > 10 ):
                        self.powerFans = random.randint(20, 30)
                    elif(tempDif<10 and tempDif>0):
                        self.powerFans = random.randint(30,50)
                    elif(tempDif<0 and tempDif>-15):
                        self.powerFans = random.randint(30,50)
                    elif(tempDif<-15 and tempDif>-30):
                        self.powerFans = random.randint(50,75)
                    elif(tempDif<-30 and tempDif>-40 ):
                        self.powerFans = random.randint(75,85)
                        content = self.textEdit.toPlainText() + "UWAGA: Mocne użycie wentylatorów! \n"
                        self.textEdit.setPlainText(content)
                    elif(tempDif<-40):
                        self.powerFans = random.randint(90, 100)
                        content = self.textEdit.toPlainText() + "ERROR: Wentylatory pracują na pelnych obrotach! \n"
                        self.textEdit.setPlainText(content)
                else:
                    self.powerFans = 0
                # elif (self.changedFansCount == 1):
                #     self.powerFans = random.randint(70, 85)
                #     content = self.textEdit.toPlainText() + "UWAGA: Mocne użycie wentylatorów! \n"
                #     self.textEdit.setPlainText(content)
                # else:
                #     self.powerFans = random.randint(95, 100)
                #     content = self.textEdit.toPlainText() + "ERROR: Wentylatory pracują na pelnych obrotach! \n"
                #     self.textEdit.setPlainText(content)


            # print("powerFans:" + str(self.powerFans))
            self.tempC.display(self.temperature)
            self.fanUsing.setValue(self.powerFans)



    def usingFans(self):
        if (self.temperature > self.tempCChangeUp  and self.numberOfFans < self.maxFans and self.cannotChangeFans == False):
            self.numberOfFans = self.numberOfFans + 1
            content = self.textEdit.toPlainText() + "Uruchomienie dodatkowego wentylatora \n"
            self.textEdit.setPlainText(content)
        elif (self.temperature < self.tempCChangeDown and  self.numberOfFans>0 and self.cannotChangeFans == False ):
            self.numberOfFans = self.numberOfFans - 1
            content = self.textEdit.toPlainText() + "Wylaczenie jednego wentylatora \n"
            self.textEdit.setPlainText(content)

        self.fanNumbers.display(self.numberOfFans)



    def turnOnProcessor(self):
        # print("przed if")


        if( self.valueCPU<25):
            self.valueCPU = self.valueCPU + 2
            print("<25")
            print(self.valueCPU)
            self.usingCPU.setValue(self.valueCPU)

        else:
            # print("el if")
            rand = random.randint(-2, 2)
            temp = self.valueCPU + rand
            self.valueCPU = temp
            self.usingCPU.setValue(self.valueCPU)
            self.timerTurnOn.stop()




    def okUser(self):
        if self.start == True:

            self.start = False
            # print("ok")
            content = self.textEdit.toPlainText() + "Uruchomienie linii produkcyjnej \n"
            self.textEdit.setPlainText(content)
            self.timerTurnOn = QtCore.QTimer()
            self.timerTurnOn.start(200)
            self.timerTurnOn.timeout.connect(self.turnOnProcessor)
            self.timerTurnOnLCD = QtCore.QTimer()
            self.timerTurnOnLCD.start(2000)
            self.timerTurnOnLCD.timeout.connect(self.tempCLCD)
            self.timerTurnOnFans = QtCore.QTimer()
            self.timerTurnOnFans.start(2000)
            self.timerTurnOnFans.timeout.connect(self.usingFans)
            self.checkUser = QtCore.QTimer()
            self.checkUser.start(100)
            self.checkUser.timeout.connect(self.checkUserFun)
        elif self.start == False:
            self.cannotChangeFans = False
            self.changedFansCount = 0
            content = self.textEdit.toPlainText() + "Uwaga: Powrót do trybu [auto] \n"
            self.textEdit.setPlainText(content)

    def turnAnotherFanFun(self):
        if (self.start == False):
            self.changedFansCount = 0
            self.numberOfFans = self.numberOfFans +1
            if(self.cannotChangeFans == False):
                content = self.textEdit.toPlainText() + "Uwaga:Przejscie do trybu [manual]. Aby wrócic do trybu [auto] proszę kliknac przycisk [ok] \n Uruchomienie dodatkowego wentylatora"
                self.textEdit.setPlainText(content)
                self.cannotChangeFans = True
            else:
                content = self.textEdit.toPlainText() + " Uruchomienie dodatkowego wentylatora\n"
                self.textEdit.setPlainText(content)

    def turnOffFanFun(self):
        if (self.numberOfFans > 0 and self.start == False):
            self.numberOfFans = self.numberOfFans -1
            self.changedFansCount = self.changedFansCount +1
            if(self.cannotChangeFans == False):
                content = self.textEdit.toPlainText() + "Uwaga:Przejscie do trybu [manual]. Aby wrócic do trybu [auto] proszę kliknac przycisk [ok] \n Wylaczenie jednego wentylatora"
                self.textEdit.setPlainText(content)
                self.cannotChangeFans = True
            else:
                content = self.textEdit.toPlainText() + " Wylaczenie jednego wentylatora\n"
                self.textEdit.setPlainText(content)


    def lessWorkFun(self):
        # print("mniej roboty")
        if(self.start == False):
            self.prevValProc = self.valueCPU
            self.timerLessWork = QtCore.QTimer()
            self.timerLessWork.start(200)
            self.timerLessWork.timeout.connect(self.lessWorkFunChanger)

    def moreWorkFun(self):
        if self.start == False:
        # print("wiecej roboty")
            self.prevValProc = self.valueCPU
            self.timerMoreWork = QtCore.QTimer()
            self.timerMoreWork.start(200)
            self.timerMoreWork.timeout.connect(self.moreWorkFunChanger)

    def moreWorkFunChanger(self):
        randomDif = random.randint(12,17)
        if(abs(self.valueCPU-self.prevValProc)<randomDif and self.valueCPU<90):
            self.valueCPU = self.valueCPU + random.randint(0,3)
            self.usingCPU.setValue(self.valueCPU)
        elif(self.valueCPU>=90):
            self.valueCPU = random.randint(90,95)
            self.timerMoreWork.stop()
        else:
            self.timerMoreWork.stop()

    def lessWorkFunChanger(self):
        randomDif = random.randint(12,17)
        if(abs(self.valueCPU-self.prevValProc)<randomDif and self.valueCPU>5):
            self.valueCPU = self.valueCPU - random.randint(0,3)
            self.usingCPU.setValue(self.valueCPU)
        elif (self.valueCPU <= 5):
            self.valueCPU = random.randint(3, 5)
            self.timerLessWork.stop()
        else:
            self.timerLessWork.stop()
    def checkUserFun(self):
        self.userON = self.userON + 1
        if (self.userON == 60):
            content = self.textEdit.toPlainText() + " ***********\n Prosze potwierdzic obecnosc przyciskiem [off] \n ***********\n"
            self.textEdit.setPlainText(content)
        elif (self.userON == 120):
            content = self.textEdit.toPlainText() + " ***********\n ERROR \n ***********\n Brak obecności uzytkownika, linia produkcyjna zostaje wylaczona\n"
            self.textEdit.setPlainText(content)
            self.start = True
            self.valueCPU = 0
            self.usingCPU.setValue(self.valueCPU)

    def userAvaible(self):
        self.userON = 0
        content = self.textEdit.toPlainText() + " ***********\n Uzytkownik jest \n ***********\n"
        self.textEdit.setPlainText(content)
    def initUI(self):
        self.setGeometry(100, 100, 643, 519)
        self.setWindowTitle('ask')

        self.setStyleSheet("#ok{\n"
"background:green;\n"
"}\n"
"#off{\n"
"background:red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.usingCPU = QtWidgets.QProgressBar(self)
        self.usingCPU.setGeometry(QtCore.QRect(140, 90, 118, 23))
        self.usingCPU.setProperty("value", 0)
        self.usingCPU.setObjectName("usingCPU")
        self.usingCPUlabel = QtWidgets.QLabel(self)
        self.usingCPUlabel.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.usingCPUlabel.setObjectName("usingCPUlabel")
        self.tempClabel = QtWidgets.QLabel(self)
        self.tempClabel.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.tempClabel.setObjectName("tempClabel")
        self.tempC = QtWidgets.QLCDNumber(self)
        self.tempC.setGeometry(QtCore.QRect(170, 20, 64, 23))
        self.tempC.setObjectName("tempC")
        self.ok = QtWidgets.QPushButton(self)
        self.ok.setGeometry(QtCore.QRect(60, 370, 221, 121))
        self.ok.setObjectName("ok")
        self.off = QtWidgets.QPushButton(self)
        self.off.setGeometry(QtCore.QRect(360, 370, 221, 121))
        self.off.setObjectName("off")
        self.fanLabel = QtWidgets.QLabel(self)
        self.fanLabel.setGeometry(QtCore.QRect(20, 160, 181, 16))
        self.fanLabel.setObjectName("fanLabel")
        self.fanUsing = QtWidgets.QProgressBar(self)
        self.fanUsing.setGeometry(QtCore.QRect(210, 160, 118, 23))
        self.fanUsing.setProperty("value", 0)
        self.fanUsing.setObjectName("fanUsing")
        self.turnAnotherFan = QtWidgets.QPushButton(self)
        self.turnAnotherFan.setGeometry(QtCore.QRect(360, 0, 271, 51))
        self.turnAnotherFan.setObjectName("turnAnotherFan")
        self.fanNumbers = QtWidgets.QLCDNumber(self)
        self.fanNumbers.setGeometry(QtCore.QRect(190, 210, 64, 23))
        self.fanNumbers.setObjectName("fanNumbers")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 210, 151, 16))
        self.label.setObjectName("label")
        self.turnOffFan = QtWidgets.QPushButton(self)
        self.turnOffFan.setGeometry(QtCore.QRect(360, 60, 271, 51))
        self.turnOffFan.setObjectName("turnOffFan")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(350, 240, 271, 121))
        self.textEdit.setObjectName("textEdit")
        self.moreWork = QtWidgets.QPushButton(self)
        self.moreWork.setGeometry(QtCore.QRect(360, 120, 271, 51))
        self.moreWork.setObjectName("moreWork")
        self.lessWork = QtWidgets.QPushButton(self)
        self.lessWork.setGeometry(QtCore.QRect(360, 180, 271, 51))
        self.lessWork.setObjectName("lessWork")



        self.ok.clicked.connect(self.okUser)
        self.turnAnotherFan.clicked.connect(self.turnAnotherFanFun)
        self.turnOffFan.clicked.connect(self.turnOffFanFun)
        self.moreWork.clicked.connect(self.moreWorkFun)
        self.lessWork.clicked.connect(self.lessWorkFun)
        self.off.clicked.connect(self.userAvaible)





        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


        self.show()

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            self.setWindowTitle(_translate("self", "self"))
            self.usingCPUlabel.setText(_translate("self", "Zuzycie procesora"))
            self.tempClabel.setText(_translate("self", "Temperatura Procesora [C]"))
            self.ok.setText(_translate("self", "OK"))
            self.off.setText(_translate("self", "OFF"))
            self.fanLabel.setText(_translate("self", "prędkości obrotowych wentylatorów"))
            self.turnAnotherFan.setText(_translate("self", "Wlaczyc dodatkowy wentylator"))
            self.label.setText(_translate("self", "Ilosc wlączonych wentylatorow"))
            self.turnOffFan.setText(_translate("self", "Wylaczyc jeden wentylator"))
            self.moreWork.setText(_translate("self", "Wieksza ilosc pracy"))
            self.lessWork.setText(_translate("self", "Mniejsza ilosc pracy"))


    # ///////////////////////////////////////////////




    # ///////////////////////////////////////////////





# import icon_rc
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


