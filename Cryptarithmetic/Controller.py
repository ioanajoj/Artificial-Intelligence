class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def dfs(self, root):
        q = [root]
        while len(q) > 0:
            currentState = q.pop()
            # print(currentState)
            if self.__problem.check(currentState):
                return currentState
            new_state = self.__problem.expand(currentState)
            q = q + new_state
        print("Couldn't find any solution")

    def greedyBfs(self, root):
        next_configuration = [root]
        while len(next_configuration) > 0:
            currentState = next_configuration.pop()
            # print(currentState)
            if self.__problem.check(currentState):
                return currentState
            new_states = self.__problem.expand(currentState)
            new_state = self.__problem.heuristic(new_states)
            if new_state:
                next_configuration = next_configuration + new_state
        print("Couldn't find any solution")
