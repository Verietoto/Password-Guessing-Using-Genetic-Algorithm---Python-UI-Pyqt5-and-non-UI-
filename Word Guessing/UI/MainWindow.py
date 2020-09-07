"""
Hello World!!! This is a free python code of Genetic Algorithm method for word guessing problem, i made GUI Version
and nonGUI Version just it cas you guys are eager too learn about the parameters and how it affect the others.
You can use this as your reference, but dont use for commercial use.

Contact Me:

Email:      Verietoto@gmail.com
Linkedin:   www.linkedin.com/in/ketut-toto-suryahadinata-2755a9b0
"""


### Some Libraries

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from  PyQt5.QtCore import *
import numpy as np
import time
COUNTER = 0
import sys

from UI.Screen.LoadingScreen import Ui_loadingWindow
from UI.Screen.GeneticWindow import GeneticWindow_UI
from UI.GeneticAlgorithm import WordsGuessing

# Class Windiw for DashBoard
class DashBoard():

    def __init__(self):
        """
         Here I am using init method with no object in braket

         mainWindow is the main window i used
         dashBoard is genetic UI attached into mainWindow
         hideParent is function to hide every parent in dashboard window
         sliderValue is function to change label when slider is moved
         self.dashBoard.startButton.clicked.connect(self.startGenetic) means when i click start button, genetic algorithm will start
         """

        self.mainWindow = QMainWindow()
        self.dashBoard = GeneticWindow_UI()
        self.dashBoard.setupUi(self.mainWindow)
        self.hideParent()
        self.sliderValue()
        self.dashBoard.startButton.clicked.connect(self.startGenetic)

    def startGenetic(self):
        """
        Start Genetic when start button pressed
        :return: Nothing
        """

        TARGET = self.dashBoard.targetTextInput.text()
        crossOverRate = float(self.dashBoard.CORNumber.text())
        mutationRate = float(self.dashBoard.MRNumber.text())
        populationNumber = int(self.dashBoard.populationNumberInput.text())
        numParent = int(self.dashBoard.NPNumber.text())

        self.wordGuess = WordsGuessing(TARGET, populationNumber, numParent, mutationRate, crossOverRate)
        for i in range(10):
            if i <= numParent-1:
                eval("self.dashBoard.parent" + str(i + 1)).show()
                eval("self.dashBoard.fitness" + str(i + 1)).show()
            else:
                eval("self.dashBoard.parent" + str(i + 1)).hide()
                eval("self.dashBoard.fitness" + str(i + 1)).hide()

        self.update(numParent, mutationRate)

    def update(self, numParent, mutationRate):
        """
        Update every parameter in ggenetic algorithm
        :param numParent:
        :param mutationRate:
        :return:
        """
        self.generation = 0
        self.bestFitness = 0

        while self.bestFitness != 100:

            time.sleep(0.005)
            self.bestFitness = self.wordGuess.populationFitness[np.argmax(self.wordGuess.populationFitness)]
            self.minPopulation = np.argsort(self.wordGuess.population)[0:len(self.wordGuess.children)]
            self.bestIndividu = self.wordGuess.population[np.argmax(self.wordGuess.populationFitness)]
            self.wordGuess.selectParent(numParent)
            self.wordGuess.createChild(mutationRate)


            self.dashBoard.bestFintessScore.setText(
                "<html><head/><body><p><span style=\" font-weight:600;\">Best </span>Guess: <span style=\" font-weight:600; color:#ffffff;\">" + self.bestIndividu + "</span></p></body></html>")
            self.dashBoard.bestFintessScore_2.setText(
                "<html><head/><body><p><span style=\" font-weight:600;\">Generation </span>Number: <span style=\" font-weight:600; color:#ffffff;\">" + str(
                    self.generation) + "</span></p></body></html>")

            for i in range(numParent):
                eval("self.dashBoard.parent" + str(i + 1)).setText("{}".format(self.wordGuess.population[i]))
                eval("self.dashBoard.fitness" + str(i + 1)).setText("fitness: {:.2f}".format(self.wordGuess.populationFitness[i]))
            self.generation += 1


            for i, j in enumerate(self.minPopulation):
                self.wordGuess.population[j] = self.wordGuess.children[i]
                self.wordGuess.populationFitness[j] = self.wordGuess.childrenFitness[i]

            if self.generation > 5000:
                break

            QCoreApplication.processEvents()

    def hideParent(self):
        """
        Hide Parent Text in DashBoard for a while until genetic algorithm start
        :return:
        """
        for i in range(10):
            eval("self.dashBoard.parent"+str(i+1)).hide()
            eval("self.dashBoard.fitness"+str(i+1)).hide()

    def sliderValue(self):
        """
        Change slider value Minimum and Maksimum
        :return:
        """
        self.dashBoard.crossOverRateSlider_2.setMinimum(0)
        self.dashBoard.crossOverRateSlider_2.setMaximum(10)
        self.dashBoard.crossOverRateSlider_2.setTickInterval(1)
        self.dashBoard.crossOverRateSlider_2.valueChanged.connect(
            lambda : self.changeValueSlider(self.dashBoard.MRNumber,self.dashBoard.crossOverRateSlider_2))

        self.dashBoard.mutationRateSlider_2.setMinimum(0)
        self.dashBoard.mutationRateSlider_2.setMaximum(10)
        self.dashBoard.mutationRateSlider_2.setTickInterval(1)
        self.dashBoard.mutationRateSlider_2.valueChanged.connect(
            lambda: self.changeValueSlider(self.dashBoard.CORNumber, self.dashBoard.mutationRateSlider_2))

        self.dashBoard.numberParentSlider_2.setMinimum(2)
        self.dashBoard.numberParentSlider_2.setMaximum(10)
        self.dashBoard.numberParentSlider_2.setTickInterval(1)
        self.dashBoard.numberParentSlider_2.valueChanged.connect(lambda: self.changeValueSlider(self.dashBoard.NPNumber, self.dashBoard.numberParentSlider_2))

    def changeValueSlider(self, text, slider):
        """
        Change label text respectivly with slider value
        :return:
        """

        size = slider.value()
        if slider != self.dashBoard.numberParentSlider_2:
            text.setText(str(size/10))
        else:
            text.setText(str(size))


class HomePage():
    def __init__(self):

        """
        Same init method as DashBoard
        """
        # Main Window
        self.mainWindow = QMainWindow()


        # Embedded Main Window to Loading Screen and move to center of screen
        self.loadingScreen = Ui_loadingWindow()
        self.loadingScreen.setupUi(self.mainWindow)
        self.mainWindow.move(300, 100)

        # Set Window into Frameless Window and show Window
        self.mainWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.mainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.mainWindow.show()

        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)

        # Editing Loading Text
        QtCore.QTimer.singleShot(4500,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>WELCOME</strong> TO SEISTROV"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>LOADING</strong> USER INTERFACE"))
        QtCore.QTimer.singleShot(2000,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>LOADING</strong> DATA BASED"))

    def progress(self):
        """
        Make a progress bar i loading window animated and close loading window after a specific time
        then open DashBoard
        :return:
        """
        global COUNTER

        self.loadingScreen.progressBar.setValue(COUNTER)
        COUNTER += 1

        if COUNTER > 100:
            self.timer.stop()
            self.mainWindow.close()
            self.geneticWindow = DashBoard()
            self.geneticWindow.mainWindow.showMaximized()


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = HomePage()
    sys.exit(app.exec_())