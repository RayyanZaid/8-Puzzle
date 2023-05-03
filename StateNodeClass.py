from typing import List
from typing import Tuple
import copy
import math


class StateNode:
    def __init__(self, board2DArray: List[List[str]], parent, initialStateMap, algorithmNumber) -> None:
        self.board2DArray = board2DArray
        self.parent = parent


        self.gn = distanceFromStart(self.board2DArray, initialStateMap)   # cost from start
        self.hn : float     # PREDICTED cost until end

        if(algorithmNumber == 1):
            self.hn = 0
        
        if(algorithmNumber == 2):
            self.hn = misplacedTileHeuristic(self.board2DArray)
        
        if(algorithmNumber == 3):
            self.hn = euclideanDistanceHeuristic(self.board2DArray)

        self.fn = self.gn + self.hn    # total cost

    def isGoalState(self) -> bool:
        
        count = 1
        for i in range(len(self.board2DArray)):
            for j in range(len(self.board2DArray[i])):

                if(i == len(self.board2DArray) - 1 and j == len(self.board2DArray[i]) - 1):
                   return True
                
                if(str(count) != self.board2DArray[i][j]):
                    return False
                
                count+=1

    def __lt__(self,other):
        return self.hn <= other.hn

    


def expand(stateNode : StateNode) -> List[StateNode]:
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

            arrayOfChildren.append(newBoard)
    
    return arrayOfChildren

def misplacedTileHeuristic(board : List[List[str]]):

    count = 1

    numMisplacedTiles = 0

    for i in range(len(board)):
        for j in range(len(board[i])):

            if(i == len(board) - 1 and j == len(board) - 1):
                break
            else:
                if(board[i][j] != str(count)):
                    numMisplacedTiles+=1
                
            count += 1
    
    return numMisplacedTiles
            



def euclideanDistanceHeuristic(board : List[List[str]]):

    numToIndices = {
        "1" : (0,0),
        "2" : (0,1),
        "3" : (0,2),
        "4" : (1,0),
        "5" : (1,1),
        "6" : (1,2),
        "7" : (2,0),
        "8" : (2,1),
        "0" : (2,2),

    }

    distanceToEnd = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            num = board[i][j]

            if(num == "0"):
                continue

            (correct_i , correct_j) = numToIndices[num]

            distanceToEnd += math.sqrt(math.pow((correct_i - i),2) + math.pow((correct_j - j),2))

    return distanceToEnd

def distanceFromStart(board, numToIndices : dict()):
    distanceFromStart = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            num = board[i][j]

            if(num == "0"):
                continue

            (correct_i , correct_j) = numToIndices[num]

            distanceFromStart += math.sqrt(math.pow((correct_i - i),2) + math.pow((correct_j - j),2))

    return distanceFromStart

# node = StateNode([["1","2","3"],
#                   ["4","0","6"],
#                   ["7","5","8"]],
                  
#                   None, 
                  
#                   initialStateMap=
#                   {"1" : (0,0),
#                    "2" : (0,1),
#                    "3" : (0,2),
#                    "4" : (1,0),
#                    "6" : (1,1),
#                    "0" : (1,2),
#                    "7" : (2,0),
#                    "5" : (2,1),
#                    "8" : (2,2)}, 
                   
#                    algorithmNumber=3)

# # print(euclideanDistanceHeuristic(node.board2DArray))

# print(node.hn)
