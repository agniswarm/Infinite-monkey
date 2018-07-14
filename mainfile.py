from Population import Population

# define the variables that can be tweaked
target = 'To be or not to be.'
popMax = 150
mutationRate = 0.01

population = Population(target, mutationRate, popMax)

generation = 0
while(True):
    population.naturalSelection()
    population.generate()
    population.calcFitness()
    print('"' + str(population.getBest()) + '"' +
          ' in generation :' + str(population.generation))
    if population.finished:
        break
