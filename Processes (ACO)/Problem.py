class Problem:
    def __init__(self, file_name):
        """
        self.machines = number of available machines
        self.tasks = number of tasks to be run
        self.durations_m1 = mapping of task and duration on machine m1
        self.durations_m2 = mapping of task and duration on machine m2
        """
        self.machines = 0
        self.tasks = 0
        self.cost_matrix = []
        self.load_problem(file_name)

    def load_problem(self, file_name):
        """
        Load problem parameters from file
        :param file_name: String
        :return: void
        """
        file = open(file_name)
        lines = file.read().split("\n")
        self.machines = int(lines[0].split(":")[1])
        self.tasks = int(lines[1].split(":")[1])
        self.cost_matrix = [[0 for i in range(self.machines)] for j in range(self.tasks)]
        for i in range(self.tasks):
            line = lines[i + 2].split(" ")
            for j in range(self.machines):
                self.cost_matrix[i][j] = int(line[j])
        print(self.machines)
        print(self.tasks)
        print(self.cost_matrix)
