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
        ' Range of numbers to choose from '
        self.__pool = list(range(0, 10))
        ' Controller : problem'
        self.__controller = None
        ' Problem : text, pool'
        self.__problem = None
        ' Text of problem '
        self.__text = []
        ' Method 0: DFS, Method 1: GreedyBFS '
        self.__choice = 0
        self.change_method()

    def printMainMenu(self):
        s = ''
        s += "1 - Enter custom operation. \n"
        s += "2 - Change method. \n"
        s += "3 - Change range. \n"
        for i in range(len(self.__text)):
            s += str(i+4) + " - Solve " + str(self.__text[i]) + "\n"
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
                    self.custom_operation()
                elif command == 2:
                    self.change_method()
                elif command == 3:
                    self.change_pool()
                elif command == 4:
                    text = self.__text[0]
                    self.solve(text)
                elif command == 5:
                    text = self.__text[1]
                    self.solve(text)
                elif command == 6:
                    text = self.__text[2]
                    self.solve(text)
                elif command == 7:
                    text = self.__text[3]
                    self.solve(text)
            except ValueError:
                print("invalid command")

    def solve(self, text):
        if self.__choice == 0:
            self.solveWithDFS(text)
        else:
            self.solveWithGreedy(text)

    def solveWithDFS(self, text):
        """
            Create Controller having Problem by text and solve using DFS
            :param text: Text of the problem
        """
        print("DFS:")
        self.__problem = Problem(text, self.__pool)
        self.__controller = Controller(self.__problem)
        start_time = time()
        try:
            print(str(self.__controller.dfs(self.__problem.get_root())))
        except Exception as ex:
            print(ex)
        print("execution time =", time() - start_time, "seconds")

    def solveWithGreedy(self, text):
        """
            Create Controller having Problem by text and solve using GreedyBFS
            :param text: Text of the problem
        """
        print("GreedyBFS")
        self.__problem = Problem(text, self.__pool)
        self.__controller = Controller(self.__problem)
        start_time = time()
        try:
            print(str(self.__controller.greedyBfs(self.__problem.get_root())))
        except Exception as ex:
            print(ex)
        print("execution time =", time() - start_time, "seconds")

    def custom_operation(self):
        """
            Take text input of custom problem having the form A + B = C
        """
        text = input("Enter your problem: ")
        self.solve(text)

    def change_pool(self):
        """
            Change pool of values
        """
        limit = int(input("Enter limit: "))
        self.__pool = list(range(0, limit))

    def read_from_file(self):
        """
            Read from file
        """
        with open('input_problems') as f:
            for line in f:
                self.__text.append(line.rstrip('\n'))
        f.close()

    def change_method(self):
        """
            Change method for solving
        """
        self.__choice = int(input("Enter 0 for DFS and 1 for greedyBFS: "))


def main():
    ui = UI()
    ui.run()


main()
