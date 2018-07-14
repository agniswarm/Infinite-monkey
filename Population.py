from DNA import DNA
import math
import random


def map(itemToBeMapped, lowerToMap, higherToMap, lowerToBeMapped=0, higherToBeMapped=1):
    try:
        val = (itemToBeMapped-lowerToMap)/(higherToMap-lowerToMap) * \
            (higherToBeMapped-lowerToBeMapped)+lowerToBeMapped
    except:
        return lowerToBeMapped
    return val


class Population:
    mutatationRate = 0
    target = ''
    population = []
    matingPool = []
    finished = False
    perfectScore = 0
    generation = 0

    def __init__(self, target, mutationRate, popMax):
        self.target = target
        self.mutationRate = mutationRate
        for i in range(popMax):
            self.population.append(DNA(len(target)))
        self.calcFitness()
        self.finished = False
        self.perfectScore = 1

    def calcFitness(self):
        for popu in self.population:
            popu.fitness(self.target)

    def naturalSelection(self):
        self.matingPool.clear()
        maxFitness = 0
        for popu in self.population:
            if(popu.fit > maxFitness):
                maxFitness = popu.fit
        for popu in self.population:
            fit = int(map(popu.fit, 0, maxFitness, 0, 100))
            for i in range(fit):
                self.matingPool.append(popu)

    def generate(self):
        for i in range(len(self.population)):
            a = random.choices(self.matingPool, k=2)
            child = a[0].crossover(a[1])
            child.mutate(self.mutationRate)
            self.population[i] = child
        self.generation += 1

    def getBest(self):
        worldRecord = 0
        index = 0
        for i in range(len(self.population)):
            if worldRecord < self.population[i].fit:
                worldRecord = self.population[i].fit
                index = i
        if worldRecord == self.perfectScore:
            self.finished = True
        return self.population[index].getPhrase()
