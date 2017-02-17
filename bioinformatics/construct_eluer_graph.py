import networkx as nx
from process_sequence_data import *


def construct_graph():
    read_list = get_clone_list()
    print read_list
    edge_list = map(lambda ele: (ele[:-1], ele[1:],), read_list)
    return nx.DiGraph(edge_list)


def get_post_process_graph():
    graph = construct_graph()
    odd_v_list = filter(lambda v: graph.degree(v) % 2 == 1, graph.nodes())
    if graph.out_degree(odd_v_list[0]) - graph.in_degree(odd_v_list[0]) < 0:
        graph.add_edge(odd_v_list[0], odd_v_list[1])
        ret_tuple = odd_v_list[0], odd_v_list[1]
    else:
        graph.add_edge(odd_v_list[1], odd_v_list[0])
        ret_tuple = odd_v_list[1], odd_v_list[0]
    return graph, ret_tuple


def check_connected_balanced(graph):
    """
    :type graph: nx.DiGraph
    """
    for v in graph.nodes():
        print graph.in_degree(v), graph.out_degree(v)
    sub_graph_list = nx.weakly_connected_component_subgraphs(graph, True)
    for sub_graph in sub_graph_list:
        print sub_graph.edges()


def get_euler_path(graph):
    """
    :type graph: nx.DiGraph
    """
    start_v = graph.nodes()[0]
    global_path, in_path_v_list = [start_v], {start_v}
    covered_out_edge_dict = dict()
    for v in graph.nodes():
        covered_out_edge_dict[v] = []

    while len(global_path) < graph.number_of_edges() + 1:
        # print 'find v with unvisited out edges'
        for v in in_path_v_list:
            if len(covered_out_edge_dict[v]) < graph.out_degree(v):
                local_path = [v]
                # print 'expand'
                last_v = local_path[-1]
                while len(local_path) == 1 or last_v != v:
                    last_v = local_path[-1]
                    for src, dst in graph.out_edges(last_v):
                        if dst not in covered_out_edge_dict[src]:
                            covered_out_edge_dict[src].append(dst)
                            local_path.append(dst)
                            in_path_v_list.add(dst)
                            break
                idx = global_path.index(v)
                global_path = global_path[0:idx] + local_path + global_path[idx + 1:]
                break
    return global_path


if __name__ == '__main__':
    graph, ret_tuple = get_post_process_graph()
    check_connected_balanced(graph)
    v_list = get_euler_path(graph)
    print ret_tuple
    print v_list

    for i in xrange(len(v_list) - 2):
        if v_list[i] == ret_tuple[0] and v_list[i + 1] == ret_tuple[1]:
            split_idx = i + 2
            break

    res_list = v_list[split_idx:] + v_list[1:split_idx - 2]
    print res_list
    print 'super str:', res_list[0][0] + ''.join(map(lambda ele: ele[1:], res_list))
