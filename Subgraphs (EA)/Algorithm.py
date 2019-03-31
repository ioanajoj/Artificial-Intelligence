from random import randint


class Algorithm:
    def __init__(self, problem, population, file_name):
        """
        self.__problem: Problem
        self.__population: Population
        """
        self.__problem = problem
        self.__population = population
        self.read_paramaters(file_name)

    def read_paramaters(self, file_name):
        """
        Create problem object and call load_data on it
        :param file_name: String
        :return: void
        """
        pass

    def iteration(self, probability):
        """

        :return: void
        """
        i1 = randint(0, self.__population.getSize() - 1)
        i2 = randint(0, self.__population.getSize() - 1)
        if i1 != i2:
            individual1 = self.__population.getIndividual(i1)
            individual2 = self.__population.getIndividual(i2)
            child1, child2 = individual1.crossover(individual2, probability)
            child1.mutate(probability)
            child2.mutate(probability)
            fitness1 = individual1.fitness(self.__problem)
            fitness2 = individual2.fitness(self.__problem)
            '''
            the repeated evaluation of the parents can be avoided
            if  next to the values stored in the individuals we 
            keep also their fitnesses 
            '''
            fitness_child1 = child1.fitness(self.__problem)
            fitness_child2 = child2.fitness(self.__problem)
            if fitness_child1 < fitness_child2:
                child = child1
                fitness = fitness_child1
            else:
                child = child2
                fitness = fitness_child2
            if (fitness1 > fitness2) and (fitness1 > fitness):
                self.__population.setIndividual(i1, child)
            if (fitness2 > fitness1) and (fitness2 > fitness):
                self.__population.setIndividual(i2, child)

    def run(self):
        """

        :return: void
        """
        number_iterations = 1000
        probability_mutation = 0.01
        for i in range(number_iterations):
            self.iteration(probability_mutation)
        self.__population.evaluate(self.__problem)
        print(3)

    def statistics(self):
        """

        :return: void
        """
        pass
