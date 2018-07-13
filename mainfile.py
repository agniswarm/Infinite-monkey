from Population import Population

target = 'To be or not to be'
popMax = 150
mutationRate = 0.01

population = Population(target, mutationRate, popMax)

print(population.population)
