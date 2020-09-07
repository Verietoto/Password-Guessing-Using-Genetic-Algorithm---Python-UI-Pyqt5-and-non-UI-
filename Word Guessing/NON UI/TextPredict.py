
"""
Hello World!!! This is a free python code of Genetic Algorithm method for word guessing problem, i made GUI Version
and nonGUI Version just it cas you guys are eager too learn about the parameters and how it affect the others.
You can use this as your reference, but dont use for commercial use.

Contact Me:

Email:      Verietoto@gmail.com
Linkedin:   www.linkedin.com/in/ketut-toto-suryahadinata-2755a9b0

"""

"""
importing Some libraries
"""
import numpy as np
from itertools import combinations
import sys
import time


class WordsGuessing():
    """
    I am using init method
    Target is word target (string)
    crossOverRate is probability of a children inherith both parent1 and parent2 genes
    MUTATIONRATE is probability of a gen experience a mutation
    numParrent is how many parent (Nth best guess) we pick
    select Parent is how we pick a parent
    createChild is function for creating a child based on every combination of parent
    selection is a simply a looping to update paameter
    display is a display function
    """
    def __init__(self, TARGET, populationNumber, numParent, MUTATIONRATE, CROSSOVER_RATE):
        self.TARGET = TARGET
        self.crossOverRate = CROSSOVER_RATE
        self.populationNumber = populationNumber
        self.MUTATIONRATE = MUTATIONRATE
        self.numparent = numParent
        self.createPopulation(populationNumber)
        self.selectParent(self.numparent)
        self.createChild(self.crossOverRate)
        self.selection()
        self.display(self.generation)


    def createGen(self):
        """
        creating child using random function. Creat a random number from 32 and 127 then convert into string
        :return:
        """

        gen = []
        for i in range(len(self.TARGET)):
            gen.append(chr(np.random.randint(32, 127)))
        return ''.join(gen)

    def createPopulation(self, populationNumber):
        """
        create a specicfic number of population
        :param populationNumber:
        :return:
        """
        self.population = []
        for i in range(populationNumber):
            self.population.append(self.createGen())
        self.populationFitness = self.calculateFitness(self.population)

    def calculateFitness(self, population):
        """
        calcultion of fitness of every individu in population
        :param population:
        :return:
        """
        populatinFitness = np.zeros((len(population)))
        for index, word in enumerate(population):
            for element in zip(word, self.TARGET):
                if element[0] == element[1]:
                    populatinFitness[index] += 1
        return populatinFitness*100/len(self.TARGET)

    def selectParent(self, numParent):
        """
        Select a spesific number of parent (N number of best guess)
        :param numParent:
        :return:
        """
        indexes = np.argsort(self.populationFitness)[-numParent:]
        self.parent = []

        for i in range(numParent):
            self.parent.append(self.population[indexes[i]])


    def crossOver(self, parent1, parent2):
        """
        cross child genes from parent 1 and parent 2 in random crossover point
        :param parent1:
        :param parent2:
        :return:
        """
        child1 = []
        child2 = []

        for i in range(len(parent1)):
            cross_points = np.random.randint(0, len(parent1))
            if i <= cross_points:
                child1.append(parent2[i])
                child2.append(parent1[i])
            else:
                child1.append(parent1[i])
                child2.append(parent2[i])

        return ''.join(child1), ''.join(child2)

    def createChild(self, crossOverRate):
        """
        creating child with crossover rate, when value surpassed crossover rate then cross over is trigerred
        if no, child's gen and parent's gen will exactly same.
        :param crossOverRate:
        :return:
        """
        children = []
        parentCombination = combinations(self.parent, 2)


        for i in parentCombination:
            if np.random.rand() < crossOverRate:
                children.extend(self.crossOver(i[0], i[1]))
            else:
                children.extend([i[0], i[1]])
        self.children = [self.mutateChild(child, self.MUTATIONRATE) for child in children]
        self.childrenFitness = self.calculateFitness(self.children)

    def mutateChild(self, child, MUTATIONRATE):
        """
        mutate gen in child's gen when a random number lies over mutation rate
        :param child:
        :param MUTATIONRATE:
        :return:
        """
        mutate = []
        for j, i in enumerate(child):
            posibility = np.random.rand(1)
            if MUTATIONRATE >= posibility:
                mutate.append(chr(np.random.randint(32, 128)))
            else:
                mutate.append(i)
        return ''.join(mutate)


    def selection(self):
        """
        update all parameter in genetic algorithm
        :return:
        """
        self.bestFitness = 0
        self.generation = 0
        while self.bestFitness != 100:

            minPopulation = np.argsort(self.population)[0:len(self.children)]
            self.bestIndividu = self.population[np.argmax(self.populationFitness)]
            self.bestFitness = self.populationFitness[np.argmax(self.populationFitness)]
            self.selectParent(self.numparent)
            self.createChild(self.crossOverRate)
            self.display(self.generation)

            self.generation += 1
            for i, j in enumerate(minPopulation):
                self.population[j] = self.children[i]
                self.populationFitness[j] = self.childrenFitness[i]
    def display(self, generation):
        sys.stdout.write('\r Generation # ' + str(generation) + '\t' + "Guess: {} \t Fitness: {}".format(self.bestIndividu, self.bestFitness))


if __name__ == '__main__':
    TARGET = "Hallo my name is Ketut Toto Suryahadinata!!"
    WordsGuessing(TARGET, 1000,10, 0.07, 0.5)