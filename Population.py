from DNA import DNA


class Population:
    mutatationRate = 0
    target = ''
    population = []
    matingPool = []
    finished = False
    perfectScore = 9999

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
