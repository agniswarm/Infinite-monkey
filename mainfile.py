from Population import Population

# define the variables that can be tweaked
target = 'Et tu Brute, then Fall Caesar'
popMax = 150
mutationRate = 0.05

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
