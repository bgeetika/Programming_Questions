#https://coderpad.io/P7TTM37W
class Node:
    WHITE = 0
    BLACK = 1
    GREY = 2

    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.color = self.WHITE
        self.level = 0


class Graph:
    t = 0
    def __init__(self):
        self.__node_list = {}

    def populate_graph(self, adjacency_matrix):
        '''
        It helps in creating a graph given it's adjacency matrix.
        '''
        for v in adjacency_matrix:
            n = Node(v)
            print type(v)
            self.__node_list[v] = n
        for v, val in adjacency_matrix.iteritems():
            n = self.__lookup_node(v)
            temp = []
            for name in val:
                nod = self.__lookup_node(name)
                temp.append(nod)
            n.neighbors = temp

    def  __lookup_node(self, data):
        return self.__node_list[data] 
    
    # Use colors to find back, cross and tree edges.
    
    
    def dfs(self, name):
        timestamp = {}
        for n in self.__node_list.values():
            n.color = Node.WHITE
        node = self.__lookup_node(name)
        path = []
        return self.__dfs_call(node, path)
    
    
    def dfs_forest(self):
        path = []
        timestamp = {}
        is_cycle =  False
        for n in self.__node_list.values():
            n.color = Node.WHITE
        for n in self.__node_list.values():
            if n.color == Node.WHITE:
                  iscycle, path, timestamp =  self.__dfs_call(n, path, timestamp) 
                  is_cycle = iscycle or is_cycle
        return is_cycle, path, timestamp
    
    def __dfs_call(self, n, path, timestamp):
        #global t
        flag = False
        n.color = Node.GREY
        path.append(n.data)
        for nod in n.neighbors:
            if nod.color == Node.GREY:
                print "back_edge: " + str(n.data) + "->" + str(nod.data)
                flag = True
                print "flag set"
            elif nod.color == Node.BLACK:
                pass
                print "cross_edge: " + str(n.data) + "->" + str(nod.data)
            elif nod.color == Node.WHITE:
                flag1, path, timestamp = self.__dfs_call(nod, path, timestamp)
                print str(flag1) + "geet"
                flag = flag1 or flag
        print "flag here: " + str(flag)
        n.color = n.BLACK
        self.t = self.t + 1
        timestamp[n] = self.t
        return flag, path, timestamp
    
    
    
    
    def bfs_path(self, name, dest):
        for n in self.__node_list.values():
            n.color = Node.WHITE
        que = []
        node = self.__lookup_node(name)
        node.color = Node.BLACK
        node_parent = {}
        n_w =  self.__lookup_node(dest)
        que.append(node)
        while len(que) > 0:
            n  = que.pop(0)
            #print n.data
            if n.data == dest:
                break
            for nod in n.neighbors:
                if nod.color == Node.WHITE:
                    nod.level = n.level + 1
                    nod.color = Node.BLACK
                    node_parent[nod] = n
                    que.append(nod)
        self.trace_path(n_w, node, node_parent)
        
        
    def trace_path(self , node2, node1, node_parent):
         #print node2.data,node1.data
         node = node2
         print node.data
         while node.data != node1.data:
            print node_parent[node].data
            node = node_parent[node]
         #print node.data
        
            
                    
    def bfs(self, name):
        for n in self.__node_list.values():
            n.color = Node.WHITE
        que = []
        node = self.__lookup_node(name)
        node.color = Node.BLACK
        que.append(node)
        while len(que) > 0:
            n  = que.pop(0)
            #print n.data
            for nod in n.neighbors:
                if nod.color == Node.WHITE:
                    nod.level = n.level + 1
                    n.color = Node.BLACK
                    que.append(nod)
                elif nod.level != n.level:
                    print "not a tree edge" + nod.data + "->" + n.data



def make_adjacency(n, prereq):
    vertex = set()
    adjacency = {}
    for val in prereq:
        if val[0] not in vertex:
            vertex.add(val[0])
        if val[1] not in vertex:
            vertex.add(val[1])
        adjacency.setdefault(val[0], []).append(val[1])
    
    for v in vertex:
        if v not in adjacency:
            adjacency[v] = []
    print adjacency
    print vertex
    return  adjacency, vertex
    
    
    
prereq = [[1,0],[2,0],[0,1]]
adjacency,vertex = make_adjacency(5,prereq)
    
    

g = Graph()
#g.populate_graph(adjacency_matrix)
g.populate_graph(adjacency)

'''
Printing graph to check if it getting populated properly or not
'''
'''for v in g.node_list:
    print v.data,
    for val in v.neighbors:
        print val.data,
    print "\n"
''' 
start_node = "102"
#g.dfs(start_node)
out, path, timestamp = g.dfs_forest()
print out

# for togological sort

if  not out:
    print "There is no Cycle"
    vals =  sorted(timestamp, key=timestamp.get)
    for v in vals:
        print v.data
    print path[::-1]
else:
    print "There is a cycle in a graph so it is not possible"
    
#g.bfs_path("F", "B")






