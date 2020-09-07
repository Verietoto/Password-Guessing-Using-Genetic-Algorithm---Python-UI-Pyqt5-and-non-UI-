"""
Hello World!!! This is a free python code of Genetic Algorithm method for word guessing problem, i made GUI Version
and nonGUI Version just it cas you guys are eager too learn about the parameters and how it affect the others.
You can use this as your reference, but dont use for commercial use.

Contact Me:

Email:      Verietoto@gmail.com
Linkedin:   www.linkedin.com/in/ketut-toto-suryahadinata-2755a9b0

"""

import numpy as np
from itertools import combinations


class WordsGuessing():
    def __init__(self, TARGET, populationNumber, numParent, CHANCE, CROSSOVER_RATE):
        self.TARGET = TARGET
        self.CROSSOVER_RATE = CROSSOVER_RATE
        self.populationNumber = populationNumber
        self.CHANCE = CHANCE
        self.numparent = numParent
        self.createPopulation(populationNumber)
        self.selectParent(self.numparent)
        self.createChild(self.CROSSOVER_RATE)


    def createGen(self):
        gen = []
        for i in range(len(self.TARGET)):
            gen.append(chr(np.random.randint(32, 127)))
        return ''.join(gen)

    def createPopulation(self, populationNumber):
        self.population = []
        for i in range(populationNumber):
            self.population.append(self.createGen())
        self.populationFitness = self.calculateFitness(self.population)

    def calculateFitness(self, population):
        populatinFitness = np.zeros((len(population)))
        for index, word in enumerate(population):
            for element in zip(word, self.TARGET):
                if element[0] == element[1]:
                    populatinFitness[index] += 1
        return populatinFitness*100/len(self.TARGET)

    def selectParent(self, numParent):
        indexes = np.argsort(self.populationFitness)[-numParent:]
        self.parent = []

        for i in range(numParent):
            self.parent.append(self.population[indexes[i]])


    def crossOver(self, parent1, parent2):
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

    def createChild(self, CROSSOVER_RATE):
        children = []
        parentCombination = combinations(self.parent, 2)


        for i in parentCombination:
            if np.random.rand() < CROSSOVER_RATE:
                children.extend(self.crossOver(i[0], i[1]))
            else:
                children.extend([i[0], i[1]])
        self.children = [self.mutateChild(child, self.CHANCE) for child in children]
        self.childrenFitness = self.calculateFitness(self.children)

    def mutateChild(self, child, CHANCE):
        mutate = []
        for j, i in enumerate(child):
            posibility = np.random.rand(1)
            if CHANCE >= posibility:
                mutate.append(chr(np.random.randint(32, 128)))
            else:
                mutate.append(i)
        return ''.join(mutate)


    def selection(self):
        self.bestFitness = 0
        self.generation = 0
        while self.bestFitness != 100:

            minPopulation = np.argsort(self.population)[0:len(self.children)]
            self.bestIndividu = self.population[np.argmax(self.populationFitness)]
            self.bestFitness = self.populationFitness[np.argmax(self.populationFitness)]
            self.selectParent(self.numparent)
            self.createChild(self.CROSSOVER_RATE)
            self.display(self.generation)

            self.generation += 1
            # if np.max(self.childrenFitness) <= self.bestFitness-10:
            #     continue
            for i, j in enumerate(minPopulation):
                self.population[j] = self.children[i]
                self.populationFitness[j] = self.childrenFitness[i]

