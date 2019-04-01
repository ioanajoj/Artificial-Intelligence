from Individual import Individual
from random import shuffle, randint


class Population:
    def __init__(self, no_individuals, individual_size):
        """

        :param no_individuals: Integer
        :param list_individuals: List<Individual>
        """
        self.__no_individuals = no_individuals
        self.__list_individuals = []
        for i in range(self.__no_individuals):
            values = list(range(individual_size))
            shuffle(values)
            self.__list_individuals.append(Individual(individual_size, values))

    def evaluate(self, problem):
        """

        :return: void
        """
        for individual in self.__list_individuals:
            individual.fitness(problem)

    def selection(self):
        """
        Can have more parameters
        :return: void
        """
        i1 = randint(0, self.__no_individuals - 1)
        i2 = randint(0, self.__no_individuals - 1)
        while i1 == i2:
            i2 = randint(0, self.__no_individuals - 1)
        return i1, i2

    def getSize(self):
        return self.__no_individuals

    def getIndividual(self, index):
        return self.__list_individuals[index]

    def setIndividual(self, index, individual):
        self.__list_individuals[index] = individual

    def getBest(self):
        """
        Get the individual having the best fitness
        :return: Individual
        """
        return min(self.__list_individuals)

    def getFitnesses(self):
        individuals = sorted(self.__list_individuals)
        return [i.getFitness() for i in individuals]