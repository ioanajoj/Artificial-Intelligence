class State:
    def __init__(self, permutation):
        """
        :param permutation: Permutation
                self.__mapping = dictionary of letters mapped to values from Permutation
        """
        self.__permutation = permutation.get_copy()
        self.__mapping = self.__permutation.get_mapping()

    def set_new_values(self, values):
        """
        :param values: dictionary
        :return: sets new values to current state letters
        """
        i = 0
        for key in self.__mapping.keys():
            self.__mapping[key] = values[i]
            i += 1

    def is_valid(self, constraints):
        """
        :param constraints: String
        :return: False if constraint letters = 0, any letter is mapped to None or there are duplicate values
                 True, otherwise
        """
        for letter in constraints:
            if self.__mapping[letter] == 0 or self.__mapping[letter] is None:
                return False
        if list(self.__mapping.values()).__contains__(None):
            return False
        return len(self.__mapping.values()) == len(set(self.__mapping.values()))

    def has_next(self, constraints):
        """
        :param constraints: String
        :return: False if any constrained letter is mapped to 0 or any two letters are mapped to the same value
                 True, otherwise
        """
        for letter in constraints:
            if self.__mapping[letter] == 0:
                return False
        filtered = list(filter(lambda x: x is not None, self.__mapping))
        if len(filtered) != len(set(filtered)):
            return False
        return True

    def get_value(self, letter):
        """
        :param letter: String
        :return: mapped value of letter
        """
        return self.__permutation.get_mapping()[letter]

    def get_length(self):
        """
        :return: number of letters
        """
        return len(self.__mapping)

    def get_permutation(self):
        """
        :return: Permutation object
        """
        return self.__permutation

    def __str__(self):
        s = ''
        for l in self.__mapping.keys():
            s += l + "=" + str(self.__mapping[l]) + " : "
        return s

    def __add__(self, permutation):
        new_state = State(permutation.get_copy())
        new_state.set_new_values(permutation.get_values())
        return new_state
