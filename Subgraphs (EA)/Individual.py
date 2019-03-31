from collections import deque
from random import random, randint


class Individual:
    def __init__(self, size, configuration):
        """
        :param size: Integer
        :param configuration: [0,1...]
        """
        self.__size = size
        self.__configuration = configuration

    def fitness(self, problem):
        """
        Get the number of vertices not reaching all the other vertices in its subgraph
        :param problem: Problem
        :return: Integer
        """
        if self.__configuration.count(0) != self.__size // 2 or self.__configuration.count(1) != self.__size // 2:
            return self.__size + 1
        subgraph1, subgraph2 = self.partition()
        graph = problem
        fit1 = self.getGraphFitness(graph, subgraph1)
        fit2 = self.getGraphFitness(graph, subgraph2)
        return fit1 + fit2

    def getGraphFitness(self, graph, subgraph):
        """
        Count all the vertices not reaching all the other vertices in its subgraph
        :param graph: Dictionary representing the whole graph
        :param subgraph: Set of vertices in subgraph
        :return:
        """
        fit = 0
        for node in subgraph:
            reached_nodes = self.bfs(node, subgraph, graph)
            if len(reached_nodes) < graph.getNumberOfNodes()//2:
                fit += 1
        return fit

    def bfs(self, vertex, subgraph, graph):
        """
        Find all reachable nodes from subgraph
        :param vertex: Integer
        :param subgraph: Set of integers representing nodes from same subgraph
        :param graph: Dictionary representing the whole graph
        :return: list of reachable nodes
        """
        q = deque()
        q.append(vertex)
        visited = set()
        visited.add(vertex)
        while not len(q) == 0:
            current = q.popleft()
            for n in self.getNeghbours(current, graph, subgraph):
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        return visited

    def getNeghbours(self, vertex, graph, subgraph):
        """
        Get direct neighbours of vertex in subgraph
        :param vertex: Integer
        :param graph: Dictionary representing the whole graph
        :param subgraph: Set of integers representing nodes from same subgraph
        :return: set of direct neighbouring nodes
        """
        neighbours = set()
        graph_config = graph.getGraph()
        for n in graph_config[vertex]:
            if n in subgraph:
                neighbours.add(n)
        return neighbours

    def partition(self):
        """
        Get sets of nodes from divided subgraphs based on current configuration
        :return:
        """
        subgraph1 = set()
        subgraph2 = set()
        for i in range(len(self.__configuration)):
            if self.__configuration[i] == 0:
                subgraph1.add(i)
            else:
                subgraph2.add(i)
        return subgraph1, subgraph2

    def mutate(self, probability):
        """
        Performs a mutation on an individual with the probability of pM.
        If the event will take place, at a random position a new value will be
        generated in the interval [vmin, vmax]

        individual:the individual to be mutated
        pM: the probability the mutation to occure
        :param probability:
        :return: void
        """
        if probability > random():
            p = randint(0, self.__size//2)
            rand = randint(0, 2)
            self.__configuration[p] = rand
            self.__configuration[self.__size - 1 - p] = int(rand-1)

    def crossover(self, individ, probability):
        """
        Crossover another individual
        :param individ: Individual
        :param probability: float
        :return: void
        """
        half1 = self.__configuration[:self.__size//2]
        half2 = individ.getConfiguration()[self.__size//2:]
        # if probability > random():
        #     half1, half2 = half2, half1
        child = Individual(self.__size, half1 + half2)
        child2 = Individual(self.__size, half2 + half1)
        return child, child2

    def getConfiguration(self):
        return self.__configuration

    def __str__(self):
        return str(self.__configuration)
