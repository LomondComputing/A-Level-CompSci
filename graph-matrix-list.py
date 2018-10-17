# Program to implement a graph in terms of adjacency matrices and lists

def isEdge(graph,a,b):
     foundA = False
     i = 0
     while not foundA and i < len(graph):
           if graph[i][0] == a:
                foundB = False
                j = 0
                while not foundB and j < len(graph[i][1]):
                     if graph[i][j] == b:
                          foundB = True
     return foundA and foundB
          
aMatrix = [[None for col in range(6)] for row in range(6)]
aMatrix[0][1] = 5
aMatrix[0][2] = 4
aMatrix[1][2] = 6
aMatrix[1][3] = 3
aMatrix[2][5] = 8
aMatrix[3][4] = 2

aList = ( ('A',(('B',5),('C',4))),
          ('B',(('C',6),('D',3))),
          ('C',(('F',8))),
          ('D',(('E',2))),
          ('E',()),
          ('F',())
          )

print(isEdge(aList,'B','D'))
           
