class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def dfs(self, root):
        q = [root]
        while len(q) > 0:
            currentState = q.pop(0)
            if self.__problem.check(currentState):
                return currentState
            new_state = self.__problem.expand()
            if new_state is not None:
                q.append(new_state)
                print(str(new_state) + str(len(q)))
        print("finished?")