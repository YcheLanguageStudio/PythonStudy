import networkx as nx

g = nx.Graph()
fin = open("./edge_list2.txt")
for l in fin:
    l = l.rstrip().split(" ")
    g.add_edge(l[0], l[1])

print '\n'
print g.number_of_nodes()
graphs = list(nx.connected_component_subgraphs(g))

print len(graphs)

print 100000 - g.number_of_nodes() + len(graphs)
