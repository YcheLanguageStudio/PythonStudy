#Find Euler Path Algorithm
##Algorithm Input

- [read_list.txt](read_list.txt)

- content as follows

```zsh
AGT
AAA
ACT
AAC
CTT
GTA
TTT
TAA
```

##Python Script

- [find_euler_path.py](find_euler_path.py), where [read_list.txt](read_list.txt) is read in the execution of script

- execution with python 2.7 as follows

```zsh
python find_euler_path.py
```

##Algorithm Output

```zsh
read list: ['AGT', 'AAA', 'ACT', 'AAC', 'CTT', 'GTA', 'TTT', 'TAA']
vertex list: ['AA', 'AC', 'GT', 'AG', 'TT', 'TA', 'CT'] 

connected component: [('AA', 'AA'), ('AA', 'AC'), ('AC', 'CT'), ('GT', 'TA'), ('AG', 'GT'), ('TT', 'TT'), ('TT', 'AG'), ('CT', 'TT'), ('TA', 'AA')]

find v with unvisited out edges,  expand from vertex: AA local path: ['AA', 'AA']
find v with unvisited out edges,  expand from vertex: AA local path: ['AA', 'AC', 'CT', 'TT', 'TT', 'AG', 'GT', 'TA', 'AA']

added extra edge: ('TT', 'AG') 
euler cycle: ['AA', 'AC', 'CT', 'TT', 'TT', 'AG', 'GT', 'TA', 'AA', 'AA']
euler path: ['AG', 'GT', 'TA', 'AA', 'AA', 'AC', 'CT', 'TT', 'TT']
super str: AGTAAACTTT
```