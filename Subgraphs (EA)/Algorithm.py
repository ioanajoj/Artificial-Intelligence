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
        self.__population.evaluate(self.__problem)
        i1, i2 = self.__population.selection()
        individual1 = self.__population.getIndividual(i1)
        individual2 = self.__population.getIndividual(i2)
        child = individual1.crossover(individual2, probability)
        child.fitness(self.__problem)
        mutated = child.mutate(probability)
        mutated.fitness(self.__problem)

        individuals = sorted([individual1, individual2, child, mutated])
        self.__population.setIndividual(i1, individuals[0])
        self.__population.setIndividual(i2, individuals[1])

    def run(self):
        """

        :return: void
        """
        number_iterations = 1000
        probability_mutation = 0.01
        for i in range(number_iterations):
            self.iteration(probability_mutation)
        print(self.__population.getBest())

    def statistics(self):
        """

        :return: void
        """
        pass
