#this problem contains two graphs where graph_01 has a negative edge but no
#negative cycle, whereas the graph_02 has both negative edge and negative
#cycle. 
#Therefore when Bellman Ford algorithm is applied onto both the graph it
#returns the array of the solutions i.e array of the distances for ex:
#shortes path to vertex[i] from root node is solution[i] here solution is
#solution array, therefore if root node is vertex[n] then solution[n] = 0
#as solution[n] represents root node itself
#if there is a no solution i.e if there is negative cycle this program
#prints and let knows user that there is a negative cycle and returns None

class Graph:
    def __init__(self,vertices,edges):
        self.vertices = vertices
        self.edges = edges
    def get_weight(self,node_1,node_2):
        index_1 = self.vertices.index(node_1)
        index_2 = self.vertices.index(node_2)
        return self.edges[index_1][index_2]
    def djkstra(self,solution_list):
        l = len(self.vertices)
        for i in range(0,l):
            for j in range(0,l):
                if self.edges[i][j] != 0:
                    solution_list[j] = min(solution_list[j],
                    solution_list[i] + 
                    self.get_weight(self.vertices[i],self.vertices[j]))
        return solution_list
    def Bellman_Algo(self,root_node):
        if root_node not in self.vertices:
            print("Please give proper node")
        else:
            n = len(self.vertices)
            inf = float('inf')
            solution_list = [inf for l in range(n)]
            solution_list[self.vertices.index(root_node)] = 0
            for i in range(n-1):
                solution_list = self.djkstra(solution_list)
            check_list = []
            for cost in solution_list:
                check_list.append(cost)
            check_list = self.djkstra(check_list)
            if check_list != solution_list:
                print("No solution! as there is a negative cycle in the graph when root_node is",root_node)
                return None
            return solution_list


#Graph_01
vertices_01 = [ 1, 2, 3, 4, 5]
edges_01 =   [[ 0, 3, 8, 0,-4], #1  1->1, 1->2, 1->3.....
              [ 0, 0, 0, 1, 7], #2  2->1, 2->2, 2->3.....
              [ 0, 4, 0, 0, 0], #3
              [ 2, 0,-5, 0, 0], #4
              [ 0, 0, 0, 6, 0]] #5


#Graph_02
vertices_02 = [1,2,3,4]
edges_02 = [[0, 4, 0, 5],
            [0, 0, 0, 5],
            [0,-10,0, 0],
            [0, 0, 3, 0]]

graph_01 = Graph(vertices_01,edges_01)
graph_02 = Graph(vertices_02,edges_02)

print(graph_01.Bellman_Algo(2))
print(graph_02.Bellman_Algo(2))

