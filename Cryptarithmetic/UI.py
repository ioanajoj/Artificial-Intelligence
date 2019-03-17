"""
    Implement an algorithm that solves a crypt-arithmetic problem knowing that:
        • Each letter represents a hexadecimal number
        • The result of the arithmetic operation must be correct when the letters are
            replaced by numbers
        • The numbers can not start with 0
        • Every problem can have only one solution

     SEND +      EAT +       NEVER -
     MORE =     THAT =       DRIVE =
    MONEY       CAKE          RIDE

"""
from time import time

from Cryptarithmetic.Controller import Controller
from Cryptarithmetic.Problem import Problem


class UI:
    def __init__(self):
        self.__pool = list(range(0, 10))
        self.__problem = None
        self.__controller = None

    def printMainMenu(self):
        s = "1 - Solve SEND + MORE = MONEY.\n"
        s += "2 - Solve EAT + THAT = CAKE. \n"
        s += "3 - Solve NEVER - DRIVE = RIDE. \n"
        s += "4 - Enter custom operation. \n"
        s += "5 - Change range. \n"
        print(s)

    def run(self):
        run_menu = True
        self.printMainMenu()
        while run_menu:
            try:
                command = int(input(": "))
                if command == 0:
                    run_menu = False
                elif command == 1:
                    text = "SEND + MORE = MONEY"
                    self.solveWithDFS(text)
                elif command == 2:
                    text = "EAT + THAT = CAKE"
                    self.solveWithDFS(text)
                elif command == 3:
                    text = "NEVER - DRIVE = RIDE"
                    self.solveWithDFS(text)
                elif command == 4:
                    self.custom_operation()
                elif command == 5:
                    self.change_pool()
            except ValueError:
                print("invalid command")

    def solveWithDFS(self, text):
        self.__problem = Problem(text, self.__pool)
        self.__controller = Controller(self.__problem)
        startTime = time()
        print(str(self.__controller.dfs(self.__problem.get_root())))
        print("execution time =", time() - startTime, "seconds")

    def custom_operation(self):
        text = input("Enter your problem: ")
        self.solveWithDFS(text)

    def change_pool(self):
        limit = int(input("Enter limit: "))
        self.__pool = list(range(0, limit))


def main():
    ui = UI()
    ui.run()


main()
