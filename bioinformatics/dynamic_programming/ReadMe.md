#Explanation
##First: Fibonacci

we can use matrix fast pow to compute that.

see [fibonacci.py](fibonacci.py)

##Second: max sum sub arr

I reduce the problem into another one though doing prefix sum computation first.

see [max_sum_sub_arr.py](max_sum_sub_arr.py)

- input 

```zsh
[1, -2, 3, 10, -4, 7, 2, -5]
```

- output

```zsh
input list: [1, -2, 3, 10, -4, 7, 2, -5]
scan list: [0, 1, -1, 2, 12, 8, 15, 17, 12]
differ: 18
sub arr input list lower idx: 2 value: 3
sub arr input list upper idx: 6 value: 2
sub arr: [3, 10, -4, 7, 2]

```

##Third: max len incremental sub arr

see [max_len_incre_sub_arr.py](max_len_incre_sub_arr.py)

- input 

```zsh
[7, 2, 3, 1, 5, 8, 9, 6]
```

- output

```zsh
max incre count: 5 

root-1                                            
 |_2                                              
   |_3                                            
     |_5                                          
       |_8                                        
         |_9           

```

##Fourth

skip

##Fifth

see [min_sum_path.py](min_sum_path.py)

- input weight matrix

```zsh
matrix = [[1, 2, 9], [3, 4, 8], [5, 6, 7]]
```

- output

```zsh
root[(2, 2)]                                       (3, 3)
 |_[(2, 1)]                                        (2, 2) weight: 7 min sum: 20
   |_[(1, 1)]                                      (2, 1) weight: 6 min sum: 13
     |_[(0, 1)]                                    (1, 1) weight: 4 min sum: 7
       |_[(0, 0)]                                  (0, 1) weight: 2 min sum: 3
         |_None                                    (0, 0) weight: 1 min sum: 1
min sum:20

```