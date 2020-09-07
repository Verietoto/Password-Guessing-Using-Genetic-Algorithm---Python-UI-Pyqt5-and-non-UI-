"""
Hello World!!! This is a free python code of Genetic Algorithm method for word guessing problem, i made GUI Version
and nonGUI Version just it cas you guys are eager too learn about the parameters and how it affect the others.
You can use this as your reference, but dont use for commercial use.

Contact Me:

Email:      Verietoto@gmail.com
Linkedin:   www.linkedin.com/in/ketut-toto-suryahadinata-2755a9b0

"""
from PyQt5 import QtCore, QtGui, QtWidgets

import UI.Screen.resource_rc
class GeneticWindow_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 667)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 600))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setMinimumSize(QtCore.QSize(700, 600))
        self.mainFrame.setStyleSheet("QFrame#mainFrame{\n"
"    \n"
"    border-image: url(:/newPrefix/mainFrame.png);\n"
"}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setContentsMargins(20, 50, 20, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logoFrame = QtWidgets.QFrame(self.mainFrame)
        self.logoFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.logoFrame.setMaximumSize(QtCore.QSize(100000, 100000))
        self.logoFrame.setStyleSheet("QFrame#logoFrame{\n"
"    border: None;\n"
"}")
        self.logoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logoFrame.setObjectName("logoFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.logoFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(518, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.wordGuessingLogo = QtWidgets.QLabel(self.logoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordGuessingLogo.sizePolicy().hasHeightForWidth())
        self.wordGuessingLogo.setSizePolicy(sizePolicy)
        self.wordGuessingLogo.setMaximumSize(QtCore.QSize(250, 100))
        self.wordGuessingLogo.setText("")
        self.wordGuessingLogo.setPixmap(QtGui.QPixmap("Background/WORDGUESSER.png"))
        self.wordGuessingLogo.setScaledContents(True)
        self.wordGuessingLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.wordGuessingLogo.setIndent(-1)
        self.wordGuessingLogo.setObjectName("wordGuessingLogo")
        self.horizontalLayout_4.addWidget(self.wordGuessingLogo)
        self.verticalLayout.addWidget(self.logoFrame, 0, QtCore.Qt.AlignTop)
        self.contentFrame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy)
        self.contentFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.contentFrame.setMaximumSize(QtCore.QSize(16777215, 600))
        self.contentFrame.setStyleSheet("QFrame#contentFrame{\n"
"\n"
"border:None;\n"
"}")
        self.contentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFrame.setObjectName("contentFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.contentFrame)
        self.verticalLayout_2.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bestFintessScore = QtWidgets.QLabel(self.contentFrame)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(24)
        self.bestFintessScore.setFont(font)
        self.bestFintessScore.setStyleSheet("color:rgb(62, 191, 191)")
        self.bestFintessScore.setObjectName("bestFintessScore")
        self.verticalLayout_2.addWidget(self.bestFintessScore)
        self.bestFintessScore_2 = QtWidgets.QLabel(self.contentFrame)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(24)
        self.bestFintessScore_2.setFont(font)
        self.bestFintessScore_2.setStyleSheet("color:rgb(62, 191, 191)")
        self.bestFintessScore_2.setObjectName("bestFintessScore_2")
        self.verticalLayout_2.addWidget(self.bestFintessScore_2)
        self.frame_4 = QtWidgets.QFrame(self.contentFrame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.parent1 = QtWidgets.QLabel(self.frame_4)
        self.parent1.setGeometry(QtCore.QRect(20, 20, 141, 17))
        self.parent1.setStyleSheet("color:white;\n"
"")
        self.parent1.setObjectName("parent1")
        self.parent3 = QtWidgets.QLabel(self.frame_4)
        self.parent3.setGeometry(QtCore.QRect(350, 20, 141, 17))
        self.parent3.setStyleSheet("color:white;\n"
"")
        self.parent3.setObjectName("parent3")
        self.parent6 = QtWidgets.QLabel(self.frame_4)
        self.parent6.setGeometry(QtCore.QRect(20, 150, 141, 17))
        self.parent6.setStyleSheet("color:white;\n"
"")
        self.parent6.setObjectName("parent6")
        self.parent2 = QtWidgets.QLabel(self.frame_4)
        self.parent2.setGeometry(QtCore.QRect(160, 20, 141, 17))
        self.parent2.setStyleSheet("color:white;\n"
"")
        self.parent2.setObjectName("parent2")
        self.parent4 = QtWidgets.QLabel(self.frame_4)
        self.parent4.setGeometry(QtCore.QRect(550, 20, 141, 17))
        self.parent4.setStyleSheet("color:white;\n"
"")
        self.parent4.setObjectName("parent4")
        self.parent5 = QtWidgets.QLabel(self.frame_4)
        self.parent5.setGeometry(QtCore.QRect(720, 20, 141, 17))
        self.parent5.setStyleSheet("color:white;\n"
"")
        self.parent5.setObjectName("parent5")
        self.parent7 = QtWidgets.QLabel(self.frame_4)
        self.parent7.setGeometry(QtCore.QRect(160, 150, 141, 17))
        self.parent7.setStyleSheet("color:white;\n"
"")
        self.parent7.setObjectName("parent7")
        self.parent8 = QtWidgets.QLabel(self.frame_4)
        self.parent8.setGeometry(QtCore.QRect(350, 150, 141, 17))
        self.parent8.setStyleSheet("color:white;\n"
"")
        self.parent8.setObjectName("parent8")
        self.parent9 = QtWidgets.QLabel(self.frame_4)
        self.parent9.setGeometry(QtCore.QRect(550, 150, 141, 17))
        self.parent9.setStyleSheet("color:white;\n"
"")
        self.parent9.setObjectName("parent9")
        self.parent10 = QtWidgets.QLabel(self.frame_4)
        self.parent10.setGeometry(QtCore.QRect(730, 150, 141, 17))
        self.parent10.setStyleSheet("color:white;\n"
"")
        self.parent10.setObjectName("parent10")
        self.fitness1 = QtWidgets.QLabel(self.frame_4)
        self.fitness1.setGeometry(QtCore.QRect(20, 50, 141, 17))
        self.fitness1.setStyleSheet("color:white;\n"
"")
        self.fitness1.setObjectName("fitness1")
        self.fitness2 = QtWidgets.QLabel(self.frame_4)
        self.fitness2.setGeometry(QtCore.QRect(160, 50, 141, 17))
        self.fitness2.setStyleSheet("color:white;\n"
"")
        self.fitness2.setObjectName("fitness2")
        self.fitness3 = QtWidgets.QLabel(self.frame_4)
        self.fitness3.setGeometry(QtCore.QRect(350, 50, 140, 17))
        self.fitness3.setStyleSheet("color:white;\n"
"")
        self.fitness3.setObjectName("fitness3")
        self.fitness4 = QtWidgets.QLabel(self.frame_4)
        self.fitness4.setGeometry(QtCore.QRect(550, 50, 141, 17))
        self.fitness4.setStyleSheet("color:white;\n"
"")
        self.fitness4.setObjectName("fitness4")
        self.fitness5 = QtWidgets.QLabel(self.frame_4)
        self.fitness5.setGeometry(QtCore.QRect(720, 50, 141, 17))
        self.fitness5.setStyleSheet("color:white;\n"
"")
        self.fitness5.setObjectName("fitness5")
        self.fitness6 = QtWidgets.QLabel(self.frame_4)
        self.fitness6.setGeometry(QtCore.QRect(20, 180, 141, 17))
        self.fitness6.setStyleSheet("color:white;\n"
"")
        self.fitness6.setObjectName("fitness6")
        self.fitness7 = QtWidgets.QLabel(self.frame_4)
        self.fitness7.setGeometry(QtCore.QRect(160, 180, 141, 17))
        self.fitness7.setStyleSheet("color:white;\n"
"")
        self.fitness7.setObjectName("fitness7")
        self.fitness8 = QtWidgets.QLabel(self.frame_4)
        self.fitness8.setGeometry(QtCore.QRect(350, 180, 141, 17))
        self.fitness8.setStyleSheet("color:white;\n"
"")
        self.fitness8.setObjectName("fitness8")
        self.fitness9 = QtWidgets.QLabel(self.frame_4)
        self.fitness9.setGeometry(QtCore.QRect(550, 180, 141, 17))
        self.fitness9.setStyleSheet("color:white;\n"
"")
        self.fitness9.setObjectName("fitness9")
        self.fitness10 = QtWidgets.QLabel(self.frame_4)
        self.fitness10.setGeometry(QtCore.QRect(730, 180, 141, 17))
        self.fitness10.setStyleSheet("color:white;\n"
"")
        self.fitness10.setObjectName("fitness10")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 7)
        self.bestFintessScore.raise_()
        self.bestFintessScore_2.raise_()
        self.frame_4.raise_()
        self.verticalLayout.addWidget(self.contentFrame)
        self.windgedFrame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windgedFrame.sizePolicy().hasHeightForWidth())
        self.windgedFrame.setSizePolicy(sizePolicy)
        self.windgedFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.windgedFrame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.windgedFrame.setStyleSheet("QFrame{\n"
"\n"
"border:None;\n"
"}")
        self.windgedFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windgedFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windgedFrame.setObjectName("windgedFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windgedFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.windgedFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setSizeIncrement(QtCore.QSize(2, 2))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.MRNumber = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.MRNumber.setFont(font)
        self.MRNumber.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    \n"
"\n"
"}")
        self.MRNumber.setObjectName("MRNumber")
        self.gridLayout.addWidget(self.MRNumber, 0, 2, 1, 1)
        self.crossOverRateTX_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crossOverRateTX_2.sizePolicy().hasHeightForWidth())
        self.crossOverRateTX_2.setSizePolicy(sizePolicy)
        self.crossOverRateTX_2.setMinimumSize(QtCore.QSize(0, 20))
        self.crossOverRateTX_2.setMaximumSize(QtCore.QSize(50, 20))
        self.crossOverRateTX_2.setStyleSheet("color:Black;")
        self.crossOverRateTX_2.setObjectName("crossOverRateTX_2")
        self.gridLayout.addWidget(self.crossOverRateTX_2, 1, 0, 1, 1)
        self.parentNumber_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parentNumber_2.sizePolicy().hasHeightForWidth())
        self.parentNumber_2.setSizePolicy(sizePolicy)
        self.parentNumber_2.setMaximumSize(QtCore.QSize(50, 20))
        self.parentNumber_2.setStyleSheet("color:Black;")
        self.parentNumber_2.setObjectName("parentNumber_2")
        self.gridLayout.addWidget(self.parentNumber_2, 3, 0, 1, 1)
        self.numberParentSlider_2 = QtWidgets.QSlider(self.frame)
        self.numberParentSlider_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.numberParentSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 3px solid;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    ;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 188, 191, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: yellow;\n"
"    border: 1px solid;\n"
"    height: 4px;\n"
"    width: 12px;\n"
"    margin: -5px 0px;\n"
"    }")
        self.numberParentSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.numberParentSlider_2.setObjectName("numberParentSlider_2")
        self.gridLayout.addWidget(self.numberParentSlider_2, 2, 1, 2, 1)
        self.crossOverRateSlider_2 = QtWidgets.QSlider(self.frame)
        self.crossOverRateSlider_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.crossOverRateSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 3px solid;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    ;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(127, 191, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: yellow;\n"
"    border: 1px solid;\n"
"    height: 4px;\n"
"    width: 12px;\n"
"    margin: -5px 0px;\n"
"    }")
        self.crossOverRateSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.crossOverRateSlider_2.setObjectName("crossOverRateSlider_2")
        self.gridLayout.addWidget(self.crossOverRateSlider_2, 0, 1, 1, 1)
        self.mutationRateSlider_2 = QtWidgets.QSlider(self.frame)
        self.mutationRateSlider_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.mutationRateSlider_2.setSizeIncrement(QtCore.QSize(2, 2))
        self.mutationRateSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 3px solid;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    ;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 191, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: yellow;\n"
"    border: 1px solid;\n"
"    height: 4px;\n"
"    width: 12px;\n"
"    margin: -5px 0px;\n"
"    }")
        self.mutationRateSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.mutationRateSlider_2.setObjectName("mutationRateSlider_2")
        self.gridLayout.addWidget(self.mutationRateSlider_2, 1, 1, 1, 1)
        self.mutationRateText_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mutationRateText_2.sizePolicy().hasHeightForWidth())
        self.mutationRateText_2.setSizePolicy(sizePolicy)
        self.mutationRateText_2.setMaximumSize(QtCore.QSize(40, 20))
        self.mutationRateText_2.setStyleSheet("color:Black;")
        self.mutationRateText_2.setObjectName("mutationRateText_2")
        self.gridLayout.addWidget(self.mutationRateText_2, 0, 0, 1, 1)
        self.CORNumber = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CORNumber.setFont(font)
        self.CORNumber.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    \n"
"\n"
"}")
        self.CORNumber.setObjectName("CORNumber")
        self.gridLayout.addWidget(self.CORNumber, 1, 2, 2, 1)
        self.NPNumber = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.NPNumber.setFont(font)
        self.NPNumber.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    \n"
"\n"
"}")
        self.NPNumber.setObjectName("NPNumber")
        self.gridLayout.addWidget(self.NPNumber, 3, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setRowStretch(0, 5)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.windgedFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(0, 60, 321, 44))
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.populationNumberInput = QtWidgets.QLineEdit(self.widget)
        self.populationNumberInput.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstDecorative")
        font.setPointSize(10)
        self.populationNumberInput.setFont(font)
        self.populationNumberInput.setStyleSheet("background-color:rgb(125, 125, 125);\n"
"color: White;\n"
"\n"
"")
        self.populationNumberInput.setCursorPosition(13)
        self.populationNumberInput.setAlignment(QtCore.Qt.AlignCenter)
        self.populationNumberInput.setObjectName("populationNumberInput")
        self.horizontalLayout_5.addWidget(self.populationNumberInput)
        self.startButton = QtWidgets.QPushButton(self.widget)
        self.startButton.setMaximumSize(QtCore.QSize(140, 16777215))
        self.startButton.setStyleSheet("background-color:Green;\n"
"color:White")
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_5.addWidget(self.startButton)
        self.targetTextInput = QtWidgets.QLineEdit(self.frame_2)
        self.targetTextInput.setGeometry(QtCore.QRect(69, 24, 171, 31))
        self.targetTextInput.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstDecorative")
        font.setPointSize(10)
        self.targetTextInput.setFont(font)
        self.targetTextInput.setStyleSheet("background-color:rgb(125, 125, 125);\n"
"color: White;")
        self.targetTextInput.setCursorPosition(6)
        self.targetTextInput.setAlignment(QtCore.Qt.AlignCenter)
        self.targetTextInput.setObjectName("targetTextInput")
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.windgedFrame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.windgedFrame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 6)
        self.horizontalLayout_2.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bestFintessScore.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Best </span>Guess: <span style=\" font-weight:600; color:#ffffff;\">NONE</span></p></body></html>"))
        self.bestFintessScore_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Generation </span>Number: <span style=\" font-weight:600; color:#ffffff;\">NONE</span></p></body></html>"))
        self.parent1.setText(_translate("MainWindow", "Parent"))
        self.parent3.setText(_translate("MainWindow", "Parent"))
        self.parent6.setText(_translate("MainWindow", "Parent"))
        self.parent2.setText(_translate("MainWindow", "Parent"))
        self.parent4.setText(_translate("MainWindow", "Parent"))
        self.parent5.setText(_translate("MainWindow", "Parent"))
        self.parent7.setText(_translate("MainWindow", "Parent"))
        self.parent8.setText(_translate("MainWindow", "Parent"))
        self.parent9.setText(_translate("MainWindow", "Parent"))
        self.parent10.setText(_translate("MainWindow", "Parent"))
        self.fitness1.setText(_translate("MainWindow", "Fitness: "))
        self.fitness2.setText(_translate("MainWindow", "Fitness: "))
        self.fitness3.setText(_translate("MainWindow", "Fitness: "))
        self.fitness4.setText(_translate("MainWindow", "Fitness: "))
        self.fitness5.setText(_translate("MainWindow", "Fitness: "))
        self.fitness6.setText(_translate("MainWindow", "Fitness: "))
        self.fitness7.setText(_translate("MainWindow", "Fitness: "))
        self.fitness8.setText(_translate("MainWindow", "Fitness: "))
        self.fitness9.setText(_translate("MainWindow", "Fitness: "))
        self.fitness10.setText(_translate("MainWindow", "Fitness: "))
        self.MRNumber.setText(_translate("MainWindow", "0"))
        self.crossOverRateTX_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">COR</span></p></body></html>"))
        self.parentNumber_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">NP</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.mutationRateText_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">MR</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\"><br/></span></p></body></html>"))
        self.CORNumber.setText(_translate("MainWindow", "0"))
        self.NPNumber.setText(_translate("MainWindow", "2"))
        self.populationNumberInput.setText(_translate("MainWindow", "Population No"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.targetTextInput.setText(_translate("MainWindow", "TARGET"))

