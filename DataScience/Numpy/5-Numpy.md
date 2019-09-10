
### 常用数组生成函数


```python
import numpy as np
```


```python
print(np.zeros(3))
```

    [0. 0. 0.]
    


```python
print(np.zeros((3, 3)))
```

    [[0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]]
    


```python
print(np.ones((3, 3)) * 8)
```

    [[8. 8. 8.]
     [8. 8. 8.]
     [8. 8. 8.]]
    


```python
print(np.ones((3, 3), dtype=np.float32))
```

    [[1. 1. 1.]
     [1. 1. 1.]
     [1. 1. 1.]]
    


```python
a = np.empty(6)
print(a)
```

    [0. 0. 0. 0. 0. 0.]
    


```python
print(a.shape)
```

    (6,)
    


```python
a.fill(1)
print(a)
```

    [1. 1. 1. 1. 1. 1.]
    


```python
tang_array = np.array([1, 2, 3])
print(np.zeros_like(tang_array))
print(np.ones_like(tang_array))
```

    [0 0 0]
    [1 1 1]
    


```python
print(np.identity(5))
```

    [[1. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0.]
     [0. 0. 1. 0. 0.]
     [0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 1.]]
    

### 运算


```python
import numpy as np
```


```python
x = np.array([5, 5])
y = np.array([2, 2])
```


```python
print(np.multiply(x, y))
```

    [10 10]
    


```python
print(np.dot(x, y))
```

    20
    


```python
x.shape = 2, 1
print(x)
```

    [[5]
     [5]]
    


```python
y.shape = 1, 2
print(x.shape, y.shape)
```

    (2, 1) (1, 2)
    


```python
print(np.dot(x, y))
print(np.dot(y, x))
```

    [[10 10]
     [10 10]]
    [[20]]
    


```python
x = np.array([1, 1, 1])
y = np.array([[1, 2, 3], [4, 5, 6]])
```


```python
print(x * y)
```

    [[1 2 3]
     [4 5 6]]
    


```python
x = np.array([1, 1, 1])
y = np.array([1, 1, 1])
print(x == y)
```

    [ True  True  True]
    


```python
print(np.logical_and(x, y))
print(np.logical_or(x, y))
print(np.logical_not(x, y))
```

    [ True  True  True]
    [ True  True  True]
    [0 0 0]
    
