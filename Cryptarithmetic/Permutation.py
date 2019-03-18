class Permutation:

    def __init__(self, mapping, possible_values, level):
        """
        :param mapping: dictionary
        :param possible_values: pool of values
        :param level: in the tree of possible solutions
        """
        self.__level = level
        self.__mapping = mapping
        self.__config = list(mapping.values())
        self.__possible_values = possible_values

    def next_permutation(self):
        """
        :return: get next permutation from current config
        """
        if self.__level == len(self.__config):
            return []
        result = []
        for i in self.__possible_values:
            new_config = self.__config[:]
            new_config[self.__level] = i
            new_mapping = self.__mapping.copy()
            j = 0
            for key in list(new_mapping.keys()):
                new_mapping[key] = new_config[j]
                j += 1
            result.append(Permutation(new_mapping, self.__possible_values, self.__level + 1))
        return result

    def get_partial_sum(self):
        """
        :return: Sum up values from current config
        """
        return sum(filter(None, self.__config))

    def get_values(self):
        return self.__config

    def get_mapping(self):
        return self.__mapping

    def get_copy(self):
        return Permutation(self.__mapping.copy(), self.__possible_values, self.__level)
