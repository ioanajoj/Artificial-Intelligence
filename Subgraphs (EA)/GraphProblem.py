class GraphProblem:
    def __init__(self, file_name):
        """
            self.__nodes: Integer
            self.__matrix: Matrix of 0 and 1
        """
        self.__nodes = 0
        self.__graph = dict()
        self.load_data(file_name)

    def load_data(self, file_name):
        """
        Load data from file
        :param file_name: String
        :return: void
        """
        file = open(file_name)
        lines = file.read().split("\n")
        self.__nodes = int(lines[0])
        for i in range(self.__nodes):
            line = lines[i+1].split(" ")
            self.__graph[i] = []
            for j in range(self.__nodes):
                if line[j] != '0':
                    self.__graph[i].append(j)
        print(self.__graph)

    def getNumberOfNodes(self):
        """
        :return: Number of nodes in the graph
        """
        return self.__nodes

    def getGraph(self):
        """
        :return: Dictionary of values in the graph and connected nodes
        """
        return self.__graph
