from random import randint, random


class Ant:
    def __init__(self, tasks, machines, problem):
        """
        Initialize a possible schedule for tasks on given machines
        self.tasks: Integer = number of tasks
        self.machines: Integer = number of machines
        self.problem: Problem -> used for evaluating fitness
        self.solution = tasks * machines matrix having 1 where task i is executed by machine j, 0 otherwise
        """
        self.tasks = tasks
        self.machines = machines
        self.problem = problem
        self.solution = [[0 for j in range(machines)] for i in range(tasks)]
        self.initialize()

    def initialize(self):
        """
        Initialize the solution with a first task given to all machines
        :return:
        """
        for i in range(self.machines):
            combo = (randint(0, self.problem.tasks - 1), i)
            self.update(combo)

    def update(self, task_machine):
        """
        Update solution
        task_machine = (task, machine)
        :return:
        """
        task, machine = task_machine
        self.solution[task][machine] = 1

    def get_available_tasks(self):
        """
        :return: list containing available tasks for the given machine
        """
        available_tasks = []
        for t, task_line in enumerate(self.solution):
            ok = True
            for m in task_line:
                if m == 1:
                    ok = False
            if ok:
                available_tasks.append(t)
        return available_tasks

    def add_move(self, pheromone_matrix, alpha, beta):
        """
        Add a task for each machine
        :param pheromone_matrix: Matrix having <no_task> lines and <no_machine> columns
        :param alpha:
        :param beta:
        """
        for machine_index in range(self.machines):
            # get list of available tasks
            available_tasks = self.get_available_tasks()
            # if list is empty then break
            if len(available_tasks) == 0:
                break

            # compute the sum of indices given by all paths
            divider = sum((pheromone_matrix[task_index][machine_index] ** alpha) *
                          (self.problem.cost_matrix[task_index][machine_index] ** beta)
                          for task_index in available_tasks)

            # compute probabilities for all tasks
            probabilities = []
            for task in available_tasks:
                p = ((pheromone_matrix[task][machine_index] ** alpha) *
                     (self.problem.cost_matrix[task][machine_index] ** beta)) / divider
                probabilities.append(p)

            # compute a cumulative sum for probabilities
            cumulative_sum = self.get_cumulative_sum(probabilities)
            # choose a task using the roulette method and update the solution
            task = available_tasks[self.choose_task(cumulative_sum)]
            self.solution[task][machine_index] = 1

    def choose_task(self, cumulative_sum):
        """
        Choose random task_index from cumulative_sum array using roulette method
        :param cumulative_sum: list of int [0,1]
        :return: int
        """
        r = random()
        cumulative_sum = cumulative_sum[::-1]
        for task_index, x in enumerate(cumulative_sum):
            if r < x:
                return task_index

    def get_cumulative_sum(self, probabilities):
        """
        Compute the cumulative sum given a list of probabilities
                probabilities:  0.76, 0.19, 0.05
            =>  cumulative_sum:    1, 0.24, 0.05
        :param probabilities: List<float>
        :return: List<float>
        """
        cumulative_sum = []
        for i in range(len(probabilities)):
            suma = sum(probabilities[i:])
            cumulative_sum.append(suma)
        return cumulative_sum

    def fitness(self):
        """
        Compute fitness by counting the cost for each machine and determining the maximum from all
        :return: int
        """
        cost = []
        # for task_index, task_line in enumerate(self.solution):
        #     machine_cost = 0
        #     for machine_index, usage_value in enumerate(task_line):
        #         if usage_value != 0:
        #             machine_cost += self.problem.cost_matrix[task_index][machine_index]
        #     cost.append(machine_cost)
        for machine_index in range(self.machines):
            machine_cost = 0
            for task_index, task_line in enumerate(self.solution):
                if task_line[machine_index] == 1:
                    machine_cost += self.problem.cost_matrix[task_index][machine_index]
            cost.append(machine_cost)
        return max(cost)

    def show_solution(self):
        """
        Print the solution somewhat nicely
        :return: void
        """
        for task_index, task_line in enumerate(self.solution):
            for machine_index, usage_value in enumerate(task_line):
                if usage_value == 1:
                    print("Task " + str(task_index) + " executed by machine " + str(machine_index))

    def __gt__(self, other):
        return self.fitness() > other.fitness()
