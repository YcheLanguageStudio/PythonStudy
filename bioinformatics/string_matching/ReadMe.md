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