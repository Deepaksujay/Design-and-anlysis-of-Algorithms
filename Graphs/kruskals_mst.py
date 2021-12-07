class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.edges = []
    def add_edge(self,a,b,cost): #a->b
        if a in self.vertices and b in self.vertices:
            edge = len(self.edges) 
            if edge == 0:
                self.edges.append([a,b,cost])
            elif edge > 0:
                data = self.edges[edge-1]
                while data[2] < cost:
                    if edge == 0:
                        break
                    edge = edge - 1
                self.edges.insert(edge,[a,b,cost])
        else:
            print("This node doesn't exist in vertices list provided")
    def get_weight(self,a,b):
        for edge in self.edges:
            if edge[0] == a and edge[1] == b:
                return edge[2]
        return 0
    def get_adjacents_of(self,a):
        adjacents = []
        for edge in self.edges:
            if edge[0] == a:
                adjacents.append(edge)
        return adjacents
    def __check_circle(self,a,main_list,main_node,parent):
        for node in main_list:
            if node[0] == a:
                if node[1] == main_node:
                    return 0
                elif node[1] != parent:
                    if self.__check_circle(node[1],main_list,main_node,node[0]) == 0:
                        return 0
            elif node[1] == a:
                if node[0] == main_node:
                    return 0
                elif node[0] != parent:
                    if self.__check_circle(node[0],main_list,main_node,node[1]) == 0:
                        return 0
        return 1
    def kruskals_mst(self):
        main_list,e,least = [],0,len(self.edges)-1
        EDGES_NO = len(self.vertices) 
        while e < EDGES_NO and least > -1 :
            node = self.edges[least]
            if self.__check_circle(node[0],main_list,node[1],node[0]) :
                main_list.append(node)
                e = e + 1
            least = least - 1
        return main_list


def add_all_edges(graph,edges):
    for edge in edges:
        for cost in range(0,len(edge)):
            if edge[cost] != 0:
                node_1_index = edges.index(edge)
                graph.add_edge(graph.vertices[node_1_index],graph.vertices[cost],edge[cost])

vertices = [0,1,2,3,4,5,6,7,8]
#             0  1  2  3  4  5  6  7  8 
edges   =   [[0, 4, 0, 0, 0, 0, 0, 8, 0],  # 0
             [0, 0, 8, 0, 0, 0, 0,11, 0],  # 1 it is b->a, b->h but not a->b
             [0, 0, 0, 7, 0, 4, 0, 0, 2],  # 2  here arrow is from row name to column name
             [0, 0, 0, 0, 9,14, 0, 0, 0],  # 3
             [0, 0, 0, 0, 0,10, 0, 0, 0],  # 4
             [0, 0, 0, 0, 0, 0, 2, 0, 0],  # 5
             [0, 0, 0, 0, 0, 0, 0, 1, 6],  # 6
             [0, 0, 0, 0, 0, 0, 0, 0, 7],  # 7
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 8

#list will be in this order "node -- node's parent node -- cost"
graph = Graph(vertices)
add_all_edges(graph,edges)
print(graph.kruskals_mst())





