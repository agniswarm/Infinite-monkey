import random


class DNA:

    # create a population object with some genes
    # here genes are random ascii characters b/e 0 to 150
    def __init__(self, length):
        self.fit = 0
        self.genes = []
        for i in range(length):
            self.genes.append(chr(random.randint(0, 150)))

    # this function returns the character array as a string
    def getPhrase(self):
        return "".join(self.genes)

    # the fitness of all the elements are calculated
    def fitness(self, target):
        score = 0
        # it checks the number of elements that are in the correct position the more elements
        # in the correct position the better is the score assigned to it
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score += 1
        # the score is then normalized by dividing it with the no of elements that needs to be correct
        self.fit = score

    # crossover function takes two set of DNA and performs a crossover b/w those
    def crossover(self, partner):
        child = DNA(0)
        # a random midpoint is calculated to make the crossover happen
        midpoint = random.randint(0, len(self.genes))
        # all the DNA before the midpoint are taken from parent1(calling object)
        # rest are taken from partner
        for i in range(len(self.genes)):
            if i < midpoint:
                child.genes.append(self.genes[i])
            else:
                child.genes.append(partner.genes[i])
        return child

    # return a mutatued gene to keep the variation going throughout the generation
    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[i] = chr(random.randint(0, 150))
