import networkx as nx


def get_clone_list():
    with open('read_list.txt') as ifs:
        return map(lambda ele: ele.strip(), ifs.readlines())


def construct_graph(read_list):
    print 'read list:', read_list
    edge_list = map(lambda ele: (ele[:-1], ele[1:],), read_list)
    return nx.DiGraph(edge_list)


def get_post_process_graph(graph):
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
        assert graph.in_degree(v) == graph.out_degree(v)
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
        print 'find v with unvisited out edges, ',
        for v in in_path_v_list:
            if len(covered_out_edge_dict[v]) < graph.out_degree(v):
                local_path = [v]
                print 'expand from vertex:', v,
                last_v = local_path[-1]
                while len(local_path) == 1 or last_v != v:
                    for src, dst in graph.out_edges(last_v):
                        if dst not in covered_out_edge_dict[src]:
                            covered_out_edge_dict[src].append(dst)
                            local_path.append(dst)
                            in_path_v_list.add(dst)
                            last_v = local_path[-1]
                            break
                idx = global_path.index(v)
                print 'local path:', local_path
                global_path = global_path[0:idx] + local_path + global_path[idx + 1:]
                break
    return global_path


if __name__ == '__main__':
    graph, ret_tuple = get_post_process_graph(construct_graph(get_clone_list()))
    print 'vertex list:', graph.nodes(), '\n'

    check_connected_balanced(graph)
    v_list = get_euler_path(graph)

    print '\nadded extra edge:', ret_tuple, '\neuler cycle:', v_list

    for i in xrange(len(v_list) - 2):
        if v_list[i] == ret_tuple[0] and v_list[i + 1] == ret_tuple[1]:
            split_idx = i + 1
            break

    res_list = v_list[split_idx:] + v_list[1:split_idx]
    print 'euler path:', res_list
    print 'super str:', res_list[0][0] + ''.join(map(lambda ele: ele[1:], res_list))
