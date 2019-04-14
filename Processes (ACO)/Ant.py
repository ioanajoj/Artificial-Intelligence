from random import randint, random


class Ant:
    def __init__(self, tasks, machines, problem):
        """
        Initialize a possible schedule for tasks on given machines
        self.tasks: Integer = number of tasks
        self.machines: Integer = number of machines
        self.solution = tasks * machines matrix having 1 where task i is executed by machine j
        """
        self.tasks = tasks
        self.machines = machines
        self.problem = problem
        self.solution = [[0 for j in range(machines)] for i in range(tasks)]
        self.initialize()

    def initialize(self):
        for i in range(self.machines):
            combo = (randint(0, self.problem.tasks - 1), i)
            self.update(combo)

    def evaluate(self):
        pass

    def update(self, task_machine):
        """
        Update solution
        task_machine = (task, machine)
        :return:
        """
        # get available tasks for each machine
        # available_tasks = self.get_available_tasks()
        task, machine = task_machine
        self.solution[task][machine] = 1

    def get_available_tasks(self):
        """
        return a list containing lists of available tasks for each machine
        :return:
        """
        result = []
        for m, machine in enumerate(self.machines):
            available_tasks = []
            for t, task_line in enumerate(self.solution):
                if task_line[m] == 0:
                    available_tasks.append(task_line[m])
            result.append(available_tasks)
        return result

    def get_available_tasks_per_machine(self, machine_index):
        """
        return a list containing available tasks for given machine
        :return:
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
        :param pheromone_matrix: Matrix having <task> lines and <machine> columns
        :param alpha:
        :param beta:
        :return:
        """
        for machine_index in range(self.machines):
            available_tasks = self.get_available_tasks_per_machine(machine_index)
            if len(available_tasks) == 0:
                continue
            divider = sum((pheromone_matrix[task_index][machine_index] ** alpha) *
                          (self.problem.cost_matrix[task_index][machine_index] ** beta)
                          for task_index in available_tasks)

            probabilities = []
            for task in available_tasks:
                a = pheromone_matrix[task][machine_index]
                b = self.problem.cost_matrix[task][machine_index]
                c = divider
                p = ((pheromone_matrix[task][machine_index] ** alpha) *
                    (self.problem.cost_matrix[task][machine_index] ** beta)) / divider
                probabilities.append(p)

            cumulative_sum = self.get_cumulative_sum(probabilities)
            task_index = self.choose_task(cumulative_sum)
            if task_index == None:
                print("aici")
            task = available_tasks[task_index]
            self.solution[task][machine_index] = 1

    def choose_task(self, cumulative_sum):
        """
        Choose random task_index from cumulative_sum array using roulette method
        :param cumulative_sum:
        :return: int
        """
        r = random()
        cumulative_sum = cumulative_sum[::-1]
        for task_index, x in enumerate(cumulative_sum):
            if r < x:
                return task_index

    def get_cumulative_sum(self, probabilities):
        cumulative_sum = []
        for i in range(len(probabilities)):
            suma = sum(probabilities[i:])
            cumulative_sum.append(suma)
        return cumulative_sum

    def cost_move(self, task_index, machine_index):
        return self.problem.cost_matrix[task_index][machine_index]

    def fitness(self):
        cost = 0
        for task_index, task_line in enumerate(self.solution):
            for machine_index, usage_value in enumerate(task_line):
                if usage_value == 1:
                    cost += self.problem.cost_matrix[task_index][machine_index]
        return cost

    def show_solution(self):
        for task_index, task_line in enumerate(self.solution):
            for machine_index, usage_value in enumerate(task_line):
                if usage_value == 1:
                    print("Task " + str(task_index) + " executed by machine " + str(machine_index))

    def __gt__(self, other):
        return self.fitness() > other.fitness()
