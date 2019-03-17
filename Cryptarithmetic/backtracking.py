def backIter(max_number, max_len):
    x = [0, 0, 0]
    while len(x) > 0:
        choosed = False
        while not choosed and x[-1] < max_number-1:
            x[-1] = x[-1] + 1
            choosed = consistent(x, max_len)
            if choosed:
                if solution(x, max_len):
                    print(x)
                x.append(-1)
            else:
                x = x[:-1]


def consistent(stack, max_len):
    return len(stack) == len(set(stack)) and len(stack) <= max_len


def solution(stack, max_len):
    return len(stack) == max_len


backIter(5, 3)
