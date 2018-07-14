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
        self.perfectScore = len(target)

    # calcuate the fitness of the individual element of the population
    def calcFitness(self):
        for popu in self.population:
            popu.fitness(self.target)

    # natural selection to take place here
    def naturalSelection(self):
        # clear the mating pool
        self.matingPool.clear()
        # sorting the array according to fitness and taking the
        # top 1/3 fit guys to make the next generation
        self.population.sort(key=lambda x: x.fit, reverse=True)
        self.matingPool = self.population[0:int(len(self.population)/3)]
        # for i in range(int(len(self.population)/3)):
        #     self.matingPool.append(self.population[i])

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
        worldRecord = self.population[0].fit
        if worldRecord == self.perfectScore:
            self.finished = True
        return self.population[0].getPhrase()
