class Point:
    """
	Exemple d'utilisation
		sommet = Point(x, y)
		id = sommet.getID()
		x, y = sommet.getCoords()		
	"""
    ID = 0 # Attribut UNIQUE d'identification de chaque point
    def __init__(self, x, y):
        # Init
        self.x = x
        self.y = y
        self.id = Point.ID
        Point.ID += 1
    def getID(self): return self.id
    def getCoords(): return self.x, self.y

class Chemin :
    # ok
    def __init__(self, pointInitial, pointFinal, poids):
        self.start = pointInitial
        self.final = pointFinal
        self.weight = poids
        
    def getChemin(self): 
        print(self.start.getID(), self.final.getID(), self.weight)
        return (self.start.getID(), self.final.getID(), self.weight)
        
    def getStart(self): return self.start

    def getFinal(self): return self.final

    def getWeight(self): return self.weight

# Classe du graphe
class Graph: 

	def __init__(self, vertices): 
		self.V = vertices # Number of vertices 
		self.graph = [] 
		self.parent = [None] * self.V

	# function to add an edge to graph 
	def addEdge(self, u, v, w): 
		self.graph.append([u, v, w]) 
	
	def addChemin(self, chemin): 
		self.graph.append(chemin.getChemin())
	# utility function used to print the solution 
	def printArr(self, dist): 
		print("\n Pondérations du point  SOURCE vers tous les autres POINTS") 
		for i in range(self.V): 
			print("{0}\t\t{1}".format(i, dist[i])) 
	
	# The main function that finds shortest distances from src to 
	# all other vertices using Bellman-Ford algorithm. The function 
	# also detects negative weight cycle 
	def BellmanFord(self, src): 

		# Step 1: Initialize distances from src to all other vertices 
		# as INFINITE 
		dist = [float("Inf")] * self.V 
		dist[src] = 0
		# parent = [None] * self.V

		# Step 2: Relax all edges |V| - 1 times. A simple shortest 
		# path from src to any other vertex can have at-most |V| - 1 
		# edges 
		for _ in range(self.V - 1): 
			# Update dist value and parent index of the adjacent vertices of 
			# the picked vertex. Consider only those vertices which are still in 
			# queue 
			for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
						dist[v] = dist[u] + w
						self.parent[v] = u

		# Step 3: check for negative-weight cycles. The above step 
		# guarantees shortest distances if graph doesn't contain 
		# negative weight cycle. If we get a shorter path, then there 
		# is a cycle. 

		for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
						print("Graph contains negative weight cycle") 
						return
						
		# print all distance 
		self.printArr(dist) 

	def PathPrinting(self, u) :
		v = self.parent[u]
		if v is None:
		    return
		self.PathPrinting(v)
		print(u)


g = Graph(6) 
# g.addEdge(0, 1, -1) 
# g.addEdge(0, 2, 4) 
# g.addEdge(1, 2, 3) 
# g.addEdge(1, 3, 2) 
# g.addEdge(1, 4, 2) 
# g.addEdge(3, 2, 5) 
# g.addEdge(3, 1, 1) 
# g.addEdge(4, 3, -3) 

p0 = Point(0, 5)
p1 = Point(10, -84)
p2 = Point(95, 4)
p3 = Point(54, -9)
p4 = Point(-2, 0)
p5 = Point(0, 0)

print('A - B - poids') 
g.addChemin(Chemin(p0, p1, -1)) 
g.addChemin(Chemin(p0, p2, 4)) 
g.addChemin(Chemin(p1, p2, 3)) 
g.addChemin(Chemin(p1, p3, 2)) 
g.addChemin(Chemin(p1, p4, 2)) 
g.addChemin(Chemin(p3, p2, 5)) 
g.addChemin(Chemin(p3, p1, 1)) 
g.addChemin(Chemin(p4, p3, -3)) 
g.addChemin(Chemin(p4, p5, 1)) 

# Print the solution
g.BellmanFord(0)

print('Points à passer pour aller à celui d\'ID ', 5)
g.PathPrinting(5)
# Initially, Contributed by Neelam Yadav 
# Later On, Edited by Himanshu Garg 
