from Controller import Controller


controller = Controller("data.in", "parameters.in")
print("We are going on a trip in our favourite rocket ship...")
best_ant = controller.runAlgorithm()
print("Best solution found")
print("Having fitness: " + str(best_ant.fitness()))
best_ant.show_solution()
