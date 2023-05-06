from typing import List
from SolvePuzzleFunction import solve_puzzle
from ActionPathFunction import returnListOfStates


initialBoard : List[str] = []

print("Enter your custom puzzle!")

for i in range(9):
    item = input("Enter item #{}: ".format(i+1))
    initialBoard.append(item)


print("Enter which algorithm you want: 1 = Uniform Cost Search, 2 = Misplaced Tile heuristic, and 3 = Euclidean Distance heuristic")
algorithmNumber = input()


result = solve_puzzle(initialBoard, algorithmNumber)
isSolved = result[0]
if(isSolved):
    print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
    print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
    print(f"The depth of the goal node was {result[2]}")
    print("EXTRA CREDIT:")
    list_of_states = returnListOfStates(result[3])
    for eachState in list_of_states:
        print(eachState)
        print()

   





# print("EASY")
# result = solve_puzzle([["1","2","0"],
#                    ["4","5","3"],
#                    ["7","8","6"]],2)


# print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
# print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
# print(f"The depth of the goal node was {result[2]}")

# print()
# print("EXTRA CREDIT:")
# list_of_states = returnListOfStates(result[3])

# for eachState in list_of_states:
#     print(eachState)
#     print()

# print("DOABLE")
# result = solve_puzzle([["0","1","2"],
#                    ["4","5","3"],
#                    ["7","8","6"]],2)


# print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
# print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
# print(f"The depth of the goal node was {result[2]}")

# print()
# print("EXTRA CREDIT:")
# list_of_states = returnListOfStates(result[3])

# for eachState in list_of_states:
#     print(eachState)
#     print()


# print("OH BOY")
# result = solve_puzzle([["8","7","1"],
#                    ["6","0","2"],
#                    ["5","4","3"]],2)


# print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
# print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
# print(f"The depth of the goal node was {result[2]}")

# print()
# print("EXTRA CREDIT:")
# list_of_states = returnListOfStates(result[3])

# for eachState in list_of_states:
#     print(eachState)
#     print()