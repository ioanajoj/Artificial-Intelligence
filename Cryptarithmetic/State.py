class State:
    def __init__(self, mapping):
        self.__mapping = mapping

    def set_new_values(self, values):
        i = 0
        for key in self.__mapping.keys():
            self.__mapping[key] = values[i]
            i += 1

    def get_value(self, letter):
        return self.__mapping[letter]

    def get_length(self):
        return len(self.__mapping)

    def is_valid(self, constraints):
        for letter in constraints:
            if self.__mapping[letter] == 0 or self.__mapping[letter] is None:
                return False
        return len(self.__mapping.values()) == len(set(self.__mapping.values()))

    def __str__(self):
        s = ''
        for l in self.__mapping.keys():
            s += l + "=" + str(self.__mapping[l]) + " : "
        return s
