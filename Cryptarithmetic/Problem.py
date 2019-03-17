import itertools

from Cryptarithmetic.State import State
from collections import OrderedDict


class Problem:
    def __init__(self, text):
        # first = constrained letters
        # second = unconstrained letters
        self.__text = text
        self.__constraints = set(self.get_constraints())
        self.__first_letters = self.get_first_letters()
        self.__rest_letters = self.get_rest_letters()

        # define States
        # self.__state_1 = State(self.__first_letters)
        # self.__state_2 = State(self.__rest_letters)
        self.__current_state = State(self.__first_letters, self.__rest_letters)

        # define iterators:
        #   iter_1 = iterator for values different from 0
        #   iter_2 = iterator for all values
        self.__pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.__iter_1 = iter(itertools.permutations(self.__pool[1:], len(self.__constraints)))
        self.__iter_2 = iter(itertools.permutations(self.__pool, self.__current_state.get_length() - len(self.__constraints)))

    def expand(self):
        while True:
            values_1 = next(self.__iter_1, None)
            values_2 = next(self.__iter_2, None)
            # print(values)
            if values_1 and values_2 is not None:
                self.__current_state.set_new_values(values_1, 1)
                self.__current_state.set_new_values(values_2, 2)
                # self.__state_1.set_new_values(values_1)
                # self.__state_1.set_new_values(values_2)
                print(values_1)
                print(values_2)
                if self.__current_state.is_valid(self.__constraints):
                    return self.__current_state
            else:
                break

    def expand(self):
        while True:
            values_1 = next(self.__iter_1, None)
            if values_1 is not None:
                self.__current_state.set_new_values(values_1, 1)
                values_2 = next(self.__iter_2, None)
                if values_1 and values_2 is not None:
                    self.__current_state.set_new_values(values_2, 2)
                    print(values_1)
                    print(values_2)
                    if self.__current_state.is_valid(self.__constraints):
                        return self.__current_state
            else:
                break

    def expand_rest(self):
        self.__iter_2 = iter(
            itertools.permutations(self.__pool, self.__current_state.get_length() - len(self.__constraints)))
        while True:
            values_2 = next(self.__iter_2, None)
            if values_2 is not None:
                self.__current_state.set_new_values(values_2, 2)
                print(values_1)
                print(values_2)
                if self.__current_state.is_valid(self.__constraints):
                    return self.__current_state

    # solve for minus
    def check(self, current_state):
        if not current_state.is_valid(self.__constraints):
            return False
        before_eq = True
        operation = '+'
        left_side = 0
        right_side = 0
        for word in self.__text.split(' '):
            if before_eq:
                if word == '-':
                    operation = '-'
                elif word == '=':
                    before_eq = False
                elif word != '+':
                    left_side = self.get_value(word, current_state)
            else:
                right_side = self.get_value(word, current_state)
        return left_side == right_side

    @staticmethod
    def get_value(word, current_state):
        suma = 0
        index = 0
        for letter in word[::-1]:
            suma += current_state.get_value(letter) * 16 * index
            index += 1
        return suma

    def get_root(self):
        return self.__current_state

    @staticmethod
    def get_initial_dict(text):
        new_text = ''.join(filter(str.isalpha, text))
        return OrderedDict.fromkeys(new_text)

    def get_constraints(self):
        whitelist = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        words = ''.join(filter(whitelist.__contains__, self.__text)).split(' ')
        constraints = ''
        for word in words:
            if len(word) > 0:
                constraints += word[0]
        return constraints

    def get_first_letters(self):
        new_text = ''.join(filter(lambda v: self.check_filter(v), self.__text))
        return OrderedDict.fromkeys(new_text)

    def get_rest_letters(self):
        new_text = ''.join(filter(lambda v: str.isalpha(v) and not self.check_filter(v), self.__text))
        return OrderedDict.fromkeys(new_text)

    def check_filter(self, v):
        return str.isalpha(v) and self.__constraints.__contains__(v)

    def not_check_filter(self):
        return not self.check_filter()
