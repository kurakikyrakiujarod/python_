

```python
import numpy as np
```


```python
tang_array = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
```


```python
print(tang_array)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    


```python
print(tang_array.shape)
```

    (3, 3)
    


```python
print(tang_array.size)
```

    9
    


```python
print(tang_array.ndim)
```

    2
    


```python
print(tang_array[1, 1])
```

    5
    


```python
tang_array[1, 1] = 50
print(tang_array)
```

    [[ 1  2  3]
     [ 4 50  6]
     [ 7  8  9]]
    


```python
print(tang_array[1])
```

    [ 4 50  6]
    


```python
print(tang_array[:, 1])
```

    [ 2 50  8]
    


```python
print(tang_array[0, 0:2])
```

    [1 2]
    


```python
tang_array = np.arange(0, 100, 10)
print(tang_array)
```

    [ 0 10 20 30 40 50 60 70 80 90]
    


```python
mask = np.array([0, 0, 0, 1, 1, 1, 0, 0, 0, 1], dtype=bool)
print(mask)
```

    [False False False  True  True  True False False False  True]
    


```python
print(tang_array[mask])
```

    [30 40 50 90]
    


```python
random_array = np.random.rand(10)
print(random_array)
```

    [0.91191123 0.33709687 0.76458396 0.41975946 0.21459646 0.83833011
     0.72517067 0.32968367 0.98318312 0.63378133]
    


```python
mask = random_array > 0.5
print(mask)
```

    [False False  True False  True  True False False False  True]
    


```python
print(random_array[mask])
```

    [0.96354512 0.56409341 0.77245364 0.63003959]
    


```python
tang_array = np.array([10, 20, 30, 40, 50])
print(np.where(tang_array > 30))
```

    (array([3, 4], dtype=int64),)
    
