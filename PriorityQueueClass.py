# from typing import List
# from typing import Tuple
# import copy
# import math
# import queue


# class PriorityQueue:
# 	def __init__(self):
# 		self.queue = []
		

# 	def rearrange(self):
# 		self.

# 	def isEmpty(self):
# 		return len(self.queue) == 0
	
# 	def enqueue(self, newNode):
# 		self.queue.append(newNode)
# 		#rearrange 

# 	def popCheapest(self):
# 		#rearrange 
# 		return self.queue.get()

# 	def heapSort(self):
# 		#rearrange by f(n)

import queue
from StateNodeClass import StateNode

pq = queue.PriorityQueue()


top = StateNode([["1","2","3"],
                  ["4","0","6"],
                  ["7","5","8"]],
                  
                  None, 
                  
                  initialStateMap=
                  {"1" : (0,0),
                   "2" : (0,1),
                   "3" : (0,2),
                   "4" : (1,0),
                   "6" : (1,1),
                   "0" : (1,2),
                   "7" : (2,0),
                   "5" : (2,1),
                   "8" : (2,2)}, 
                   
                   algorithmNumber=3)

child1 = StateNode([["1","2","3"],
                  ["4","5","6"],
                  ["7","0","8"]],
                  
                  top, 
                  
                  initialStateMap=
                  {"1" : (0,0),
                   "2" : (0,1),
                   "3" : (0,2),
                   "4" : (1,0),
                   "6" : (1,1),
                   "0" : (1,2),
                   "7" : (2,0),
                   "5" : (2,1),
                   "8" : (2,2)}, 
                   
                   algorithmNumber=3)

grandChild  = StateNode([["1","2","3"],
                  ["4","5","6"],
                  ["7","8","0"]],
                  
                  child1, 
                  
                  initialStateMap=
                  {"1" : (0,0),
                   "2" : (0,1),
                   "3" : (0,2),
                   "4" : (1,0),
                   "6" : (1,1),
                   "0" : (1,2),
                   "7" : (2,0),
                   "5" : (2,1),
                   "8" : (2,2)}, 
                   
                   algorithmNumber=3)

pq.put(child1)
pq.put(grandChild)
pq.put(top)



	