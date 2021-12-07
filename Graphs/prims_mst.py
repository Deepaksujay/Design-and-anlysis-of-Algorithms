class Graph:
    def __init__(self,vertices,edges):
        self.vertices = vertices
        self.edges = edges
    def get_weight(self,node_1,node_2):
        if node_1 in self.vertices and node_2 in self.vertices:
            index_1 = self.vertices.index(node_1)
            index_2 = self.vertices.index(node_2)
            w_1 = self.edges[index_1][index_2]
            return w_1
        else:
            return "Recheck the entered nodes,They aren't in graph!"
    def get_adjacents_of(self,element): #returns list with indices of adjacent nodes according to vertices list
        if element in self.vertices:
            index = self.vertices.index(element)
            indexes = []
            for edge in self.edges[index]:
                if edge != 0:
                    index_ver = self.edges[index].index(edge)
                    indexes.append(index_ver)
            return indexes
        else:
            print("Sorry there is no such edge in this graph")
    def __prims_sub(self,mst_updated,main_list):
        if  main_list:
            min_data = min(main_list,key = lambda x : x[2])
            adjacents = self.get_adjacents_of(min_data[0])
            for adjacent in adjacents:
                node = self.vertices[adjacent]
                adjacent = node
            for row in main_list:
                if row[0] in adjacents:
                    weight = self.get_weight(min_data[0],row[0])
                    if row[2] > weight:
                        row[2] = weight
                        row[1] = min_data[0]
            mst_updated.append(min_data)
            main_list.remove(min_data)
            return self.__prims_sub(mst_updated,main_list)
        else:
            return mst_updated
    def prims_algo(self,source_node):  #The main algorithm it takes source manually from user
        mst_updated,main_list = [],[]
        inf = float('inf')
        for vertex in self.vertices:
            if vertex == source_node:
                main_list.append([vertex,source_node,0]) 
            else:
                main_list.append([vertex,source_node,inf]) 
        return self.__prims_sub(mst_updated,main_list)

vertices = [0,1,2,3,4,5,6,7,8]
#           0 1 2 3 4 5 6 7 8 
edges =   [[0,3,0,2,0,0,0,0,4], # 0
           [3,0,0,0,0,0,0,4,0], # 1 it is b->a, b->h but not a->b
           [0,0,0,6,0,1,0,2,0], # 2  here arrow is from row name to column name
           [2,0,6,0,1,0,0,0,0], # 3
           [0,0,0,1,0,0,0,0,8], # 4
           [0,0,1,0,0,0,8,0,0], # 5
           [0,0,0,0,0,8,0,0,0], # 6
           [0,4,2,0,0,0,0,0,0], # 7
           [4,0,0,0,8,0,0,0,0]] # 8

vertices_2 = [0,1,2,3,4,5,6,7,8]
#             0  1  2  3  4  5  6  7  8 
edges_2 =   [[0, 4, 0, 0, 0, 0, 0, 8, 0],  # 0
             [4, 0, 8, 0, 0, 0, 0,11, 0],  # 1 it is b->a, b->h but not a->b
             [0, 8, 0, 7, 0, 4, 0, 0, 2],  # 2  here arrow is from row name to column name
             [0, 0, 7, 0, 9,14, 0, 0, 0],  # 3
             [0, 0, 0, 9, 0,10, 0, 0, 0],  # 4
             [0, 0, 4,14,10, 0, 2, 0, 0],  # 5
             [0, 0, 0, 0, 0, 2, 0, 1, 6],  # 6
             [8,11, 2, 0, 0, 0, 1, 0, 7],  # 7
             [0, 0, 2, 0, 0, 0, 6, 7, 0]]  # 8

graph_1 = Graph(vertices,edges)
graph_2 = Graph(vertices_2,edges_2)
list = graph_1.prims_algo(0)
print(list)
list = graph_2.prims_algo(0)
print(list)
#list will be in this order "node-node's parent node-cost"

