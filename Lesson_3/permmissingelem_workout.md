```python
def solution(A):
    length = len(A)
    xor_sum = 0
    for index in range(0, length):
        xor_sum = xor_sum ^ A[index] ^ (index + 1)
    return xor_sum^(length + 1)
```
Work through code line by line

e.g.

A = [2,3,1,5]

length = 4

xor_sum = 0

### Going through the loop
```
index = 0
xor_sum = xor_sum ^ A[index] ^ (index + 1) 
        = 0 ^ 2 ^ 1
        = 3
```
```
index = 1
xor_sum = xor_sum ^ A[index] ^ (index + 1)
        = 3 ^ 3 ^ 2
        = 2
```
```
index = 2
xor_sum = xor_sum ^ A[index] ^ (index + 1)
        = (2 ^ 1) ^ 3
        = 3 ^ 3
        = 0
```
```
index = 3
xor_sum = xor_sum ^ A[index] ^ (index + 1)
        = 0 ^ 5 ^ 4
        = 1
```

### Final calculation

```
  xor_sum ^ (length+1)
= 1 ^ (4+1)
= 1 ^ 5
= 4
```
