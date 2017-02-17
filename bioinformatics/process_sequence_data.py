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
