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
        self.__text = []
        self.__choice = 1

    def printMainMenu(self):
        s = "1 - Solve " + self.__text[0] + "\n"
        s += "2 - Solve " + self.__text[1] + "\n"
        s += "3 - Solve " + self.__text[2] + "\n"
        s += "4 - Solve " + self.__text[3] + "\n"
        s += "5 - Enter custom operation. \n"
        s += "6 - Change method. \n"
        s += "7 - Change range. \n"
        print(s)

    def run(self):
        run_menu = True
        self.read_from_file()
        self.printMainMenu()
        while run_menu:
            try:
                command = int(input(": "))
                if command == 0:
                    run_menu = False
                elif command == 1:
                    text = self.__text[0]
                    self.solve(text)
                elif command == 2:
                    text = self.__text[1]
                    self.solve(text)
                elif command == 3:
                    text = self.__text[2]
                    self.solve(text)
                elif command == 4:
                    text = self.__text[3]
                    self.solve(text)
                elif command == 5:
                    self.custom_operation()
                elif command == 6:
                    self.change_method()
                elif command == 7:
                    self.change_pool()
            except ValueError:
                print("invalid command")

    def solve(self, text):
        if self.__choice == 0:
            self.solveWithDFS(text)
        else:
            self.solveWithGreedy(text)

    def solveWithDFS(self, text):
        self.__problem = Problem(text, self.__pool)
        self.__controller = Controller(self.__problem)
        startTime = time()
        print(str(self.__controller.dfs(self.__problem.get_root())))
        print("execution time =", time() - startTime, "seconds")

    def solveWithGreedy(self, text):
        self.__problem = Problem(text, self.__pool)
        self.__controller = Controller(self.__problem)
        startTime = time()
        print(str(self.__controller.greedyBfs(self.__problem.get_root())))
        print("execution time =", time() - startTime, "seconds")

    def custom_operation(self):
        text = input("Enter your problem: ")
        self.solveWithDFS(text)

    def change_pool(self):
        limit = int(input("Enter limit: "))
        self.__pool = list(range(0, limit))

    def read_from_file(self):
        with open('input_problems') as f:
            for line in f:
                self.__text.append(line.rstrip('\n'))
        f.close()

    def change_method(self):
        self.__choice = int(input("Enter 0 for DFS and 1 for greedyBFS: "))


def main():
    ui = UI()
    ui.run()


main()
