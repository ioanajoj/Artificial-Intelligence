from Cryptarithmetic.Permutation import Permutation
from Cryptarithmetic.State import State
from collections import OrderedDict


class Problem:
    def __init__(self, text, pool):
        self.__text = text
        self.__constraints = set(self.get_constraints())
        self.__pool = pool
        self.__config = Permutation(self.get_initial_dict(), self.__pool, 0)
        self.__current_state = State(self.__config)

    def expand(self, current_config):
        configs = current_config.get_permutation().next_permut()
        result = []
        for conf in configs:
            state = self.__current_state + conf
            if state.has_next(self.__constraints):
                result.append(state)
        return result

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
                        left_side = left_side + self.get_value(current_state, word)
                    else:
                        left_side = left_side - self.get_value(current_state, word)
            else:
                right_side = self.get_value(current_state, word)
        if left_side == right_side:
            return True
        return False

    def get_value(self, current_state, word):
        result = 0
        index = 0
        for letter in word[::-1]:
            result += current_state.get_value(letter) * pow(10, index)
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
