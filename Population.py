from DNA import DNA
import math
import random

# self created map function to normalize the data to a correct form


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

    # initialize a population having a certain DNA structure
    def __init__(self, target, mutationRate, popMax):
        self.target = target
        self.mutationRate = mutationRate
        for i in range(popMax):
            self.population.append(DNA(len(target)))
        self.calcFitness()
        self.finished = False
        self.perfectScore = 1

    # calcuate the fitness of the individual element of the population
    def calcFitness(self):
        for popu in self.population:
            popu.fitness(self.target)

    # natural selection to take place here
    def naturalSelection(self):
        self.matingPool.clear()  # clear the mating pool
        maxFitness = 0
        for popu in self.population:  # compute the maximum fitness in the group
            if(popu.fit > maxFitness):
                maxFitness = popu.fit
        for popu in self.population:  # compute the maxFitness and normalise the data b/w 0 to 100
            fit = int(map(popu.fit, 0, maxFitness, 0, 100))
            for i in range(fit):  # add to the most fittest to the mating pool
                self.matingPool.append(popu)

    # generate a new population of the with some mutation and crossovers
    def generate(self):
        for i in range(len(self.population)):
            a = random.choices(self.matingPool, k=2)
            child = a[0].crossover(a[1])  # crossover taking place
            # the child is getting mutated to add variation to the population
            child.mutate(self.mutationRate)
            self.population[i] = child
        self.generation += 1

    # to get the best fittest element of the lot
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
