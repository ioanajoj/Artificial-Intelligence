class Controller:
    def __init__(self, problem):
        """
        :param problem: Problem
        """
        self.__problem = problem

    def dfs(self, root):
        """
        :param root: State
        :return: valid result State
        """
        q = [root]
        while len(q) > 0:
            current_state = q.pop()
            if self.__problem.check(current_state):
                return current_state
            new_state = self.__problem.expand(current_state)
            q = q + new_state
        raise Exception('No solution found')

    def greedyBfs(self, root):
        """
        :param root: State
        :return: valid result State
        """
        next_configuration = [root]
        while len(next_configuration) > 0:
            current_state = next_configuration.pop()
            if self.__problem.check(current_state):
                return current_state
            new_states = self.__problem.expand(current_state)
            new_state = self.__problem.heuristic(new_states)
            if new_state:
                next_configuration = next_configuration + new_state
        raise Exception('No solution found')
