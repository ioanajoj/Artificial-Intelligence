class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def dfs(self, root):
        q = [root]
        while len(q) > 0:
            currentState = q.pop()
            print(currentState)
            if self.__problem.check(currentState):
                return currentState
            new_state = self.__problem.expand(currentState)
            if new_state is not None:
                q = q + new_state
        print("Couldn't find any solution")
