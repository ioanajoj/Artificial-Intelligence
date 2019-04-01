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
        self.__fitnesses = []
        self.__problem = None
        self.__population = None
        self.__population_size = None
        self.__evaluations = None
        self.__number_of_runs = None
        self.__muation_probability = None
        self.read_paramaters(parameters_file_name)

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
        # Evaluate fitness for each individual
        self.__population.evaluate(self.__problem)

        # Select individuals
        i1, i2 = self.__population.selection()
        individual1 = self.__population.getIndividual(i1)
        individual2 = self.__population.getIndividual(i2)

        # Create offspring
        child1, child2 = individual1.crossover(individual2, probability)
        child1.fitness(self.__problem)
        child2.fitness(self.__problem)
        child1.mutate(probability)
        child2.mutate(probability)

        individuals = [individual1, individual2, child1, child2]
        individuals = sorted(individuals)

        self.__population.setIndividual(i1, individuals[0])
        self.__population.setIndividual(i2, individuals[1])

    def run(self):
        """

        :return: void
        """
        self.__problem = GraphProblem(self.__data_file_name)
        for i in range(self.__number_of_runs):
            print("Iteration " + str(i), end=": ")
            self.__population = Population(self.__population_size, self.__problem.getNumberOfNodes())
            for j in range(self.__evaluations):
                self.iteration(self.__muation_probability)
                average_fitness = self.__population.getAverage()
                print(average_fitness)
                self.__fitnesses.append(average_fitness)
            self.plotGeneration()
        # self.statistics()


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
        std_deviation = math.sqrt(sum_best // (len(self.__fitnesses) - 1))
        print(std_deviation)

    def plotGeneration(self):
        to_plot = self.__fitnesses
        plt.plot(to_plot)
        plt.ylabel('fitness')
        plt.xlabel('individual')
        plt.show()
