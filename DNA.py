import random


class DNA:

    def __init__(self, length):
        self.fit = 0
        self.genes = []
        for i in range(length):
            self.genes.append(chr(random.randint(0, 150)))

    def getPhrase(self):
        return "".join(self.genes)

    def fitness(self, target):
        score = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score += 1
        self.fit = score/len(target)

    def crossover(self, partner):
        child = DNA(0)
        midpoint = random.randint(0, len(self.genes))
        for i in range(len(self.genes)):
            if i < midpoint:
                child.genes.append(self.genes[i])
            else:
                child.genes.append(partner.genes[i])
        return child

    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[i] = chr(random.randint(0, 150))
