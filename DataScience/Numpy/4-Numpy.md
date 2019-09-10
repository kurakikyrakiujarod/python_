
### 数组类型


```python
import numpy as np
```


```python
tang_array = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print(tang_array.dtype)
print(tang_array.nbytes)
```

    float32
    20
    


```python
tang_array = np.array([1, 10, 3, 5.1, 'str'], dtype=np.object)
print(tang_array)
print(tang_array * 2)
```

    [1 10 3 5.1 'str']
    [2 20 6 10.2 'strstr']
    


```python
tang_array = np.array([1, 2, 3, 4, 5])
print(np.asarray(tang_array, dtype=np.float32))
print(tang_array)
```

    [1. 2. 3. 4. 5.]
    [1 2 3 4 5]
    


```python
print(tang_array.astype(np.float32))
```

    [1. 2. 3. 4. 5.]
    [1 2 3 4 5]
    

### 数值计算


```python
tang_array = np.array([[1, 2, 3],
                       [4, 5, 6]])

```


```python
print(np.sum(tang_array))
```

    21
    


```python
print(tang_array.sum())
```

    21
    


```python
print(np.sum(tang_array, axis=0))
```

    [5 7 9]
    


```python
print(np.sum(tang_array, axis=1))
```

    [ 6 15]
    


```python
print(np.sum(tang_array, axis=1))
```

    [ 6 15]
    


```python
print(tang_array.sum(axis=0))
```

    [5 7 9]
    


```python
print(tang_array.sum(axis=1))
```

    [ 6 15]
    


```python
print(tang_array.sum(axis=-1))
```

    [ 6 15]
    


```python
print(tang_array.prod())
```

    720
    


```python
print(tang_array.prod(axis=0))
```

    [ 4 10 18]
    


```python
print(tang_array.prod(axis=1))
```

    [  6 120]
    


```python
print(tang_array.prod(axis=-1))
```

    [  6 120]
    


```python
print(tang_array.min())
```

    1
    


```python
print(tang_array.min(axis=0))
```

    [1 2 3]
    


```python
print(tang_array.min(axis=1))
```

    [1 4]
    


```python
print(tang_array.min(axis=-1))
```

    [1 4]
    


```python
print(tang_array.max())
```

    6
    


```python
print(tang_array.argmin())
```

    0
    


```python
print(tang_array.argmin(axis=0))
```

    [0 0 0]
    


```python
print(tang_array.argmin(axis=1))
```

    [0 0]
    


```python
print(tang_array.mean())
```

    3.5
    


```python
print(tang_array.mean(axis=0))
```

    [2.5 3.5 4.5]
    


```python
print(tang_array.mean(axis=1))
```

    [2. 5.]
    


```python
# std标准差
print(tang_array.std())
print(tang_array.std(axis=1))
```

    1.707825127659933
    [0.81649658 0.81649658]
    


```python
# 方差
print(tang_array.var())
print(tang_array.var(axis=1))
```

    2.9166666666666665
    [0.66666667 0.66666667]
    


```python
print(tang_array.clip(2, 4))
```

    [[2 2 3]
     [4 4 4]]
    


```python
tang_array = np.array([1.2, 3.334, 2.2222,
                       2.1121, 3.222, 3.356])

print(tang_array.round())
print(tang_array.round(decimals=1))
```

    [1. 3. 2. 2. 3. 3.]
    [1.2 3.3 2.2 2.1 3.2 3.4]
    

### 数组形状


```python
tang_array = np.arange(10)
print(tang_array)
```

    [0 1 2 3 4 5 6 7 8 9]
    


```python
print(tang_array.shape)
```

    (10,)
    


```python
tang_array.shape = 2, 5
print(tang_array)
```

    [[0 1 2 3 4]
     [5 6 7 8 9]]
    


```python
print(tang_array.reshape(1, 10))
```

    [[0 1 2 3 4 5 6 7 8 9]]
    


```python
tang_array = np.arange(10)
print(tang_array.shape)
```

    (10,)
    


```python
tang_array = tang_array[:, np.newaxis]
print(tang_array)
print(tang_array.shape)
```

    [[0]
     [1]
     [2]
     [3]
     [4]
     [5]
     [6]
     [7]
     [8]
     [9]]
    (10, 1)
    


```python
tang_array = tang_array[:, np.newaxis, np.newaxis]
# print(tang_array)
print(tang_array.shape)
```

    (10, 1, 1, 1)
    


```python
tang_array = tang_array.squeeze()
print(tang_array)
print(tang_array.shape)
```

    [0 1 2 3 4 5 6 7 8 9]
    (10,)
    


```python
tang_array.shape = 2, 5
print(tang_array)
```

    [[0 1 2 3 4]
     [5 6 7 8 9]]
    


```python
print(tang_array.transpose())
```

    [[0 5]
     [1 6]
     [2 7]
     [3 8]
     [4 9]]
    


```python
print(tang_array.T)
```

    [[0 5]
     [1 6]
     [2 7]
     [3 8]
     [4 9]]
    


```python
print(tang_array)
```

    [[0 1 2 3 4]
     [5 6 7 8 9]]
    

### 数组的连接


```python
a = np.array([[123, 456, 789], [321, 432, 654]])
print(a)
```

    [[123 456 789]
     [321 432 654]]
    


```python
b = np.array([[1234, 4526, 9], [31, 42, 65]])
print(b)
```

    [[1234 4526    9]
     [  31   42   65]]
    


```python
c = np.concatenate((a, b))
print(c)
```

    [[ 123  456  789]
     [ 321  432  654]
     [1234 4526    9]
     [  31   42   65]]
    


```python
c = np.concatenate((a, b), axis=0)
print(c)
```

    [[ 123  456  789]
     [ 321  432  654]
     [1234 4526    9]
     [  31   42   65]]
    


```python
c = np.concatenate((a, b), axis=1)
print(c)
print(c.shape)
```

    [[ 123  456  789 1234 4526    9]
     [ 321  432  654   31   42   65]]
    (2, 6)
    


```python
print(np.vstack((a, b)))
```

    [[ 123  456  789]
     [ 321  432  654]
     [1234 4526    9]
     [  31   42   65]]
    


```python
print(np.hstack((a, b)))
```

    [[ 123  456  789 1234 4526    9]
     [ 321  432  654   31   42   65]]
    


```python
print(a)
```

    [[123 456 789]
     [321 432 654]]
    


```python
print(a.flatten())
```

    [123 456 789 321 432 654]
    


```python
print(a.ravel())
```

    [123 456 789 321 432 654]
    
