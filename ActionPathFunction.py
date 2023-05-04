from typing import List
from StateNodeClass import StateNode

def returnListOfStates(node: StateNode) -> List[List[List[str]]]:
    listOfStates : List[List[List[str]]] = [[[]]]
    


    def trace_back_to_uppermost_parent(node: StateNode) -> StateNode:
        listOfStates.insert(0,node.board2DArray)
        if node.parent is None:
            return node
        else:
            return trace_back_to_uppermost_parent(node.parent)

    trace_back_to_uppermost_parent(node)


    return listOfStates


# top = StateNode([["1","2","3"],
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

# child1 = StateNode([["1","2","3"],
#                   ["4","5","6"],
#                   ["7","0","8"]],
                  
#                   top, 
                  
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

# grandChild  = StateNode([["1","2","3"],
#                   ["4","5","6"],
#                   ["7","8","0"]],
                  
#                   child1, 
                  
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

