# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	# function to add an edge to graph 
# Make a list visited[] to check if a node is already visited or not 
	def addEdge(self,u,v): 
		self.graph[u].append(v)
		 
		self.visited=[] 

	# Function to print a BFS of graph 
	def BFS(self, s): 
        
		# Create a queue for BFS 
		queue = [] 

		# Add the source node in 
		# visited and enqueue it 
		queue.append(s) 
		self.visited.append(s) 

		while queue: 

			# Dequeue a vertex from 
			# queue and print it 
			s = queue.pop(0) 
			print (s, end = " ") 

			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then add it 
			# in visited and enqueue it 
			for i in self.graph[s]: 
				if i not in self.visited: 
					queue.append(i) 
					self.visited.append(s) 

# Driver code 

# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
g.BFS(2) 

# This code is contributed by Neelam Yadav 
