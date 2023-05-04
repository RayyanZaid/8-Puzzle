from typing import List
from SolvePuzzleFunction import solve_puzzle


initialBoard : List[str] = []

print("Enter your custom puzzle!")

for i in range(9):
    item = input("Enter item #{}: ".format(i+1))
    initialBoard.append(item)

print("Enter which algorithm you want: 1 = Uniform Cost Search, 2 = Misplaced Tile heuristic, and 3 = Euclidean Distance heuristic")
algorithmNumber = input()


print(solve_puzzle(initialBoard, algorithmNumber))

