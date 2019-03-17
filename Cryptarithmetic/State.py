from collections import OrderedDict


class State:
    def __init__(self, mapping1, mapping2):
        self.__mapping1 = mapping1
        self.__mapping2 = mapping2
        self.__all = OrderedDict()
        for x in mapping1:
            self.__all.update({x: mapping1[x]})
        for x in mapping2:
            self.__all.update({x: mapping2[x]})

    def set_new_values(self, values, item):
        i = 0
        if item == 1:
            for key in self.__mapping1.keys():
                self.__mapping1[key] = values[i]
                self.__all[key] = values[i]
                i += 1
        else:
            for key in self.__mapping2.keys():
                self.__mapping2[key] = values[i]
                self.__all[key] = values[i]
                i += 1

    def get_value(self, letter):
        return self.__all[letter]

    def get_length(self):
        return len(self.__all)

    def is_valid(self, constraints):
        # for letter in constraints:
        #     if self.__mapping[letter] == 0 or self.__mapping[letter] is None:
        #         return False
        return len(self.__all.values()) == len(set(self.__all.values()))

    def __str__(self):
        s = ''
        for l in self.__all.keys():
            s += l + "=" + str(self.__all[l]) + " : "
        return s
