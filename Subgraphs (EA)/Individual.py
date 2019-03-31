from collections import deque
from random import randint

from copy import copy

import sys


class Individual:
    def __init__(self, size, configuration):
        """
        :param size: Integer
        :param configuration: [0,1...]
        :param problem: GraphProblem
        """
        self.__size = size
        self.__configuration = configuration
        self.__fitness = sys.maxsize

    def fitness(self, problem):
        """
        Get the number of vertices not reaching all the other vertices in its subgraph
        :param problem: Problem
        :return: Integer
        """
        subgraph1, subgraph2 = self.partition()
        graph = problem
        fit1 = self.getGraphFitness(graph, subgraph1)
        fit2 = self.getGraphFitness(graph, subgraph2)
        self.__fitness = fit1 + fit2

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
        subgraph1 = set(self.__configuration[:self.__size // 2])
        subgraph2 = set(self.__configuration[self.__size // 2:])
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
        mutated = Individual(self.__size, copy(self.__configuration))
        p = randint(0, self.__size//2)
        mutated.__configuration[p], mutated.__configuration[self.__size - 1 - p] = \
            mutated.__configuration[self.__size - 1 - p], mutated.__configuration[p]
        return mutated

    def crossover(self, individ, probability):
        """
        Crossover another individual
        :param individ: Individual
        :param probability: float
        :return: void
        """
        child_config = [self.__configuration[pos] for pos in individ.getConfiguration()]
        return Individual(self.__size, child_config)

    def getConfiguration(self):
        return self.__configuration

    def __lt__(self, other):
        return self.__fitness < other.__fitness

    def __str__(self):
        return str(self.__configuration)
