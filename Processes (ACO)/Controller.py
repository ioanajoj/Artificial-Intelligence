from Ant import Ant
from Problem import Problem


class Controller:
    def __init__(self, data_file, parameters_file):
        """
        Initialize controller
        • create Problem with path to data_file
        • self.population = List<Ant>
        • load parameters from parameters_file
        • set self.no_steps as number of tasks * number of machines
        • initialize the pheromone matrix with 1 on all positions
        """
        self.problem = Problem(data_file)
        self.population = []
        self.no_runs = 0
        self.no_generations = 0
        self.alpha = 0
        self.beta = 0
        self.rho = 0
        self.load_parameters(parameters_file)
        self.no_steps = self.problem.tasks * self.problem.machines
        self.pheromone_matrix = [[1 for j in range(self.problem.machines)] for i in range(self.problem.tasks)]

    def load_parameters(self, parameters_file):
        with open(parameters_file, 'r') as file:
            line = file.readline().split(":")
            self.no_runs = int(line[1])

            line = file.readline().split(":")
            self.no_generations = int(line[1])

            line = file.readline().split(":")
            self.alpha = float(line[1])

            line = file.readline().split(":")
            self.beta = float(line[1])

            line = file.readline().split(":")
            self.rho = float(line[1])

    def iteration(self):
        # initialize population
        ants = [Ant(self.problem.tasks, self.problem.machines, self.problem) for i in range(self.problem.tasks)]
        for ant in ants:
            self.population.append(ant)

        # add steps to complete solutions for all ants
        for step in range(self.no_steps):
            for ant in self.population:
                ant.add_move(self.pheromone_matrix, self.alpha, self.beta)

        # select best ant and spread pheromone from its path
        bestAnt = max(self.population)
        self.spread_pheromone(bestAnt)

        return bestAnt

    def spread_pheromone(self, ant):
        """
        Update self.pheromone_matrix with the path followed by given ant
        :param ant: Ant
        :return: void
        """
        pheromone_increase = 1.0 / ant.fitness()
        for task_index, task_line in enumerate(ant.solution):
            for machine_index, usage_value in enumerate(task_line):
                if usage_value == 1:
                    self.pheromone_matrix[task_index][machine_index] += pheromone_increase

    def runAlgorithm(self):
        """
        Given a number of generations, run iterations and find the fittest ant
        :return: solution?
        """
        best_ant_fitness = 10000
        best_ant_global = None
        for i in range(self.no_generations):
            best_ant = self.iteration()
            if best_ant.fitness() < best_ant_fitness:
                best_ant_global = best_ant
                best_ant_fitness = best_ant.fitness()
            self.evaporation()
            self.population = []
        return best_ant_global

    def evaporation(self):
        """
        Diminish the pheromone level with the coefficient self.rho
        :return:
        """
        for task_index, task_line in enumerate(self.pheromone_matrix):
            for machine_index, usage_value in enumerate(task_line):
                self.pheromone_matrix[task_index][machine_index] *= (1 - self.rho)
