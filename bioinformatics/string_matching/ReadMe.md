#String Matching
##Suffix Tree
###Some Concepts

- For `SuffixNode`

`self.children_dict`:
the key is an character, the value is a corresponding child node


`self.suffix_idx`: 
This will be non-negative for leaves and will give index of suffix for the path from root to this leaf. 
For non-leaf node, it will be -1.

- For `InEdgeLabel`

`self.start_idx`:
start idx, which is a value type

`self.end_idx_ref`:
end idx, which is a reference type

- [suffix_tree.py](suffix_tree.py)


###Questions

[geeksforgeeks suffix tree tutorial link](http://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-6/)


> This data structure will answer to the required queries quickly as below:

> How to check if a node is root ? — Root is a special node, with no parent and so it’s start and end will be -1, for all other nodes, start and end indices will be non-negative.

> How to check if a node is internal or leaf node ? — suffixIndex will help here. It will be -1 for internal node and non-negative for leaf nodes.

> What is the length of path label on some edge? — Each edge will have start and end indices and length of path label will be end-start+1

> What is the path label on some edge ? — If string is S, then path label will be substring of S from start index to end index inclusive, [start, end].

> How to check if there is an outgoing edge for a given character c from a node A ? — If A->children[c] is not NULL, there is a path, if NULL, no path.

> What is the character value on an edge at some given distance d from a node A ? — Character at distance d from node A will be S[A->start + d], where S is the string.

> Where an internal node is pointing via suffix link ? — Node A will point to A->suffixLink

> What is the suffix index on a path from root to leaf ? — If leaf node is A on the path, then suffix index on that path will be A->suffixIndex


##Z-Algorithm
- text and pattern

```python
pat = 'aba'
txt = 'bbabaxababay'
```

- [z_algorithm.py](z_algorithm.py)

- output

```zsh
naive: [2, 6, 8]
z algorithm: [2, 6, 8]
```