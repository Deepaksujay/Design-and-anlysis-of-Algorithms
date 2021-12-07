class Node:
    def __init__(self,name,frequency,left = None, right = None,huff = ''):
        self.name = name
        self.f = frequency
        self.left = left
        self.right = right
        self.huff = huff

def GetSolutionTable(node,sol,val = ''):
    code = val + node.huff
    if (not node.right and not node.left):
        sol.append([node.name,code])
    if node.left:
        GetSolutionTable(node.left,sol,code)
    if node.right:
        GetSolutionTable(node.right,sol,code)
    return sol

def CreateNodes(table):
    NodeList = []
    for row in table:
        NodeList.append(Node(row[0],row[1]))
    return NodeList

def Huffman_Comp_Algo(table):
    NodeList = CreateNodes(table)
    while len(NodeList) != 1:
        NodeList.sort(key = lambda x : x.f)
        left = NodeList[0]
        right = NodeList[1]
        left.huff = '0'
        right.huff = '1'
        NewNode = Node(left.name+right.name,left.f+right.f,left, right)
        NodeList.remove(left)
        NodeList.remove(right)
        NodeList.append(NewNode)
    Solution = []
    return GetSolutionTable(NodeList[0],Solution)


table = [['a',12],['b',2],['c',7],['d',13],['e',14],['f',85]]
SolutionTable = Huffman_Comp_Algo(table)
print(SolutionTable)
