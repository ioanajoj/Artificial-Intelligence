# solution = [[0 for i in range(2)]for j in range(10)]
# print(solution)
#
# for i in range(4):
#     if i == 2:
#         continue
#     print(i)

for i in range(4):
    for j in range(4):
        if j == 3:
            continue
        print("j" + str(j))
    print("i" + str(i))