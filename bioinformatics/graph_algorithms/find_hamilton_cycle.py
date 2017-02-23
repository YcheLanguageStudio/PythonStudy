import networkx as nx
import itertools


def get_clone_list():
    with open('read_list.txt') as ifs:
        return map(lambda ele: ele.strip(), ifs.readlines())


def get_edge_list(clone_list):
    prefix_list = map(lambda ele: ele[:len(ele) - 1], clone_list)
    kmer_dict = {}
    for i, prefix in enumerate(prefix_list):
        if prefix not in kmer_dict:
            kmer_dict[prefix] = []
        kmer_dict[prefix].append(clone_list[i])
    print 'kmer_dict:', kmer_dict

    def form_edge_list(vertex):
        suffix = vertex[1:]
        if suffix not in kmer_dict:
            return []
        else:
            tmp_list = filter(lambda ele: ele[0] != ele[1], zip([vertex] * len(vertex[1:]), kmer_dict[vertex[1:]]))
            return tmp_list

    return list(itertools.chain(*map(form_edge_list, clone_list)))


def construct_graph():
    read_list = get_clone_list()
    edge_list = get_edge_list(read_list)
    print 'clone list:', read_list
    print 'edge list:', edge_list
    return nx.DiGraph(edge_list)


def dfs_detail(data_graph, record_path, mark_set):
    """
    :type data_graph: nx.DiGraph
    """
    if len(record_path) == data_graph.number_of_nodes():
        super_str = record_path[0][:len(record_path[0]) - 1] + ''.join(map(lambda ele: ele[-1], record_path))
        print 'path:', record_path, 'super str:', super_str
    else:
        for src_v, dst_v in data_graph.out_edges(record_path[-1]):
            if dst_v not in mark_set:
                record_path.append(dst_v)
                mark_set.add(dst_v)
                dfs_detail(data_graph, record_path, mark_set)
                mark_set.remove(dst_v)
                record_path.pop(-1)
        return


if __name__ == '__main__':
    graph = construct_graph()
    for start_vertex in graph.nodes():
        dfs_detail(graph, [start_vertex], {start_vertex})
