
### array合并


```python
import numpy as np
```


```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
```


```python
arr3 = np.vstack((arr1, arr2))  # 垂直合并
print(arr3)
print(arr3.shape)
```

    [[1 2 3]
     [4 5 6]]
    (2, 3)
    


```python
arr4 = np.hstack((arr1, arr2))  # 水平合并
print(arr4)
print(arr4.shape)
```

    [1 2 3 4 5 6]
    (6,)
    


```python
arrv = np.vstack((arr1, arr2, arr3))
print(arrv)
```

    [[1 2 3]
     [4 5 6]
     [1 2 3]
     [4 5 6]]
    


```python
arrh = np.hstack((arr1, arr2, arr4))
print(arrh)
```

    [1 2 3 4 5 6 1 2 3 4 5 6]
    


```python
arr = np.concatenate((arr1, arr2, arr1))
print(arr)
```

    [1 2 3 4 5 6 1 2 3]
    


```python
arr = np.concatenate((arr3, arrv), axis=0)  # 合并的array维度要相同，array形状要匹配，axis=0纵向合并
print(arr)
```

    [[1 2 3]
     [4 5 6]
     [1 2 3]
     [4 5 6]
     [1 2 3]
     [4 5 6]]
    


```python
arr = np.concatenate((arr3, arr3), axis=1)  # 合并的array维度要相同，array形状要匹配，axis=1横向合并
print(arr)
```

    [[1 2 3 1 2 3]
     [4 5 6 4 5 6]]
    


```python
print(arr1.T)  # 一维的array不能转置
```

    [1 2 3]
    


```python
print(arr1.shape)
```

    (3,)
    


```python
arr1_1 = arr1[np.newaxis, :]
print(arr1_1)
print(arr1_1.shape)
```

    [[1 2 3]]
    (1, 3)
    


```python
print(arr1_1.T)
```

    [[1]
     [2]
     [3]]
    


```python
arr1_2 = arr1[:, np.newaxis]
print(arr1_2)
print(arr1_2.shape)
```

    [[1]
     [2]
     [3]]
    (3, 1)
    


```python
arr1_3 = np.atleast_2d(arr1)
print(arr1_3)
print(arr1_3.T)
```

    [[1 2 3]]
    [[1]
     [2]
     [3]]
    

### array分割


```python
arr1 = np.arange(12).reshape((3, 4))
print(arr1)
```

    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    


```python
arr2, arr3 = np.split(arr1, 2, axis=1)  # 水平方向分割，分成2份
print(arr2)
print(arr3)
```

    [[0 1]
     [4 5]
     [8 9]]
    [[ 2  3]
     [ 6  7]
     [10 11]]
    


```python
arr4, arr5, arr6 = np.split(arr1, 3, axis=0)  # 垂直方向分割，分成3份
print(arr4)
print(arr5)
print(arr6)
```

    [[0 1 2 3]]
    [[4 5 6 7]]
    [[ 8  9 10 11]]
    


```python
# arr2, arr3, arr4 = np.split(arr1, 3, axis=1)  # 水平方向分割，分成3份
# print(arr2)
# print(arr3)
# print(arr4)
```


```python
arr7, arr8, arr9 = np.array_split(arr1, 3, axis=1)  # 水平方向分割，分成3份，不等分割
print(arr7)
print(arr8)
print(arr9)
```

    [[0 1]
     [4 5]
     [8 9]]
    [[ 2]
     [ 6]
     [10]]
    [[ 3]
     [ 7]
     [11]]
    


```python
arrv1, arrv2, arrv3 = np.vsplit(arr1, 3)  # 垂直分割
print(arrv1)
print(arrv2)
print(arrv3)
```

    [[0 1 2 3]]
    [[4 5 6 7]]
    [[ 8  9 10 11]]
    


```python
arrh1, arrh2 = np.hsplit(arr1, 2)  # 水平分割
print(arrh1)
print(arrh2)
```

    [[0 1]
     [4 5]
     [8 9]]
    [[ 2  3]
     [ 6  7]
     [10 11]]
    

### numpy的浅拷贝和深拷贝


```python
arr1 = np.array([1, 2, 3])

arr2 = arr1  # arr1,arr2共享一块内存，浅拷贝
```


```python
arr2[0] = 5
print(arr1)
print(arr2)
```

    [5 2 3]
    [5 2 3]
    


```python
arr3 = arr1.copy()  # 深拷贝

arr3[0] = 10
print(arr1)
print(arr3)
```

    [5 2 3]
    [10  2  3]
    


```python
# 对于ndarray结构来说，里面所有的元素必须是同一类型的如果不是的话，会自动的向下进行转换
```


```python
tang_list = [1, 2, 3, 4, 5.0]
tang_array = np.array(tang_list)
```


```python
print(tang_array)
print(type(tang_array))
```

    [1. 2. 3. 4. 5.]
    <class 'numpy.ndarray'>
    


```python
print(tang_array.dtype)
```

    float64
    


```python
print(tang_array.itemsize)
```

    8
    


```python
print(tang_array.shape)
```

    (5,)
    


```python
print(np.shape(tang_array))
```

    (5,)
    


```python
print(np.size(tang_array))
```

    5
    


```python
print(tang_array.ndim)
```

    1
    


```python
tang_array.fill(0)
print(tang_array)
```

    [0. 0. 0. 0. 0.]
    
