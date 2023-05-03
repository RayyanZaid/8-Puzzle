from typing import List
import queue
from StateNodeClass import StateNode

def solve_puzzle(intialBoard : List[str] , algorithmNumber : int):

    numberOfNodesExpanded = 0
    maxNumberOfNodesInQueue = 0
    depthOfGoal = 0
    finalStateNode = 0
    
    nodes = queue.PriorityQueue()

    while not nodes.empty():
        if(nodes.empty()):
            return "False"
        print(item)

    return (numberOfNodesExpanded, maxNumberOfNodesInQueue, depthOfGoal, finalStateNode)
