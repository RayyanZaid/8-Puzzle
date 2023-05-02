from typing import List
from typing import Tuple
import copy



class StateNode:
    def __init__(self, board2DArray: List[List[str]], parent) -> None:
        self.board2DArray = board2DArray
        self.parent = parent


        self.gn = 0     # cost from start
        self.hn = 0     # PREDICTED cost until end
        self.fn = 0     # total cost



def findStar(board : List[List[str]], numRows, numCols) -> Tuple[int, int]:
    
    for i in range(numRows):
        for j in range(numCols):
            if board[i][j] == "*":
                return (i,j)
    
    return (-1,-1) # will never run
    


def expand(stateNode : StateNode) -> List[StateNode]:
    board = stateNode.board2DArray
    
    numRows = len(board)
    numCols = len(board[0])

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
            newBoard[newStarRowIndex][newStarColIndex] = "*"

            arrayOfChildren.append(newBoard)
    
    return arrayOfChildren

