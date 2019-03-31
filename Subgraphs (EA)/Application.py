"""
    9. Subgraphs (EA)
    Consider an undirected graph G(V , E) with 2n nodes ( V is the set of nodes, and
    E is the set of edges). Partitionate the set of nodes in two disjoint sets V 1 and V 2,
    each containing exactly n nodes, in such a way that between any two nodes of the subgraphs
    determined by the subsets of nodes should be a path (both subgraphs are conex).
"""

from GraphProblem import GraphProblem
from Population import Population
from Algorithm import Algorithm


class Application:
    def main(self):
        file_name = "graph2.in"
        population_size = 100
        problem = GraphProblem(file_name)
        population = Population(population_size, problem.getNumberOfNodes())
        algorithm = Algorithm(problem, population, file_name)
        algorithm.run()


if __name__ == '__main__':
    app = Application()
    app.main()
