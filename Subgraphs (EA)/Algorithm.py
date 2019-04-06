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
        self.best_solutions = []
        self.averages = []

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
        Create a new generation
        :return: void
        """
        # Evaluate fitness for each individual
        self.__population.evaluate(self.__problem)

        # Select individuals
        individual1, individual2 = self.__population.selection()

        # Create offspring
        child1, child2 = individual1.crossover(individual2, probability)
        child1.fitness(self.__problem)
        child2.fitness(self.__problem)
        child1.mutate(probability)
        child2.mutate(probability)

        # Select new individuals to be inserted
        individuals = [individual1, individual2, child1, child2]
        individuals = sorted(individuals)

        # Insert best individuals from parents and children
        self.__population.addIndividual(individuals[0])
        self.__population.addIndividual(individuals[1])

    def run(self):
        """
        Perform given number of runs for populations and given number of evaluations
        :return: void
        """
        self.__problem = GraphProblem(self.__data_file_name)
        for i in range(self.__number_of_runs):
            print("Iteration " + str(i), end=": ")
            self.__population = Population(self.__population_size, self.__problem.getNumberOfNodes())
            for j in range(self.__evaluations):
                self.iteration(self.__muation_probability)
                average_fitness = self.__population.getAverage()
                print("average fitness = " + str(average_fitness), end=", ")
                self.__fitnesses.append(average_fitness)
                best_solution = self.__population.getBest().getFitness()
                print("best solution = " + str(best_solution))
                self.best_solutions.append(best_solution)
            self.plotGeneration()
            self.averages.append(self.__population.getAverage())
        self.statistics()

    def statistics(self):
        """
        Print the average and standard deviation for the best solutions found by your the algorithm
        after 1000 evaluations of the fitness function in 30 runs, with populations of 40 individuals
        :return: void
        """
        print("Average of best solutions:", end=" ")
        average = float(sum(self.best_solutions)) / len(self.best_solutions)
        print(average)

        print("Standard deviation:", end=" ")
        sum_best = sum([pow(i - average, 2) for i in self.best_solutions])
        std_deviation = math.sqrt(sum_best // (len(self.best_solutions) - 1))
        print(std_deviation)

        self.plotAvg()

    def plotGeneration(self):
        """
        Plot average fitnesses after one run
        :return: void
        """
        to_plot = self.__fitnesses
        # plt.clf()
        plt.plot(to_plot, 'g^')
        plt.ylabel('fitness')
        plt.xlabel('individual')
        plt.show()
        self.__fitnesses = []

    def plotAvg(self):
        """
        Plot final average of every run
        :return: void
        """
        to_plot = self.averages
        plt.plot(to_plot, 'g^')
        plt.ylabel('final average')
        plt.xlabel('run')
        plt.show()
