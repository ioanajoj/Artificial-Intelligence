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
        self.__problem = Problem("SEND + MORE = MONEY")
        self.__controller = Controller(self.__problem)

    def printMainMenu(self):
        s = "1 - Solve SEND + MORE = MONEY.\n"
        # s += "2 - Solve EAT + THAT = CAKE. \n"
        # s += "3 - Solve NEVER + DRIVE = RIDE. \n"
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
                    self.solveWithDFS()
            except IOError:
                print("invalid command")

    def solveWithDFS(self):
        startTime = time()
        print(str(self.__controller.dfs(self.__problem.get_root())))
        print('execution time = ', time() - startTime, " seconds")


def main():
    ui = UI()
    ui.run()


main()
