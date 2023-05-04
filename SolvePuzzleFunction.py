import copy
from typing import List, Tuple
import queue
from StateNodeClass import StateNode
import numpy as np

from ActionPathFunction import returnListOfStates

def solve_puzzle(initialBoard : List[str] , algorithmNumber : int):

    
    numberOfNodesExpanded = 0
    maxNumberOfNodesInQueue = 0
    depthOfGoal = 0
    finalStateNode : StateNode
    
    visitedSet = set() # set of board lists
    
    array = np.array(initialBoard)
    twoDimArray = array.reshape((3,3))
    initialStateMap = dict()

    for i in range(len(twoDimArray)):
        for j in range(len(twoDimArray[i])):
            initialStateMap[twoDimArray[i][j]] = (i,j)
    

    initialState = StateNode(twoDimArray,None, initialStateMap, algorithmNumber, 0)
    print("Expanding state")
    print(twoDimArray)
    nodes = queue.PriorityQueue()
    nodes.put(initialState)

    while not nodes.empty():
        if(nodes.empty()):
            return False
        
        
        currentNode = nodes.get()

        visitedSet.add(tuple(map(tuple, currentNode.board2DArray)))


        # print(currentNode.board2DArray)
        # print()
        

        if(currentNode.isGoalState()):
            depthOfGoal = currentNode.depth
            maxNumberOfNodesInQueue = max(maxNumberOfNodesInQueue,nodes.qsize())
            return (numberOfNodesExpanded, maxNumberOfNodesInQueue, depthOfGoal, currentNode)
        
        
        newNodes = expand(currentNode, visitedSet)
        numberOfNodesExpanded += 1
        for eachNode in newNodes:
            newNode = StateNode(eachNode,currentNode,initialStateMap,algorithmNumber,currentNode.depth + 1)
            nodes.put(newNode)
        
        maxNumberOfNodesInQueue = max(maxNumberOfNodesInQueue,nodes.qsize())

        bestStateNode = nodes.queue[0]
        bestStateGn = bestStateNode.gn
        bestStateHn = bestStateNode.hn

        print(f"The best state to expand with g(n)={bestStateGn} and h(n)={bestStateHn} is")
        print(bestStateNode.board2DArray)
        print("Expanding this node...")

        print()
        print()

    
    return (numberOfNodesExpanded, maxNumberOfNodesInQueue, depthOfGoal, finalStateNode)

def expand(stateNode : StateNode, visitedSet) -> List[StateNode]:
    board = stateNode.board2DArray
    
    numRows = len(board)
    numCols = len(board[0])

    def findStar(board : List[List[str]], numRows, numCols) -> Tuple[int, int]:
    
        for i in range(numRows):
            for j in range(numCols):
                if board[i][j] == "0":
                    return (i,j)
        
        return (-1,-1) # will never run
    
    (starRowIndex, starColIndex) = findStar(board,numRows,numCols)

                        #   up   right  down   left
    indicesToMoveStar = [[0,-1],[1,0],[0,1], [-1,0]]

    arrayOfChildren = []

    for i in range(4):

        newStarRowIndex = starRowIndex + indicesToMoveStar[i][0]
        newStarColIndex = starColIndex + indicesToMoveStar[i][1]

        if 0 <= newStarRowIndex < numRows and 0 <= newStarColIndex < numCols:
            numberSwitched = board[newStarRowIndex][newStarColIndex]
            newBoard = copy.deepcopy(board)  # create a new copy of board
            newBoard[starRowIndex][starColIndex] = numberSwitched
            newBoard[newStarRowIndex][newStarColIndex] = "0"
            
            if tuple(map(tuple, newBoard)) not in visitedSet:
                arrayOfChildren.append(newBoard)
    
    return arrayOfChildren


print("Trivial")
result = solve_puzzle([["1","2","3"],
                   ["4","5","6"],
                   ["7","8","0"]],1)


print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
print(f"The depth of the goal node was {result[2]}")

print()
print("EXTRA CREDIT:")
list_of_states = returnListOfStates(result[3])

for eachState in list_of_states:
    print(eachState)
    print()


print("Very Easy")
result = solve_puzzle([["1","2","3"],
                   ["4","5","6"],
                   ["7","0","8"]],2)


print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
print(f"The depth of the goal node was {result[2]}")

print()
print("EXTRA CREDIT:")
list_of_states = returnListOfStates(result[3])

for eachState in list_of_states:
    print(eachState)
    print()


print("EASY")
result = solve_puzzle([["1","2","0"],
                   ["4","5","3"],
                   ["7","8","6"]],2)


print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
print(f"The depth of the goal node was {result[2]}")

print()
print("EXTRA CREDIT:")
list_of_states = returnListOfStates(result[3])

for eachState in list_of_states:
    print(eachState)
    print()

print("DOABLE")
result = solve_puzzle([["0","1","2"],
                   ["4","5","3"],
                   ["7","8","6"]],2)


print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
print(f"The depth of the goal node was {result[2]}")

print()
print("EXTRA CREDIT:")
list_of_states = returnListOfStates(result[3])

for eachState in list_of_states:
    print(eachState)
    print()


print("OH BOY")
result = solve_puzzle([["8","7","1"],
                   ["6","0","2"],
                   ["5","4","3"]],2)


print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
print(f"The depth of the goal node was {result[2]}")

print()
print("EXTRA CREDIT:")
list_of_states = returnListOfStates(result[3])

for eachState in list_of_states:
    print(eachState)
    print()

# IMPOSSIBLE
# result = solve_puzzle([["1","2","3"],
#                    ["4","5","6"],
#                    ["8","7","0"]],3)

# if(result == False):
#     print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
#     print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
#     print(f"The depth of the goal node was NOT POSSIBLE")  

# else: 
#     print(f"To solve this problem, the search algorithm expanded a total of {result[0]} nodes.")
#     print(f"The maximum number of nodes in the queue at any one time: {result[1]}")
#     print(f"The depth of the goal node was {result[2]}")

#     print()
#     print("EXTRA CREDIT:")
#     list_of_states = returnListOfStates(result[3])

#     for eachState in list_of_states:
#         print(eachState)
#         print()