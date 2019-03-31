from Individual import Individual
from random import shuffle


class Population:
    def __init__(self, no_individuals, individual_size):
        """

        :param no_individuals: Integer
        :param list_individuals: List<Individual>
        """
        self.__no_individuals = no_individuals
        self.__list_individuals = []
        for i in range(self.__no_individuals):
            values = [1 for x in range(individual_size // 2)] + \
                     [0 for x in range(individual_size // 2)]
            shuffle(values)
            self.__list_individuals.append(Individual(individual_size, values))

    def evaluate(self, problem):
        """

        :return: void
        """
        for individual in self.__list_individuals:
            if individual.fitness(problem) == 0:
                print(individual)

    def selection(self):
        """
        Can have more parameters
        :return: void
        """
        pass

    def getSize(self):
        return self.__no_individuals

    def getIndividual(self, index):
        return self.__list_individuals[index]

    def setIndividual(self, index, individual):
        self.__list_individuals[index] = individual
