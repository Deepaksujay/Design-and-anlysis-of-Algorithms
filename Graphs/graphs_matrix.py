def check(tally):
    for node in tally:
        if node == 0:
            return 1
    return 0

def dijkstras_algo(graph,spt,tally,num):
    if len(tally) != num :
        #print(spt)
        spt_column = [row[0] for row in spt]
        node_main = min(spt,key = lambda x : x[1])
        node = node_main[0]
        node_index = spt_column.index(node)
        adjacent_indeces = graph.get_adjacents_of(node)
        for index in adjacent_indeces:
            adjacent_node = graph.vertices[index]
            if adjacent_node in spt_column:
                adjacent_ind = spt_column.index(adjacent_node)
                weight = graph.get_weight(node,graph.vertices[index])
                if (spt[node_index][1]+weight < spt[adjacent_ind][1]):
                    spt[adjacent_ind][1] = spt[node_index][1]+weight
                    spt[adjacent_ind][2] = node
        tally.append(node_main)
        spt.remove(node_main)
        return dijkstras_algo(graph,spt,tally,num)
    else:
        return tally

    

def dijkstras(graph,node): #index is index of node in vertice list
    spt,tally = [],[]
    infinity = float('inf')
    for vertice in graph.vertices:
        if vertice != node:
            spt.append([vertice,infinity,""])
        else:
            spt.append([vertice,0,node])
    return dijkstras_algo(graph,spt,tally,len(spt))

class Graph_Matrix:
    def __init__(self,vertices,edges):
        self.vertices = vertices
        self.edges = edges
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
    def get_weight(self,node_1,node_2):
        if node_1 in self.vertices and node_2 in self.vertices:
            index_1 = self.vertices.index(node_1)
            index_2 = self.vertices.index(node_2)
            w_1 = self.edges[index_1][index_2]
            return w_1
        else:
            return "Recheck the entered nodes,They aren't in graph!"
    def get_shortest_route(self,node_1,node_2):
        try:
            Info_list = dijkstras(self,node_1)
            Info_column_0 = [info[0] for info in Info_list]
            node_temp = node_2
            dist = Info_list[Info_column_0.index(node_2)]
            solution_list,distance = [],dist[1]
            solution_list.append(node_temp)
            while node_temp != node_1:
                if node_temp in Info_column_0:
                    required_row = Info_list[Info_column_0.index(node_temp)]
                    solution_list.append(required_row[2])
                    node_temp = required_row[2]
            return solution_list[::-1],distance
        except:
            print("Something went wrong")
            

vertices = ['a','b','c','d','e','f','g','h','i']
#           a b c d e f g h i
edges =   [[0,3,0,2,0,0,0,0,4], # a
           [3,0,0,0,0,0,0,4,0], # b it is b->a, b->h but not a->b
           [0,0,0,6,0,1,0,2,0], # c  here arrow is from row name to column name
           [2,0,6,0,1,0,0,0,0], # d
           [0,0,0,1,0,0,0,0,8], # e
           [0,0,1,0,0,0,8,0,0], # f
           [0,0,0,0,0,8,0,0,0], # g
           [0,4,2,0,0,0,0,0,0], # h
           [4,0,0,0,8,0,0,0,0]] # i

vertices_2 = ['a','b','c','d','e','f']
#           a b c d e f
edges_2 = [[0,2,4,0,0,0], # a  a->b and a->c
           [0,0,1,7,0,0], # b  b->c and b->d
           [0,0,0,0,3,0], # c
           [0,0,0,0,0,1], # d
           [0,0,0,2,0,5], # e
           [0,0,0,0,0,0]] # f

graph_1 = Graph_Matrix(vertices,edges)
graph_2 = Graph_Matrix(vertices_2,edges_2)
# print(dijkstras(graph_1,'g'))
# print(dijkstras(graph_2,'a'))
order,distance = graph_1.get_shortest_route('a','g')
print(order,distance)

# infinity = float('inf')
# spt = []
# for i in range(0,10):
#     spt.append(["a",infinity])
# spt.append(["b",0])
# see = [spts[0] for spts in spt]
# print(see.index('b'))
# print(spt)
# node = max(spt,key = lambda x : x[1])[0]
# print(node)