from Population import Population

target = 'To be or not to be.'
popMax = 150
mutationRate = 0.01

population = Population(target, mutationRate, popMax)

print(population)
generation = 0
while(True):
    population.naturalSelection()
    population.generate()
    population.calcFitness()
    print(str(population.getBest()) +
          ' in generation :' + str(population.generation))
    if population.finished:
        break
