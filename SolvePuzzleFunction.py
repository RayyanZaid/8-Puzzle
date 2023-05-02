from typing import List


def solve_puzzle(initialBoard : List[List[str]] , algorithmNumber : int):

    # variables that need to be returned 

    numberOfNodesExpanded = 0
    maxNumberOfNodesInQueue = 0
    depthOfGoal = 0
    finalStateNode = 0
    isSuccessful = False
    
    # create queue

    node_queue = [initialBoard]

    while node_queue:
        if len(node_queue) == 0:
            return (numberOfNodesExpanded, maxNumberOfNodesInQueue, depthOfGoal, finalStateNode, isSuccessful)


    isSuccessful = True
    return (numberOfNodesExpanded, maxNumberOfNodesInQueue, depthOfGoal, finalStateNode, isSuccessful)
