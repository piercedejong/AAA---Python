# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

naziM = QtGui.QSound("nazi.wav")
ussrM = QtGui.QSound("ussr.wav")
japanM = QtGui.QSound("japan.wav")
americaM = QtGui.QSound("america.wav")
britainM = QtGui.QSound("britain.wav")
italyM = QtGui.QSound("italy.wav")

music = [naziM,ussrM,japanM,americaM,britainM,italyM]
red = (255,0,0)
orange = (255,69,0)
yellow = (255,255,0)
green = (34,180,34)
blue = (0,0,255)
purple = (127,0,255)
pink = (255,0,127)
grey = (100,100,100)
black = (10,10,10)
white = (255,255,255)
brown = (139,69,19)
beige = (215,200,173)

light_red = (255,102,102)
light_orange = (255,178,102)
light_yellow = (255,255,102)
light_green = (102,255,102)
light_blue = (102,102,255)
light_purple = (178,102,255)
light_pink = (255,102,178)
light_grey = (192,198,198)
light_black = (90,90,90)
light_brown = (185,110,50)
light_beige = (245,215,185)

dark_red = (153,0,0)
dark_blue = (0,0,153)

ECO_FONT_SIZE = 35
FONT_SIZE = 40
UNIT_FONT_SIZE = 25
OBJ_FONT_SIZE = 20

UNIT_COLOR_1 = black
UNIT_COLOR_2 = yellow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(100,100)
        MainWindow.setStyleSheet("QMainWindow {background: grey}")
        #MainWindow.show
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ecoNation = 0
        self.natNation = 0
        self.natTotalValue = 0
        self.CAPITOL_TOTAL = 22
        self.CAPITOL_VICTORY = 16
        self.set_colors()
        self.load()
        self.nation_names()
        self.eco_display()
        self.nation_turn_display()
        self.capitol_side_display()
        self.unit_display()
        self.nation_objectives_info()
        self.main_loop()
        self.bankChange=[self.GB,self.UB,self.JB,self.AB,self.CB,self.BB,self.IB,self.NB,self.FB]
        self.incomeChange=[self.GI,self.UI,self.JI,self.AI,self.CI,self.BI,self.II,self.NI,self.FI]
        self.unitCount=[self.count0,self.count1,self.count2,self.count3,self.count4,self.count5,self.count6,self.count7,self.count8,self.count9,self.count10,self.count11,self.count12,self.count13,self.count14]
        self.bChange=[self.plus1B,self.plus5B,self.minus1B,self.minus5B]
        self.iChange=[self.plus1I,self.plus5I,self.minus1I,self.minus5I]
        self.nChange=[self.nat0,self.nat1,self.nat2,self.nat3,self.nat4,self.nat5,self.nat6,self.nat7]

        self.bank_old = list(self.bank)
        self.count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.NATION_NAME = ["Germany","USSR","Japan","America","China","Britain","Italy","ANZAC","France"]
        self.UNIT_NAME = ["infantry","artillery"," mobile infantry","tank","anti-tank","anti-aircarft","fighter","  tactical bomber","bomber","submarine","destroyer","transport","cruiser","aircraft-carrier","battleship"]
        self.unitStat = ["1 2 1 3","2 2 1 4","1 2 2 4","3 3 2 6","2 3 1 6","0 0 1 5","3 4 4 10","3 3 4 11","4 1 6 12","2 1 2 8","0 0 2 8","2 2 2 8","3 3 2 12","0 2 2 16","4 4 2 20"]


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def load(self):
        newGame = str(input("\nWould you like to start a (n)ew game or (c)ontinue an old one: "))
        if newGame == ("n" or "N"):
            self.gameVersion = str(input("Enter a save slot to override: "))
            readFile = open("newGameQT.txt", "r")
        elif newGame == ("c" or "C"):
            self.gameVersion = str(input("Enter save slot to open: "))
            readFile = open("continueGameQT_"+self.gameVersion+".txt", "r")
        info = readFile.readlines()
        self.bank = info[1].replace("[","").replace("]","").replace("'","").replace(","," ").replace("\"","")
        self.bank = self.bank.split()
        self.bank = list(map(int,self.bank)) #converts numbers to ints

        self.income = info[3].replace("[","").replace("]","").replace("'","").replace(","," ").replace("\"","")
        self.income = self.income.split()
        self.income = list(map(int,self.income)) #converts numbers to ints

        self.nation = int(info[5])
        self.turn = int(info[7])
        self.axis_capitols = int(info[9])
        self.allies_capitols = self.CAPITOL_TOTAL-self.axis_capitols

        readFile.close()
    def save(self):
        openFile = open("continueGameQT_"+self.gameVersion+".txt","w")
        openFile.write("#Bank")
        openFile.write("\n")
        openFile.write(str(self.bank))
        openFile.write("\n")
        openFile.write("#Income")
        openFile.write("\n")
        openFile.write(str(self.income))
        openFile.write("\n")
        openFile.write("#Nation")
        openFile.write("\n")
        openFile.write(str(self.nation))
        openFile.write("\n")
        openFile.write("#Round")
        openFile.write("\n")
        openFile.write(str(self.turn))
        openFile.write("\n")
        openFile.write("#Axis Capitols")
        openFile.write("\n")
        openFile.write(str(self.axis_capitols))
        openFile.close
    def main_loop(self):
        self.end_turn_BUTTON()
        self.change_eco_nation_BUTTON()
        self.change_eco_BUTTONS()
        self.buy_unit_BUTTONS()
        self.resest_buy_BUTTON()
        self.capitol_change_BUTTONS()
        self.national_objectives_BUTTONS()

    def victory_display(self,value,color,value_2,value_3):
        max_income = max(self.income)
        max_income_index = self.income.index(max_income)

        if value_3 == True:
            print("axis")
            if max_income_index == 0:
                music[0].play()
            elif max_income_index == 2:
                music[2].play()
            elif max_income_index == 5:
                music[5].play
        else:
            print("allies")
            if max_income_index == 1:
                music[1].play()
            elif max_income_index == 3:
                music[3].play()
            elif max_income_index == 4:
                music[4].play()

        self.vDisplay.setText(_translate("MainWindow", str(value), None))
        self.vDisplay.setStyleSheet('color: rgb{}'.format(str(color)))

        self.nation =value_2
    def check_victory(self):
        if self.axis_capitols >= self.CAPITOL_VICTORY:
            self.victory_display("AXIS WIN",red,8,True)
        if self.allies_capitols >= self.CAPITOL_VICTORY:
            self.victory_display("ALLIES WIN",blue,8,False)
    def change_nation(self):
        self.nation = self.nation + 1
        if self.nation == 9:
            self.turn = self.turn + 1
            self.nation = 0
            self.check_victory()
        self.natNation = self.nation
        self.natTotalValue = 0
    def update_bank(self):
        self.bank[self.nation] = self.bank[self.nation] + self.income[self.nation]
        self.bank_old[self.nation] = int(self.bank[self.nation])
        self.bankChange[self.nation].setText(_translate("MainWindow", str(self.bank[self.nation]), None))
    def update_nation(self):
        self.NT.setText(_translate("MainWindow", str(self.NATION_NAME[self.nation]) + "|" + str(self.turn), None))
        self.NT.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.nation])))
        self.resetBuyBUTTON.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.nation])))
        self.endTurnButton.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.nation])))
    def reset_unit_count(self):
        self.count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        loop = 0
        while loop < len(self.count):
            self.unitCount[loop].setText(_translate("MainWindow", str(self.count[loop]), None))
            loop = loop + 1
    def check_nat_objectives(self):
        loop = 0

        while loop < len(self.nChange):
            if self.nat_obj[self.nation][loop][0] == True:
                self.bank[self.nation] = self.bank[self.nation] + self.nat_obj[self.nation][loop][1]
            loop = loop+1
    def change_nat_objectives_string(self,value):
        loop = 0
        while loop < len(self.nChange):
            self.nChange[loop].setText(_translate("MainWindow", str(self.nat_obj[value][loop][1])+"|"+str(self.nat_obj[value][loop][2]), None))
            if self.nat_obj[value][loop][0] == False:
                self.nChange[loop].setStyleSheet('Text-align:left; background-color: rgb{}'.format(str(white)))
            else:
                self.natTotalValue = self.natTotalValue + self.nat_obj[value][loop][1]
                self.nChange[loop].setStyleSheet('Text-align:left;background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[value])))
            if self.nat_obj[value][loop][1] == 0:
                print("yes")
                self.nChange[loop].setStyleSheet('Text-align:left; background-color: rgb{}'.format(str(black)))
            loop = loop + 1
            self.natTotal.setText(_translate("MainWindow", str(self.NATION_NAME[value])+"|"+str(self.natTotalValue), None))
            self.natTotal.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_ECO[value])))
    def nat_objectives_string_change(self,value,change):
        self.natTotalValue = 0
        value = value + change
        if value == 8:
            value = 0
        if value == -1:
            value = 7
        self.natNation = value
        self.change_nat_objectives_string(value)
    def end_turn_BUTTON(self):
        self.endTurnButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.endTurnButton.setFont(font)
        self.endTurnButton.setStyleSheet('background-color: rgb{}'.format(str(white)))
        self.endTurnButton.setObjectName(_fromUtf8("endTurnButton"))
        self.endTurnButton.clicked.connect(lambda: self.end_turn())
        self.gridLayout.addWidget(self.endTurnButton, 16, 15, 3, 3)
    def end_turn(self):
        self.check_nat_objectives()
        self.update_bank()
        self.change_nation()
        self.update_nation()
        self.reset_unit_count()
        self.change_nat_objectives_string(self.nation)
        self.save()

    def capitol_change_BUTTONS(self):
        self.axisCapitolsBUTTON = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.axisCapitolsBUTTON.setFont(font)
        self.axisCapitolsBUTTON.setStyleSheet('background-color: rgb{}'.format(str(red)))
        self.axisCapitolsBUTTON.setObjectName(_fromUtf8("endTurnButton"))
        self.axisCapitolsBUTTON.clicked.connect(lambda: self.capitol_change(1))
        self.gridLayout.addWidget(self.axisCapitolsBUTTON, 14, 16, 1, 1)

        self.alliesCapitolsBUTTON = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.alliesCapitolsBUTTON.setFont(font)
        self.alliesCapitolsBUTTON.setStyleSheet('background-color: rgb{}'.format(str(blue)))
        self.alliesCapitolsBUTTON.setObjectName(_fromUtf8("endTurnButton"))
        self.alliesCapitolsBUTTON.clicked.connect(lambda: self.capitol_change(-1))
        self.gridLayout.addWidget(self.alliesCapitolsBUTTON, 14, 17, 1, 1)
    def capitol_change(self,value):
        self.axis_capitols = self.axis_capitols + value
        self.allies_capitols = self.CAPITOL_TOTAL-self.axis_capitols
        self.axisCapitolsBUTTON.setText(_translate("MainWindow", str(self.axis_capitols), None))
        self.alliesCapitolsBUTTON.setText(_translate("MainWindow", str(self.allies_capitols), None))

    def resest_buy_BUTTON(self):
        self.resetBuyBUTTON = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.resetBuyBUTTON.setFont(font)
        self.resetBuyBUTTON.setStyleSheet('background-color: rgb{}'.format(str(white)))
        self.resetBuyBUTTON.setObjectName(_fromUtf8("resetBuyBUTTON"))
        self.resetBuyBUTTON.clicked.connect(lambda: self.reset_buy())
        self.gridLayout.addWidget(self.resetBuyBUTTON, 18, 0, 1, 2)
    def reset_buy(self):
        self.bank[self.nation]=int(self.bank_old[self.nation])
        self.bankChange[self.nation].setText(_translate("MainWindow", str(self.bank[self.nation]), None))
        self.reset_unit_count()

    def change_eco_nation_BUTTON(self):
        self.changeEcoButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.changeEcoButton.setFont(font)
        self.changeEcoButton.setObjectName(_fromUtf8("changeEcoButton"))
        self.changeEcoButton.clicked.connect(lambda: self.change_eco_nation())
        self.gridLayout.addWidget(self.changeEcoButton, 2, 16, 1, 2)
    def change_eco_nation(self):
        self.ecoNation = self.ecoNation + 1
        if self.ecoNation == 9:
            self.ecoNation = 0
        self.changeEcoButton.setText(_translate("MainWindow", "B "+str(self.bank[self.ecoNation])+"|"+str(self.NATION_NAME[self.ecoNation])+"|"+str(self.income[self.ecoNation])+" I", None))
        self.changeEcoButton.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[self.ecoNation])))
        loop = 0
        loop_2 = 0
        while loop < len(self.bChange):
            while loop_2 < len(self.iChange):
                if loop_2 % 2 == 0:
                    self.bChange[loop_2].setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_ECO[self.ecoNation])))
                    self.iChange[loop_2].setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.ecoNation])))
                else:
                    self.bChange[loop_2].setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.ecoNation])))
                    self.iChange[loop_2].setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_ECO[self.ecoNation])))
                loop_2 = loop_2 + 1
            loop_2 = 0
            loop = loop + 1

    def change_eco_BUTTONS(self):
        self.plus1B = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus1B.setFont(font)
        self.plus1B.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_ECO[self.ecoNation])))
        self.plus1B.setObjectName(_fromUtf8("changeEcoButton"))
        self.plus1B.clicked.connect(lambda: self.change_eco(1,self.bank,"bank"))
        self.gridLayout.addWidget(self.plus1B, 3, 16, 1, 1)

        self.plus5B = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus5B.setFont(font)
        self.plus5B.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.ecoNation])))
        self.plus5B.setObjectName(_fromUtf8("changeEcoButton"))
        self.plus5B.clicked.connect(lambda: self.change_eco(5,self.bank,"bank"))
        self.gridLayout.addWidget(self.plus5B, 4, 16, 1, 1)

        self.minus1B = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus1B.setFont(font)
        self.minus1B.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_ECO[self.ecoNation])))
        self.minus1B.setObjectName(_fromUtf8("changeEcoButton"))
        self.minus1B.clicked.connect(lambda: self.change_eco(-1,self.bank,"bank"))
        self.gridLayout.addWidget(self.minus1B, 5, 16, 1, 1)

        self.minus5B = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus5B.setFont(font)
        self.minus5B.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.ecoNation])))
        self.minus5B.setObjectName(_fromUtf8("changeEcoButton"))
        self.minus5B.clicked.connect(lambda: self.change_eco(-5,self.bank,"bank"))
        self.gridLayout.addWidget(self.minus5B, 6, 16, 1, 1)

        self.plus1I = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus1I.setFont(font)
        self.plus1I.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.ecoNation])))
        self.plus1I.setObjectName(_fromUtf8("changeEcoButton"))
        self.plus1I.clicked.connect(lambda: self.change_eco(1,self.income,"income"))
        self.gridLayout.addWidget(self.plus1I, 3, 17, 1, 1)

        self.plus5I = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus5I.setFont(font)
        self.plus5I.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_ECO[self.ecoNation])))
        self.plus5I.setObjectName(_fromUtf8("changeEcoButton"))
        self.plus5I.clicked.connect(lambda: self.change_eco(5,self.income,"income"))
        self.gridLayout.addWidget(self.plus5I, 4, 17, 1, 1)

        self.minus1I = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus1I.setFont(font)
        self.minus1I.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.ecoNation])))
        self.minus1I.setObjectName(_fromUtf8("changeEcoButton"))
        self.minus1I.clicked.connect(lambda: self.change_eco(-1,self.income,"income"))
        self.gridLayout.addWidget(self.minus1I, 5, 17, 1, 1)

        self.minus5I = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus5I.setFont(font)
        self.minus5I.setStyleSheet('background-color: rgb{}'.format(str(self.NATION_COLOR_ECO[self.ecoNation])))
        self.minus5I.setObjectName(_fromUtf8("changeEcoButton"))
        self.minus5I.clicked.connect(lambda: self.change_eco(-5,self.income,"income"))
        self.gridLayout.addWidget(self.minus5I, 6, 17, 1, 1)
    def change_eco(self,value,money,type):
        money[self.ecoNation] = money[self.ecoNation] + value
        if type == "bank":
            self.bankChange[self.ecoNation].setText(_translate("MainWindow", str(money[self.ecoNation]), None))
        if type == "income":
            self.incomeChange[self.ecoNation].setText(_translate("MainWindow", str(money[self.ecoNation]), None))
        self.changeEcoButton.setText(_translate("MainWindow", "B "+str(self.bank[self.ecoNation])+"|"+str(self.NATION_NAME[self.ecoNation])+"|"+str(self.income[self.ecoNation])+" I", None))

    def buy_unit_BUTTONS(self):
        self.inf = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.inf.setFont(font)
        self.inf.setObjectName(_fromUtf8("inf"))
        self.inf.clicked.connect(lambda: self.buy_unit(3,0))
        self.gridLayout.addWidget(self.inf, 3, 0, 1, 1)

        self.art = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.art.setFont(font)
        self.art.setObjectName(_fromUtf8("art"))
        self.art.clicked.connect(lambda: self.buy_unit(4,1))
        self.gridLayout.addWidget(self.art, 4, 0, 1, 1)

        self.mbl = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.mbl.setFont(font)
        self.mbl.setObjectName(_fromUtf8("mbl"))
        self.mbl.clicked.connect(lambda: self.buy_unit(4,2))
        self.gridLayout.addWidget(self.mbl, 5, 0, 1, 1)

        self.tnk = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.tnk.setFont(font)
        self.tnk.setObjectName(_fromUtf8("tnk"))
        self.tnk.clicked.connect(lambda: self.buy_unit(6,3))
        self.gridLayout.addWidget(self.tnk, 6, 0, 1, 1)

        self.atk = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.atk.setFont(font)
        self.atk.setObjectName(_fromUtf8("atk"))
        self.atk.clicked.connect(lambda: self.buy_unit(6,4))
        self.gridLayout.addWidget(self.atk, 7, 0, 1, 1)

        self.aaa = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.aaa.setFont(font)
        self.aaa.setObjectName(_fromUtf8("aaa"))
        self.aaa.clicked.connect(lambda: self.buy_unit(5,5))
        self.gridLayout.addWidget(self.aaa, 8, 0, 1, 1)

        self.fgh = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.fgh.setFont(font)
        self.fgh.setObjectName(_fromUtf8("fgh"))
        self.fgh.clicked.connect(lambda: self.buy_unit(10,6))
        self.gridLayout.addWidget(self.fgh, 9, 0, 1, 1)

        self.tct = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.tct.setFont(font)
        self.tct.setObjectName(_fromUtf8("tct"))
        self.tct.clicked.connect(lambda: self.buy_unit(11,7))
        self.gridLayout.addWidget(self.tct, 10, 0, 1, 1)

        self.bmb = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.bmb.setFont(font)
        self.bmb.setObjectName(_fromUtf8("bmb"))
        self.bmb.clicked.connect(lambda: self.buy_unit(12,8))
        self.gridLayout.addWidget(self.bmb, 11, 0, 1, 1)

        self.sub = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.sub.setFont(font)
        self.sub.setObjectName(_fromUtf8("sub"))
        self.sub.clicked.connect(lambda: self.buy_unit(8,9))
        self.gridLayout.addWidget(self.sub, 12, 0, 1, 1)

        self.dst = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.dst.setFont(font)
        self.dst.setObjectName(_fromUtf8("dst"))
        self.dst.clicked.connect(lambda: self.buy_unit(8,10))
        self.gridLayout.addWidget(self.dst, 13, 0, 1, 1)

        self.trn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.trn.setFont(font)
        self.trn.setObjectName(_fromUtf8("trn"))
        self.trn.clicked.connect(lambda: self.buy_unit(8,11))
        self.gridLayout.addWidget(self.trn, 14, 0, 1, 1)

        self.crs = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.crs.setFont(font)
        self.crs.setObjectName(_fromUtf8("crs"))
        self.crs.clicked.connect(lambda: self.buy_unit(12,12))
        self.gridLayout.addWidget(self.crs, 15, 0, 1, 1)

        self.acc = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.acc.setFont(font)
        self.acc.setObjectName(_fromUtf8("acc"))
        self.acc.clicked.connect(lambda: self.buy_unit(16,13))
        self.gridLayout.addWidget(self.acc, 16, 0, 1, 1)

        self.btl = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.btl.setFont(font)
        self.btl.setObjectName(_fromUtf8("btl"))
        self.btl.clicked.connect(lambda: self.buy_unit(20,14))
        self.gridLayout.addWidget(self.btl, 17, 0, 1, 1)
    def buy_unit(self,value,but):
        self.bank[self.nation] = self.bank[self.nation] - value
        self.count[but] = self.count[but] + 1
        self.unitCount[but].setText(_translate("MainWindow", str(self.count[but]), None))
        self.bankChange[self.nation].setText(_translate("MainWindow", str(self.bank[self.nation]), None))

    def national_objectives_BUTTONS(self):
        self.nat0 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.nat0.setFont(font)
        self.nat0.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.nat0.setObjectName(_fromUtf8("nat0"))
        self.nat0.setStyleSheet("Text-align:left")
        self.nat0.clicked.connect(lambda: self.nation_objectives(self.nat_obj[self.natNation][0],0))
        self.gridLayout.addWidget(self.nat0, 6, 5,1,10)

        self.nat1 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.nat1.setFont(font)
        self.nat1.setObjectName(_fromUtf8("nat0"))
        self.nat1.setStyleSheet("Text-align:left")
        self.nat1.clicked.connect(lambda: self.nation_objectives(self.nat_obj[self.natNation][1],1))
        self.gridLayout.addWidget(self.nat1, 7, 5,1,10)

        self.nat2 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.nat2.setFont(font)
        self.nat2.setObjectName(_fromUtf8("nat0"))
        self.nat2.setStyleSheet("Text-align:left")
        self.nat2.clicked.connect(lambda: self.nation_objectives(self.nat_obj[self.natNation][2],2))
        self.gridLayout.addWidget(self.nat2, 8, 5,1,10)

        self.nat3 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.nat3.setFont(font)
        self.nat3.setObjectName(_fromUtf8("nat0"))
        self.nat3.setStyleSheet("Text-align:left")
        self.nat3.clicked.connect(lambda: self.nation_objectives(self.nat_obj[self.natNation][3],3))
        self.gridLayout.addWidget(self.nat3, 9, 5,1,10)

        self.nat4 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.nat4.setFont(font)
        self.nat4.setObjectName(_fromUtf8("nat0"))
        self.nat4.setStyleSheet("Text-align:left")
        self.nat4.clicked.connect(lambda: self.nation_objectives(self.nat_obj[self.natNation][4],4))
        self.gridLayout.addWidget(self.nat4, 10, 5,1,10)

        self.nat5 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.nat5.setFont(font)
        self.nat5.setObjectName(_fromUtf8("nat0"))
        self.nat5.setStyleSheet("Text-align:left")
        self.nat5.clicked.connect(lambda: self.nation_objectives(self.nat_obj[self.natNation][5],5))
        self.gridLayout.addWidget(self.nat5, 11, 5,1,10)

        self.nat6 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.nat6.setFont(font)
        self.nat6.setObjectName(_fromUtf8("nat0"))
        self.nat6.setStyleSheet("Text-align:left")
        self.nat6.clicked.connect(lambda: self.nation_objectives(self.nat_obj[self.natNation][6],6))
        self.gridLayout.addWidget(self.nat6, 12, 5,1,10)

        self.nat7 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.nat7.setFont(font)
        self.nat7.setObjectName(_fromUtf8("nat0"))
        self.nat7.setStyleSheet("Text-align:left")
        self.nat7.clicked.connect(lambda: self.nation_objectives(self.nat_obj[self.natNation][7],7))
        self.gridLayout.addWidget(self.nat7, 13, 5,1,10)

        self.back = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.back.setFont(font)
        self.back.setObjectName(_fromUtf8("nat0"))
        self.back.setStyleSheet("Text-align:left")
        self.back.clicked.connect(lambda: self.nat_objectives_string_change(self.natNation,-1))
        self.gridLayout.addWidget(self.back, 14, 6, 1, 2)

        self.forward = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.forward.setFont(font)
        self.forward.setObjectName(_fromUtf8("nat0"))
        self.forward.setStyleSheet("Text-align:left")
        self.forward.clicked.connect(lambda: self.nat_objectives_string_change(self.natNation,1))
        self.gridLayout.addWidget(self.forward, 14, 13, 1, 2)

        self.natTotal = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(OBJ_FONT_SIZE)
        self.natTotal.setFont(font)
        self.natTotal.setObjectName(_fromUtf8("natTotal"))
        self.natTotal.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[self.natNation])))
        self.gridLayout.addWidget(self.natTotal, 14, 8, 1, 3)
    def nation_objectives(self,value,value_2):
        if value[0] == False:
            value[0] = True
            self.natTotalValue = self.natTotalValue + value[1]
            self.nChange[value_2].setStyleSheet('Text-align:left;background-color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[self.natNation])))
            self.natTotal.setText(_translate("MainWindow", str(self.NATION_NAME[self.natNation])+"|"+str(self.natTotalValue), None))
        #    self.nChange[value_2].setStyleSheet('Text-align:left')
        else:
            value[0] = False
            self.natTotalValue = self.natTotalValue - value[1]
            self.nChange[value_2].setStyleSheet('Text-align:left;background-color: rgb{}'.format(str(white)))
            self.natTotal.setText(_translate("MainWindow", str(self.NATION_NAME[self.natNation])+"|"+str(self.natTotalValue), None))
        #    self.nChange[value_2].setStyleSheet('Text-align:left')
    def nation_objectives_info(self):
        self.ger0 = [False,5,"At least one German land unit in Axis-Controlled Egypt"]
        self.ger1 = [False,5,"Germany controls Denmark and Norway"]
        self.ger2 = [False,5,"Germnay controls Volograd"]
        self.ger3 = [False,5,"Germany controls Caucasus"]
        self.ger4 = [False,5,"Germany controls Novgorod"]
        self.ger5 = [False,2,"Germany controls Iraq"]
        self.ger6 = [False,2,"Germany controls Perisa"]
        self.ger7 = [False,2,"Germany controls Northwest Perisa"]
        self.ger = [self.ger0,self.ger1,self.ger2,self.ger3,self.ger4,self.ger5,self.ger6,self.ger7]
        self.rus0 = [False,5,"Sea Zone 3 is free of Axis Warships, Archangel is controlled by USSR"]
        self.rus1 = [False,10,"Russia control Germany (One time use)"]
        self.rus2 = [False,3,"Japan and Russia are at peace. (Place 2 inf if you are defender)"]
        self.rus3 = [False,3,"Eech original German or Italian territory controoled by the USSR"]
        self.rus4 = [False,3,"Each original German or Italian territory controoled by the USSR"]
        self.rus5 = [False,3,"Each original German or Italian territory controoled by the USSR"]
        self.rus6 = [False,3,"Each original German or Italian territory controoled by the USSR"]
        self.rus7 = [False,3,"Each original German or Italian territory controoled by the USSR"]
        self.rus = [self.rus0,self.rus1,self.rus2,self.rus3,self.rus4,self.rus5,self.rus6,self.rus7]
        self.jap0 = [False,5,"The Axis control Western United States"]
        self.jap1 = [False,5,"The Axis control Midway, Wake Island, and Solomon Islands"]
        self.jap2 = [False,5,"The Axis control East Indies, Borneo, and Celebes"]
        self.jap3 = [False,5,"The Axis control India"]
        self.jap4 = [False,5,"The Axis control Honolulu"]
        self.jap5 = [False,5,"The Axis control Eastern Australia"]
        self.jap6 = [False,3,"The Axis Control the Philippines"]
        self.jap7 = [False,3,"Japan and Russia are at peace. (Place 2 inf if you are defender)"]
        self.jap = [self.jap0,self.jap1,self.jap2,self.jap3,self.jap4,self.jap5,self.jap6,self.jap7]
        self.ame0 = [False,5,"The US controls Mexico, East Mexico, Central America, West Indies"]
        self.ame1 = [False,5,"The US controls Eastern, Central, and Western United States"]
        self.ame2 = [False,3,"The US controls the Philippines"]
        self.ame3 = [False,5,"The US controls Hawaiian Islands, Alaska, Midway"]
        self.ame4 = [False,5,"There is at least one American Land unit in France"]
        self.ame5 = [False,0,""]
        self.ame6 = [False,0,""]
        self.ame7 = [False,0,""]
        self.ame = [self.ame0,self.ame1,self.ame2,self.ame3,self.ame4,self.ame5,self.ame6,self.ame7]
        self.chi0 = [False,6,"China controls the Burma road (can build artillery)"]
        self.chi1 = [False,0,""]
        self.chi2 = [False,0,""]
        self.chi3 = [False,0,""]
        self.chi4 = [False,0,""]
        self.chi5 = [False,0,""]
        self.chi6 = [False,0,""]
        self.chi7 = [False,0,""]
        self.chi = [self.chi0,self.chi1,self.chi2,self.chi3,self.chi4,self.chi5,self.chi6,self.chi7]
        self.bri0 = [False,5,"Britain controls all Original Territories in the European Theatre"]
        self.bri1 = [False,2,"Britain controls Persia and Iran"]
        self.bri2 = [False,2,"Britain control Trans-Jordan, Egypt and Alexandria"]
        self.bri3 = [False,0,""]
        self.bri4 = [False,0,""]
        self.bri5 = [False,0,""]
        self.bri6 = [False,0,""]
        self.bri7 = [False,0,""]
        self.bri = [self.bri0,self.bri1,self.bri2,self.bri3,self.bri4,self.bri5,self.bri6,self.bri7]
        self.ita0 = [False,2,"Italy controls Iraq"]
        self.ita1 = [False,2,"Italy controls Persia"]
        self.ita2 = [False,2,"Italy controls Northwest Persia"]
        self.ita3 = [False,5,"Italy controls Morocco, Algeria, Libya, Tobruk, Alexandria"]
        self.ita4 = [False,5,"There are no Allied Surface Warships in the Mediterranean Sea"]
        self.ita5 = [False,0,""]
        self.ita6 = [False,0,""]
        self.ita7 = [False,0,""]
        self.ita = [self.ita0,self.ita1,self.ita2,self.ita3,self.ita4,self.ita5,self.ita6,self.ita7]
        self.anz0 = [False,5,"ANZAC controls New Guinea, Solomon Islands, New Zealand"]
        self.anz1 = [False,5,"ANZAC controls all original territories"]
        self.anz2 = [False,5,"ANZAC controls Kwangtung and Malaya"]
        self.anz3 = [False,0,""]
        self.anz4 = [False,0,""]
        self.anz5 = [False,0,""]
        self.anz6 = [False,0,""]
        self.anz7 = [False,0,""]
        self.anz = [self.anz0,self.anz1,self.anz2,self.anz3,self.anz4,self.anz5,self.anz6,self.anz7]
        self.fra0 = [False,0,"France may place up to 12 IPC worth of troops when France is recaptured"]
        self.fra1 = [False,0,""]
        self.fra2 = [False,0,""]
        self.fra3 = [False,0,""]
        self.fra4 = [False,0,""]
        self.fra5 = [False,0,""]
        self.fra6 = [False,0,""]
        self.fra7 = [False,0,""]
        self.fra = [self.fra0,self.fra1,self.fra2,self.fra3,self.fra3,self.fra4,self.fra5,self.fra6,self.fra7]
        self.nat_obj = [self.ger,self.rus,self.jap,self.ame,self.chi,self.bri,self.ita,self.anz,self.fra]

    def set_colors(self):
        self.NATION_COLOR = [black,brown,orange,green,purple,beige,pink,grey,blue]
        self.NATION_COLOR_LIGHT = [light_black,light_brown,light_orange,light_green,light_purple,light_beige,light_pink,light_grey,light_blue]
        self.NATION_COLOR_ECO = [white,brown,orange,green,purple,beige,pink,grey,blue]
    def nation_turn_display(self):
        self.NT = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.NT.setFont(font)
        self.NT.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NT.setObjectName(_fromUtf8("NT"))
        self.gridLayout.addWidget(self.NT, 17, 2, 2, 8)
    def capitol_side_display(self):
        self.axis = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.axis.setFont(font)
        self.axis.setStyleSheet('color: rgb{}'.format(str(red)))
        self.axis.setObjectName(_fromUtf8("axis"))
        self.gridLayout.addWidget(self.axis, 13, 16, 1, 1)

        self.allies = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.allies.setFont(font)
        self.allies.setStyleSheet('color: rgb{}'.format(str(blue)))
        self.allies.setObjectName(_fromUtf8("axis"))
        self.gridLayout.addWidget(self.allies, 13, 17, 1, 1)

        self.victory = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.victory.setFont(font)
        self.victory.setStyleSheet('color: rgb{}'.format(str(black)))
        self.axis.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.victory.setObjectName(_fromUtf8("axis"))
        self.gridLayout.addWidget(self.victory, 13, 15, 3, 1)

        self.vDisplay = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.vDisplay.setFont(font)
        self.vDisplay.setObjectName(_fromUtf8("unit0"))
        self.vDisplay.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.vDisplay, 2, 5, 6, 9)
    def eco_display(self):
        self.german_eco()
        self.ussr_eco()
        self.japan_eco()
        self.china_eco()
        self.america_eco()
        self.britain_eco()
        self.italy_eco()
        self.anzac_eco()
        self.france_eco()
    def unit_display(self):
        self.unit_count()
        self.unit_stat()
        self.unit_name()

    def unit_count(self):
        self.count0 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count0.setFont(font)
        #self.count0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count0.setObjectName(_fromUtf8("GB"))
        self.count0.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.count0, 3, 1, 1, 1)

        self.count1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count1.setFont(font)
        #self.count1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count1.setObjectName(_fromUtf8("GB"))
        self.count1.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.count1, 4, 1, 1, 1)

        self.count2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count2.setFont(font)
        #self.count2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count2.setObjectName(_fromUtf8("GB"))
        self.count2.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.count2, 5, 1, 1, 1)

        self.count3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count3.setFont(font)
        #self.count3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count3.setObjectName(_fromUtf8("GB"))
        self.count3.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.count3, 6, 1, 1, 1)

        self.count4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count4.setFont(font)
        #self.count4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count4.setObjectName(_fromUtf8("GB"))
        self.count4.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.count4, 7, 1, 1, 1)

        self.count5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count5.setFont(font)
        #self.count5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count5.setObjectName(_fromUtf8("GB"))
        self.count5.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.count5, 8, 1, 1, 1)

        self.count6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count6.setFont(font)
        #self.count6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count6.setObjectName(_fromUtf8("GB"))
        self.count6.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.count6, 9, 1, 1, 1)

        self.count7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count7.setFont(font)
        #self.count7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count7.setObjectName(_fromUtf8("GB"))
        self.count7.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.count7, 10, 1, 1, 1)

        self.count8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count8.setFont(font)
        #self.count8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count8.setObjectName(_fromUtf8("GB"))
        self.count8.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.count8, 11, 1, 1, 1)

        self.count9 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count9.setFont(font)
        #self.count9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count9.setObjectName(_fromUtf8("GB"))
        self.count9.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.count9, 12, 1, 1, 1)

        self.count10 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count10.setFont(font)
        #self.count10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count10.setObjectName(_fromUtf8("GB"))
        self.count10.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.count10, 13, 1, 1, 1)

        self.count11 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count11.setFont(font)
        #self.count11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count11.setObjectName(_fromUtf8("GB"))
        self.count11.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.count11, 14, 1, 1, 1)

        self.count12 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count12.setFont(font)
        #self.count12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count12.setObjectName(_fromUtf8("GB"))
        self.count12.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.count12, 15, 1, 1, 1)

        self.count13 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count13.setFont(font)
        #self.count13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count13.setObjectName(_fromUtf8("GB"))
        self.count13.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.count13, 16, 1, 1, 1)

        self.count14 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.count14.setFont(font)
        #self.count14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count14.setObjectName(_fromUtf8("GB"))
        self.count14.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.count14, 17, 1, 1, 1)
    def unit_stat(self):
        self.info = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.info.setFont(font)
        #self.info.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.info.setObjectName(_fromUtf8("ingo"))
        self.info.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.info, 2, 3, 1, 3)

        self.unit0 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit0.setFont(font)
        #self.unit0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit0.setObjectName(_fromUtf8("unit0"))
        self.unit0.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.unit0, 3, 3, 1, 2)

        self.unit1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit1.setFont(font)
        #self.unit1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit1.setObjectName(_fromUtf8("unit0"))
        self.unit1.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.unit1, 4, 3, 1, 2)

        self.unit2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit2.setFont(font)
        #self.unit2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit2.setObjectName(_fromUtf8("unit0"))
        self.unit2.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.unit2, 5, 3, 1, 2)

        self.unit3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit3.setFont(font)
        #self.unit3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit3.setObjectName(_fromUtf8("unit0"))
        self.unit3.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.unit3, 6, 3, 1, 2)

        self.unit4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit4.setFont(font)
        #self.unit4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit4.setObjectName(_fromUtf8("unit0"))
        self.unit4.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.unit4, 7, 3, 1, 2)

        self.unit5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit5.setFont(font)
        #self.unit5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit5.setObjectName(_fromUtf8("unit0"))
        self.unit5.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.unit5, 8, 3, 1, 2)

        self.unit6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit6.setFont(font)
        #self.unit6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit6.setObjectName(_fromUtf8("unit0"))
        self.unit6.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.unit6, 9, 3, 1, 2)

        self.unit7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit7.setFont(font)
        #self.unit7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit7.setObjectName(_fromUtf8("unit0"))
        self.unit7.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.unit7, 10, 3, 1, 2)

        self.unit8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit8.setFont(font)
        #self.unit8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit8.setObjectName(_fromUtf8("unit0"))
        self.unit8.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.unit8, 11, 3, 1, 2)

        self.unit9 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit9.setFont(font)
        #self.unit9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit9.setObjectName(_fromUtf8("unit0"))
        self.unit9.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.unit9, 12, 3, 1, 2)

        self.unit10 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit10.setFont(font)
        #self.unit10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit10.setObjectName(_fromUtf8("unit0"))
        self.unit10.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.unit10, 13, 3, 1, 2)

        self.unit11 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit11.setFont(font)
        #self.unit11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit11.setObjectName(_fromUtf8("unit0"))
        self.unit11.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.unit11, 14, 3, 1, 2)

        self.unit12 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit12.setFont(font)
        #self.unit12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit12.setObjectName(_fromUtf8("unit0"))
        self.unit12.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.unit12, 15, 3, 1, 2)

        self.unit13 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit13.setFont(font)
        #self.unit13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit13.setObjectName(_fromUtf8("unit0"))
        self.unit13.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.unit13, 16, 3, 1, 2)

        self.unit14 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.unit14.setFont(font)
        #self.unit14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unit14.setObjectName(_fromUtf8("unit0"))
        self.unit14.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.unit14, 17, 3, 1, 2)
    def unit_name(self):
        self.name0 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name0.setFont(font)
        self.name0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name0.setObjectName(_fromUtf8("unit0"))
        self.name0.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.name0, 3, 1, 1, 2)

        self.name1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name1.setFont(font)
        self.name1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name1.setObjectName(_fromUtf8("unit0"))
        self.name1.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.name1, 4, 1, 1, 2)

        self.name2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE-3)
        self.name2.setFont(font)
        self.name2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name2.setObjectName(_fromUtf8("unit0"))
        self.name2.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.name2, 5, 1, 1, 2)

        self.name3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name3.setFont(font)
        self.name3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name3.setObjectName(_fromUtf8("unit0"))
        self.name3.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.name3, 6, 1, 1, 2)

        self.name4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name4.setFont(font)
        self.name4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name4.setObjectName(_fromUtf8("unit0"))
        self.name4.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.name4, 7, 1, 1, 2)

        self.name5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name5.setFont(font)
        self.name5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name5.setObjectName(_fromUtf8("unit0"))
        self.name5.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.name5, 8, 1, 1, 2)

        self.name6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name6.setFont(font)
        self.name6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name6.setObjectName(_fromUtf8("unit0"))
        self.name6.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.name6, 9, 1, 1, 2)

        self.name7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE-4)
        self.name7.setFont(font)
        self.name7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name7.setObjectName(_fromUtf8("unit0"))
        self.name7.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.name7, 10, 1, 1, 2)

        self.name8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name8.setFont(font)
        self.name8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name8.setObjectName(_fromUtf8("unit0"))
        self.name8.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.name8, 11, 1, 1, 2)

        self.name9 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name9.setFont(font)
        self.name9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name9.setObjectName(_fromUtf8("unit0"))
        self.name9.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.name9, 12, 1, 1, 2)

        self.name10 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name10.setFont(font)
        self.name10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name10.setObjectName(_fromUtf8("unit0"))
        self.name10.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.name10, 13, 1, 1, 2)

        self.name11 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name11.setFont(font)
        self.name11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name11.setObjectName(_fromUtf8("unit0"))
        self.name11.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.name11, 14, 1, 1, 2)

        self.name12 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name12.setFont(font)
        self.name12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name12.setObjectName(_fromUtf8("unit0"))
        self.name12.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.name12, 15, 1, 1, 2)

        self.name13 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE-4)
        self.name13.setFont(font)
        self.name13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name13.setObjectName(_fromUtf8("unit0"))
        self.name13.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_2)))
        self.gridLayout.addWidget(self.name13, 16, 1, 1, 2)

        self.name14 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UNIT_FONT_SIZE)
        self.name14.setFont(font)
        self.name14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name14.setObjectName(_fromUtf8("unit0"))
        self.name14.setStyleSheet('color: rgb{}'.format(str(UNIT_COLOR_1)))
        self.gridLayout.addWidget(self.name14, 17, 1, 1, 2)
    def german_eco(self):
        self.GB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.GB.setFont(font)
        self.GB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GB.setObjectName(_fromUtf8("GB"))
        self.GB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[0])))
        self.gridLayout.addWidget(self.GB, 1, 0, 1, 1)
        self.GI = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.GI.setFont(font)
        self.GI.setObjectName(_fromUtf8("GI"))
        self.GI.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[0])))
        self.gridLayout.addWidget(self.GI, 1, 1, 1, 1)
    def ussr_eco(self):
        self.UB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.UB.setFont(font)
        self.UB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.UB.setObjectName(_fromUtf8("UB"))
        self.UB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[1])))
        self.gridLayout.addWidget(self.UB, 1, 2, 1, 1)
        self.UI = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.UI.setFont(font)
        self.UI.setObjectName(_fromUtf8("UI"))
        self.UI.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[1])))
        self.gridLayout.addWidget(self.UI, 1, 3, 1, 1)
    def japan_eco(self):
        self.JB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.JB.setFont(font)
        self.JB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.JB.setObjectName(_fromUtf8("JB"))
        self.JB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[2])))
        self.gridLayout.addWidget(self.JB, 1, 4, 1, 1)
        self.JI = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.JI.setFont(font)
        self.JI.setObjectName(_fromUtf8("JI"))
        self.JI.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[2])))
        self.gridLayout.addWidget(self.JI, 1, 5, 1, 1)
    def america_eco(self):
        self.AB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.AB.setFont(font)
        self.AB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AB.setObjectName(_fromUtf8("AB"))
        self.AB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[3])))
        self.gridLayout.addWidget(self.AB, 1, 6, 1, 1)
        self.AI = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.AI.setFont(font)
        self.AI.setObjectName(_fromUtf8("AI"))
        self.AI.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[3])))
        self.gridLayout.addWidget(self.AI, 1, 7, 1, 1)
    def china_eco(self):
        self.CB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.CB.setFont(font)
        self.CB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CB.setObjectName(_fromUtf8("CB"))
        self.CB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[4])))
        self.gridLayout.addWidget(self.CB, 1, 8, 1, 1)
        self.CI = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.CI.setFont(font)
        self.CI.setObjectName(_fromUtf8("CI"))
        self.CI.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[4])))
        self.gridLayout.addWidget(self.CI, 1, 9, 1, 1)
    def britain_eco(self):
        self.BB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.BB.setFont(font)
        self.BB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BB.setObjectName(_fromUtf8("BB"))
        self.BB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[5])))
        self.gridLayout.addWidget(self.BB, 1, 10, 1, 1)
        self.BI = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.BI.setFont(font)
        self.BI.setObjectName(_fromUtf8("BI"))
        self.BI.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[5])))
        self.gridLayout.addWidget(self.BI, 1, 11, 1, 1)
    def italy_eco(self):
        self.IB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.IB.setFont(font)
        self.IB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IB.setObjectName(_fromUtf8("IB"))
        self.IB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[6])))
        self.gridLayout.addWidget(self.IB, 1, 12, 1, 1)
        self.II = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.II.setFont(font)
        self.II.setObjectName(_fromUtf8("II"))
        self.II.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[6])))
        self.gridLayout.addWidget(self.II, 1, 13, 1, 1)
    def anzac_eco(self):
        self.NB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.NB.setFont(font)
        self.NB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NB.setObjectName(_fromUtf8("NB"))
        self.NB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[7])))
        self.gridLayout.addWidget(self.NB, 1, 14, 1, 1)
        self.NI = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.NI.setFont(font)
        self.NI.setObjectName(_fromUtf8("NI"))
        self.NI.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[7])))
        self.gridLayout.addWidget(self.NI, 1, 15, 1, 1)
    def france_eco(self):
        self.FB = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.FB.setFont(font)
        self.FB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FB.setObjectName(_fromUtf8("FB"))
        self.FB.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[8])))
        self.gridLayout.addWidget(self.FB, 1, 16, 1, 1)
        self.FI = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(ECO_FONT_SIZE)
        self.FI.setFont(font)
        self.FI.setObjectName(_fromUtf8("FI"))
        self.FI.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR_LIGHT[8])))
        self.gridLayout.addWidget(self.FI, 1, 17, 1, 1)
    def nation_names(self):
        self.germany = QtGui.QLabel(self.centralwidget)
        self.germany.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.germany.setFont(font)
        self.germany.setLineWidth(1)
        self.germany.setAlignment(QtCore.Qt.AlignCenter)
        self.germany.setObjectName(_fromUtf8("germany"))
        self.germany.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[0])))
        self.gridLayout.addWidget(self.germany, 0, 0, 1, 2)

        self.ussr = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.ussr.setFont(font)
        self.ussr.setAlignment(QtCore.Qt.AlignCenter)
        self.ussr.setObjectName(_fromUtf8("ussr"))
        self.ussr.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[1])))
        self.gridLayout.addWidget(self.ussr, 0, 2, 1, 2)

        self.japan = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.japan.setFont(font)
        self.japan.setAlignment(QtCore.Qt.AlignCenter)
        self.japan.setObjectName(_fromUtf8("japan"))
        self.japan.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[2])))
        self.gridLayout.addWidget(self.japan, 0, 4, 1, 2)

        self.america = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.america.setFont(font)
        self.america.setAlignment(QtCore.Qt.AlignCenter)
        self.america.setObjectName(_fromUtf8("america"))
        self.america.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[3])))
        self.gridLayout.addWidget(self.america, 0, 6, 1, 2)

        self.china = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.china.setFont(font)
        self.china.setAlignment(QtCore.Qt.AlignCenter)
        self.china.setObjectName(_fromUtf8("china"))
        self.china.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[4])))
        self.gridLayout.addWidget(self.china, 0, 8, 1, 2)

        self.britain = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.britain.setFont(font)
        self.britain.setAlignment(QtCore.Qt.AlignCenter)
        self.britain.setObjectName(_fromUtf8("britain"))
        self.britain.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[5])))
        self.gridLayout.addWidget(self.britain, 0, 10, 1, 2)

        self.italy = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.italy.setFont(font)
        self.italy.setAlignment(QtCore.Qt.AlignCenter)
        self.italy.setObjectName(_fromUtf8("italy"))
        self.italy.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[6])))
        self.gridLayout.addWidget(self.italy, 0, 12, 1, 2)

        self.anzac = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.anzac.setFont(font)
        self.anzac.setAlignment(QtCore.Qt.AlignCenter)
        self.anzac.setObjectName(_fromUtf8("anzac"))
        self.anzac.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[7])))
        self.gridLayout.addWidget(self.anzac, 0, 14, 1, 2)

        self.france = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(FONT_SIZE)
        self.france.setFont(font)
        self.france.setAlignment(QtCore.Qt.AlignCenter)
        self.france.setObjectName(_fromUtf8("france"))
        self.france.setStyleSheet('color: rgb{}'.format(str(self.NATION_COLOR[8])))
        self.gridLayout.addWidget(self.france, 0, 16, 1, 2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.germany.setText(_translate("MainWindow", "Germany", None))
        self.GB.setText(_translate("MainWindow", str(self.bank[0]), None))
        self.GI.setText(_translate("MainWindow", str(self.income[0]), None))
        self.ussr.setText(_translate("MainWindow", "USSR", None))
        self.UB.setText(_translate("MainWindow", str(self.bank[1]), None))
        self.UI.setText(_translate("MainWindow", str(self.income[1]), None))
        self.japan.setText(_translate("MainWindow", "Japan", None))
        self.JB.setText(_translate("MainWindow", str(self.bank[2]), None))
        self.JI.setText(_translate("MainWindow", str(self.income[2]), None))
        self.america.setText(_translate("MainWindow", "America", None))
        self.AB.setText(_translate("MainWindow", str(self.bank[3]), None))
        self.AI.setText(_translate("MainWindow", str(self.income[3]), None))
        self.china.setText(_translate("MainWindow", "China", None))
        self.CB.setText(_translate("MainWindow", str(self.bank[4]), None))
        self.CI.setText(_translate("MainWindow", str(self.income[4]), None))
        self.britain.setText(_translate("MainWindow", "Britain", None))
        self.BB.setText(_translate("MainWindow", str(self.bank[5]), None))
        self.BI.setText(_translate("MainWindow", str(self.income[5]), None))
        self.italy.setText(_translate("MainWindow", "Italy", None))
        self.IB.setText(_translate("MainWindow", str(self.bank[6]), None))
        self.II.setText(_translate("MainWindow", str(self.income[6]), None))
        self.anzac.setText(_translate("MainWindow", "ANZAC", None))
        self.NB.setText(_translate("MainWindow", str(self.bank[7]), None))
        self.NI.setText(_translate("MainWindow", str(self.income[7]), None))
        self.france.setText(_translate("MainWindow", "France", None))
        self.FB.setText(_translate("MainWindow", str(self.bank[8]), None))
        self.FI.setText(_translate("MainWindow", str(self.income[8]), None))

        self.plus1B.setText(_translate("MainWindow", "+1", None))
        self.plus5B.setText(_translate("MainWindow", "+5", None))
        self.minus1B.setText(_translate("MainWindow", "-1", None))
        self.minus5B.setText(_translate("MainWindow", "-5", None))
        self.plus1I.setText(_translate("MainWindow", "+1", None))
        self.plus5I.setText(_translate("MainWindow", "+5", None))
        self.minus1I.setText(_translate("MainWindow", "-1", None))
        self.minus5I.setText(_translate("MainWindow", "-5", None))

        self.inf.setText(_translate("MainWindow", "3", None))
        self.art.setText(_translate("MainWindow", "4", None))
        self.mbl.setText(_translate("MainWindow", "4", None))
        self.tnk.setText(_translate("MainWindow", "6", None))
        self.atk.setText(_translate("MainWindow", "6", None))
        self.aaa.setText(_translate("MainWindow", "5", None))
        self.fgh.setText(_translate("MainWindow", "10", None))
        self.tct.setText(_translate("MainWindow", "11", None))
        self.bmb.setText(_translate("MainWindow", "12", None))
        self.sub.setText(_translate("MainWindow", "8", None))
        self.trn.setText(_translate("MainWindow", "8", None))
        self.dst.setText(_translate("MainWindow", "8", None))
        self.crs.setText(_translate("MainWindow", "12", None))
        self.acc.setText(_translate("MainWindow", "16", None))
        self.btl.setText(_translate("MainWindow", "20", None))

        self.info.setText(_translate("MainWindow", "A D M C", None))
        self.unit0.setText(_translate("MainWindow", str(self.unitStat[0]), None))
        self.unit1.setText(_translate("MainWindow", str(self.unitStat[1]), None))
        self.unit2.setText(_translate("MainWindow", str(self.unitStat[2]), None))
        self.unit3.setText(_translate("MainWindow", str(self.unitStat[3]), None))
        self.unit4.setText(_translate("MainWindow", str(self.unitStat[4]), None))
        self.unit5.setText(_translate("MainWindow", str(self.unitStat[5]), None))
        self.unit6.setText(_translate("MainWindow", str(self.unitStat[6]), None))
        self.unit7.setText(_translate("MainWindow", str(self.unitStat[7]), None))
        self.unit8.setText(_translate("MainWindow", str(self.unitStat[8]), None))
        self.unit9.setText(_translate("MainWindow", str(self.unitStat[9]), None))
        self.unit10.setText(_translate("MainWindow", str(self.unitStat[10]), None))
        self.unit11.setText(_translate("MainWindow", str(self.unitStat[11]), None))
        self.unit12.setText(_translate("MainWindow", str(self.unitStat[12]), None))
        self.unit13.setText(_translate("MainWindow", str(self.unitStat[13]), None))
        self.unit14.setText(_translate("MainWindow", str(self.unitStat[14]), None))

        self.name0.setText(_translate("MainWindow", str(self.UNIT_NAME[0]), None))
        self.name1.setText(_translate("MainWindow", str(self.UNIT_NAME[1]), None))
        self.name2.setText(_translate("MainWindow", str(self.UNIT_NAME[2]), None))
        self.name3.setText(_translate("MainWindow", str(self.UNIT_NAME[3]), None))
        self.name4.setText(_translate("MainWindow", str(self.UNIT_NAME[4]), None))
        self.name5.setText(_translate("MainWindow", str(self.UNIT_NAME[5]), None))
        self.name6.setText(_translate("MainWindow", str(self.UNIT_NAME[6]), None))
        self.name7.setText(_translate("MainWindow", str(self.UNIT_NAME[7]), None))
        self.name8.setText(_translate("MainWindow", str(self.UNIT_NAME[8]), None))
        self.name9.setText(_translate("MainWindow", str(self.UNIT_NAME[9]), None))
        self.name10.setText(_translate("MainWindow", str(self.UNIT_NAME[10]), None))
        self.name11.setText(_translate("MainWindow", str(self.UNIT_NAME[11]), None))
        self.name12.setText(_translate("MainWindow", str(self.UNIT_NAME[12]), None))
        self.name13.setText(_translate("MainWindow", str(self.UNIT_NAME[13]), None))
        self.name14.setText(_translate("MainWindow", str(self.UNIT_NAME[14]), None))

        self.count0.setText(_translate("MainWindow", str(self.count[0]), None))
        self.count1.setText(_translate("MainWindow", str(self.count[1]), None))
        self.count2.setText(_translate("MainWindow", str(self.count[2]), None))
        self.count3.setText(_translate("MainWindow", str(self.count[3]), None))
        self.count4.setText(_translate("MainWindow", str(self.count[4]), None))
        self.count5.setText(_translate("MainWindow", str(self.count[5]), None))
        self.count6.setText(_translate("MainWindow", str(self.count[6]), None))
        self.count7.setText(_translate("MainWindow", str(self.count[7]), None))
        self.count8.setText(_translate("MainWindow", str(self.count[8]), None))
        self.count9.setText(_translate("MainWindow", str(self.count[9]), None))
        self.count10.setText(_translate("MainWindow", str(self.count[10]), None))
        self.count11.setText(_translate("MainWindow", str(self.count[11]), None))
        self.count12.setText(_translate("MainWindow", str(self.count[12]), None))
        self.count13.setText(_translate("MainWindow", str(self.count[13]), None))
        self.count14.setText(_translate("MainWindow", str(self.count[14]), None))

        self.nat0.setText(_translate("MainWindow", str(self.nat_obj[0][0][1])+"|"+str(self.nat_obj[0][0][2]), None))
        self.nat1.setText(_translate("MainWindow", str(self.nat_obj[0][1][1])+"|"+str(self.nat_obj[0][1][2]), None))
        self.nat2.setText(_translate("MainWindow", str(self.nat_obj[0][2][1])+"|"+str(self.nat_obj[0][2][2]), None))
        self.nat3.setText(_translate("MainWindow", str(self.nat_obj[0][3][1])+"|"+str(self.nat_obj[0][3][2]), None))
        self.nat4.setText(_translate("MainWindow", str(self.nat_obj[0][4][1])+"|"+str(self.nat_obj[0][4][2]), None))
        self.nat5.setText(_translate("MainWindow", str(self.nat_obj[0][5][1])+"|"+str(self.nat_obj[0][5][2]), None))
        self.nat6.setText(_translate("MainWindow", str(self.nat_obj[0][6][1])+"|"+str(self.nat_obj[0][6][2]), None))
        self.nat7.setText(_translate("MainWindow", str(self.nat_obj[0][7][1])+"|"+str(self.nat_obj[0][7][2]), None))

        self.forward.setText(_translate("MainWindow", "forwards", None))
        self.back.setText(_translate("MainWindow", "backwards", None))
        self.natTotal.setText(_translate("MainWindow", str(self.NATION_NAME[0])+"|"+str(self.natTotalValue), None))


        self.axis.setText(_translate("MainWindow", "Axis", None))
        self.allies.setText(_translate("MainWindow", "Allies", None))
        self.vDisplay.setText(_translate("MainWindow", "", None))
        self.victory.setText(_translate("MainWindow", "Victory \n   " + str(self.CAPITOL_VICTORY), None))

        self.axisCapitolsBUTTON.setText(_translate("MainWindow", str(self.axis_capitols), None))
        self.alliesCapitolsBUTTON.setText(_translate("MainWindow", str(self.allies_capitols), None))
        self.resetBuyBUTTON.setText(_translate("MainWindow", "Reset Unit Buy", None))
        self.endTurnButton.setText(_translate("MainWindow", "End \n Turn", None))
        self.changeEcoButton.setText(_translate("MainWindow", "B "+str(self.bank[self.ecoNation])+"|"+str(self.NATION_NAME[self.ecoNation])+"|"+str(self.income[self.ecoNation])+" I", None))
        self.NT.setText(_translate("MainWindow", str(self.NATION_NAME[self.nation])+"|"+str(self.turn), None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    app.setActiveWindow(MainWindow)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
