#Crypto Homework Notes
##Euclidean Algorithm For greatest common divider(gcd)
```python
def gcd_euclidean(lhs, rhs):
    if rhs == 0:
        return lhs
    else:
        return gcd_euclidean(rhs, lhs % rhs)
```

##Extended Euclidean Algorithm