from Individual import Individual
from random import shuffle, randint, random


class Population:
    def __init__(self, no_individuals, individual_size):
        """
        Initialize population
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
        Tournament selection
        :return: two individuals having best fitness from a random sample of 10
        """
        tournament_size = 4
        probability = 0.6
        staged_individuals = []
        for i in range(tournament_size):
            random_index = randint(0, len(self.__list_individuals) - 1)
            staged_individuals.append(self.__list_individuals.pop(random_index))
        if random() > probability:
            staged_individuals = sorted(staged_individuals)
        else:
            staged_individuals = sorted(staged_individuals, reverse=True)
        ind1 = staged_individuals.pop(0)
        ind2 = staged_individuals.pop(0)
        self.__list_individuals += staged_individuals
        return ind1, ind2

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
        # individuals = sorted(self.__list_individuals)
        individuals = self.__list_individuals
        return [i.getFitness() for i in individuals]

    def getAverage(self):
        suma = 0
        for ind in self.__list_individuals:
            suma += ind.getFitness()
        return float(suma) / len(self.__list_individuals)

    def addIndividual(self, individual):
        self.__list_individuals.append(individual)
