import itertools

from Cryptarithmetic.State import State
from collections import OrderedDict


class Problem:
    def __init__(self, text):
        self.__text = text
        self.__constraints = set(self.get_constraints())

        # define state
        self.__config = self.get_initial_dict()
        self.__current_state = State(self.__config)

        # define iterator:
        self.__pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__iter = iter(itertools.permutations(self.__pool, len(self.__config)))

    def expand(self):
        while True:
            values = next(self.__iter, None)
            if values is not None:
                self.__current_state.set_new_values(values)
                if self.__current_state.is_valid(self.__constraints):
                    return self.__current_state
            else:
                break

    def check(self, current_state):
        if not current_state.is_valid(self.__constraints):
            return False
        before_eq = True
        operation = '+'
        left_side = 0
        right_side = 0
        for word in self.__text.split(' '):
            if before_eq:
                if word == '+':
                    operation = '+'
                elif word == '-':
                    operation = '-'
                elif word == '=':
                    before_eq = False
                else:
                    if operation == '+':
                        left_side = left_side + self.get_value(word)
                    else:
                        left_side = left_side - self.get_value(word)
            else:
                right_side = self.get_value(word)
        if left_side == right_side:
            return True
        return False

    def get_value(self, word):
        result = 0
        index = 0
        for letter in word[::-1]:
            result += self.__current_state.get_value(letter) * pow(10, index)
            index += 1
        return result

    def get_root(self):
        return self.__current_state

    def get_initial_dict(self):
        new_text = ''.join(filter(str.isalpha, self.__text))
        return OrderedDict.fromkeys(new_text)

    def get_constraints(self):
        words = ''.join(filter(lambda ch: str.isalpha(ch) or str.isspace(ch), self.__text)).split(' ')
        constraints = ''
        for word in words:
            if len(word) > 0:
                constraints += word[0]
        return constraints
