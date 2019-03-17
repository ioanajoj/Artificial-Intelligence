class State:
    def __init__(self, permutation):
        self.__permut = permutation.get_copy()
        self.__mapping = self.__permut.get_mapping()

    def set_new_values(self, values):
        i = 0
        for key in self.__mapping.keys():
            self.__mapping[key] = values[i]
            i += 1

    def is_valid(self, constraints):
        for letter in constraints:
            if self.__mapping[letter] == 0 or self.__mapping[letter] is None:
                return False
        if list(self.__mapping.values()).__contains__(None):
            return False
        return len(self.__mapping.values()) == len(set(self.__mapping.values()))

    def has_next(self, constraints):
        for letter in constraints:
            if self.__mapping[letter] == 0:
                return False
        for k1 in self.__mapping.keys():
            for k2 in self.__mapping.keys():
                if k1 != k2 and self.__mapping[k1] is not None and self.__mapping[k2] is not None:
                    if self.__mapping[k1] == self.__mapping[k2]:
                        return False
        return True

    def get_value(self, letter):
        return self.__permut.get_mapping()[letter]

    def get_length(self):
        return len(self.__mapping)

    def get_permutation(self):
        return self.__permut

    def __str__(self):
        s = ''
        for l in self.__mapping.keys():
            s += l + "=" + str(self.__mapping[l]) + " : "
        return s

    def __add__(self, permutation):
        new_state = State(permutation.get_copy())
        new_state.set_new_values(permutation.get_values())
        return new_state
