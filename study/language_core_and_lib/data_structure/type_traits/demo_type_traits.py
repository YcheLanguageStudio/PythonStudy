import networkx as nx

if __name__ == '__main__':
    my_dict = {1: [2, 3]}
    if isinstance(my_dict, dict):
        print 'dict!'

    my_graph = nx.Graph()
    my_graph.add_edges_from([(1, 2), (2, 3)])
    print type(my_graph)

    my_graph = nx.DiGraph()
    print type(my_graph)
