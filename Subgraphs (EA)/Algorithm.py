from math import sqrt

import math
import matplotlib.pyplot as plt

from GraphProblem import GraphProblem
from Population import Population


class Algorithm:
    def __init__(self, file_name, parameters_file_name):
        """
        self.__problem: Problem
        self.__population: Population
        """
        self.__data_file_name = file_name
        self.read_paramaters(parameters_file_name)
        self.__fitnesses = []

    def read_paramaters(self, file_name):
        """
        Create problem object and call load_data on it
        :param file_name: String
        :return: void
        """
        file = open(file_name)
        lines = file.read().split("\n")
        self.__population_size = int(lines[0].split(":")[1])
        self.__evaluations = int(lines[1].split(":")[1])
        self.__number_of_runs = int(lines[2].split(":")[1])
        self.__muation_probability = float(lines[3].split(":")[1])

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
        individuals = [individual1, individual2, child]
        if mutated is not None:
            mutated.fitness(self.__problem)
            individuals.append(mutated)
        individuals = sorted(individuals)

        self.__population.setIndividual(i1, individuals[0])
        self.__population.setIndividual(i2, individuals[1])

    def run(self):
        """

        :return: void
        """
        for i in range(self.__number_of_runs):
            print("Iteration " + str(i), end=": ")
            self.__problem = GraphProblem(self.__data_file_name)
            self.__population = Population(self.__population_size, self.__problem.getNumberOfNodes())
            for j in range(self.__evaluations):
                self.iteration(self.__muation_probability)
            self.__fitnesses.append(self.__population.getBest().getFitness())
        self.statistics()

    def statistics(self):
        """

        :return: void
        """
        print("Average of best solutions:", end=" ")
        average = float(sum(self.__fitnesses)) / len(self.__fitnesses)
        print(average)

        print("Standard deviation:", end=" ")
        sum_best = 0
        for i in self.__fitnesses:
            a = self.__fitnesses[i] - average
            sum_best += a
        sum_best = sum([pow(i - average, 2) for i in self.__fitnesses])
        # x = sum_best // len(self.__f)
        std_deviation = math.sqrt(sum_best // (len(self.__fitnesses) - 1))
        print(std_deviation)

        to_plot = self.__population.getFitnesses()
        plt.plot(to_plot)
        plt.ylabel('fitness')
        plt.xlabel('individual')
        plt.show()
