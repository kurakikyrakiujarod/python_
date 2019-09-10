

```python
import numpy as np
```


```python
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(array)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    


```python
print(array.ndim)  # 维度
print(array.shape)  # 形状
print(array.size)  # 大小
print(array.dtype)  # 元素类型
```

    2
    (3, 3)
    9
    int32
    


```python
# dtype 指定数据类型
a = np.array([1, 2, 3], dtype=np.int64)
print(a.dtype)
```

    int64
    


```python
b = np.array([1, 2, 3], dtype=np.float)
print(b.dtype)
```

    float64
    


```python
# 一维数据
c = np.array([1, 2, 3])
print(c)
```

    [1 2 3]
    


```python
# 二维矩阵
d = np.array([[1, 2, 3],
              [4, 5, 6]])
print(d)
```

    [[1 2 3]
     [4 5 6]]
    


```python
# 生成2行3列全为0的矩阵
zero = np.zeros((2, 3))
print(zero)
```

    [[0. 0. 0.]
     [0. 0. 0.]]
    


```python
# 生成3行4到全为1的矩阵
one = np.ones((3, 4))
print(one)
```

    [[1. 1. 1. 1.]
     [1. 1. 1. 1.]
     [1. 1. 1. 1.]]
    


```python
# 生成3行2列全都接近于0（不等于0）的矩阵
empty = np.empty((3, 2))
print(empty)
```

    [[0. 0.]
     [0. 0.]
     [0. 0.]]
    


```python
e = np.arange(10)
print(e)
```

    [0 1 2 3 4 5 6 7 8 9]
    


```python
f = np.arange(4, 12)
print(f)
```

    [ 4  5  6  7  8  9 10 11]
    


```python
g = np.arange(1, 20, 3)
print(g)
```

    [ 1  4  7 10 13 16 19]
    


```python
# 重新定义矩阵的形状
h = np.arange(8).reshape(2, 4)
print(h)
```

    [[0 1 2 3]
     [4 5 6 7]]
    

### 矩阵的运算


```python
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
arr2 = np.array([[1, 1, 2],
                 [2, 3, 3]])
```


```python
print(arr1)
print(arr2)
```

    [[1 2 3]
     [4 5 6]]
    [[1 1 2]
     [2 3 3]]
    


```python
print(arr1 + arr2)
```

    [[2 3 5]
     [6 8 9]]
    


```python
print(arr1 - arr2)
```

    [[0 1 1]
     [2 2 3]]
    


```python
print(arr1 * arr2)
```

    [[ 1  2  6]
     [ 8 15 18]]
    


```python
print(arr1 ** arr2)
```

    [[  1   2   9]
     [ 16 125 216]]
    


```python
print(arr1 / arr2)
```

    [[1.         2.         1.5       ]
     [2.         1.66666667 2.        ]]
    


```python
print(arr1 % arr2)
```

    [[0 0 1]
     [0 2 0]]
    


```python
print(arr1 // arr2)
```

    [[1 2 1]
     [2 1 2]]
    


```python
print(arr1 + 2)  # 所有的元素加2
```

    [[3 4 5]
     [6 7 8]]
    


```python
print(arr1 * 10)  # 所有的元素乘以10
```

    [[10 20 30]
     [40 50 60]]
    


```python
arr3 = arr1 > 3  # 判断哪些元素大于3
```


```python
print(arr3)
```

    [[False False False]
     [ True  True  True]]
    


```python
arr4 = np.ones((3, 5))
print(arr4)
```

    [[1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1.]]
    


```python
print(np.dot(arr1, arr4))  # 矩阵乘法
```

    [[ 6.  6.  6.  6.  6.]
     [15. 15. 15. 15. 15.]]
    


```python
print(arr1.dot(arr4))  # 矩阵乘法
```

    [[ 6.  6.  6.  6.  6.]
     [15. 15. 15. 15. 15.]]
    


```python
print(arr1)
```

    [[1 2 3]
     [4 5 6]]
    


```python
print(arr1.T)  # 矩阵转置
print(np.transpose(arr1))  # 矩阵转置
```

    [[1 4]
     [2 5]
     [3 6]]
    [[1 4]
     [2 5]
     [3 6]]
    

### 随机数生成


```python
sample1 = np.random.random((3, 2))  # 生成3行2列从0到1的随机数
print(sample1)
```

    [[0.63107187 0.65661147]
     [0.88437882 0.62980709]
     [0.86877985 0.08838303]]
    


```python
sample2 = np.random.normal(size=(3, 2))  # 生成3行2列符合标准正态分布的随机数
print(sample2)
```

    [[ 1.40018815  0.92163669]
     [-0.4193311   1.15665203]
     [-2.4505489  -0.73538839]]
    


```python
sample3 = np.random.randint(0, 10, size=(3, 2))  # 生成3行2列从0到10的随机整数
print(sample3)
```

    [[8 6]
     [4 3]
     [7 3]]
    


```python
print(np.sum(sample1))  # 求和
```

    3.759032129554169
    


```python
print(np.min(sample1))  # 求最小值
```

    0.08838303084610333
    


```python
print(np.max(sample1))  # 求最大值
```

    0.8843788199030156
    


```python
print(np.sum(sample1, axis=0))  # 对列求和
```

    [2.38423054 1.37480159]
    


```python
print(np.sum(sample1, axis=1))  # 对行求和
```

    [1.28768334 1.51418591 0.95716288]
    


```python
print(np.argmin(sample1))  # 求最小值的索引
print(np.argmax(sample1))  # 求最大值的索引
```

    5
    2
    


```python
print(np.mean(sample1))  # 求平均值
print(sample1.mean())  # 求平均值
```

    0.6265053549256948
    0.6265053549256948
    


```python
print(np.median(sample1))  # 求中位数
```

    0.6438416683319266
    


```python
print(np.sqrt(sample1))  # 开方
```

    [[0.79440032 0.81031566]
     [0.94041417 0.79360386]
     [0.93208361 0.29729284]]
    


```python
sample4 = np.random.randint(0, 10, size=(1, 10))
print(sample4)
```

    [[1 1 0 7 7 1 9 7 6 4]]
    


```python
print(np.sort(sample4))  # 排序
```

    [[0 1 1 1 4 6 7 7 7 9]]
    


```python
print(np.sort(sample1))
```

    [[0.63107187 0.65661147]
     [0.62980709 0.88437882]
     [0.08838303 0.86877985]]
    


```python
print(np.clip(sample4, 2, 7))  # 小于2就变成2，大于7就变为7
```

    [[2 2 2 7 7 2 7 7 6 4]]
    

### numpy的索引


```python
arr1 = np.arange(2, 14)
```


```python
print(arr1)
```

    [ 2  3  4  5  6  7  8  9 10 11 12 13]
    


```python
print(arr1[2])  # 第二个位置的数据
```

    4
    


```python
print(arr1[1:4])  # 第一到第四个位置的数据
```

    [3 4 5]
    


```python
print(arr1[2:-1])  # 第二到倒数第一个位置的数据
```

    [ 4  5  6  7  8  9 10 11 12]
    


```python
print(arr1[:5])  # 前五个数据
```

    [2 3 4 5 6]
    


```python
print(arr1[-2:])  # 最后两个数据
```

    [12 13]
    


```python
arr2 = arr1.reshape(3, 4)
```


```python
print(arr2)
```

    [[ 2  3  4  5]
     [ 6  7  8  9]
     [10 11 12 13]]
    


```python
print(arr2[1])
```

    [6 7 8 9]
    


```python
print(arr2[1][1])
```

    7
    


```python
print(arr2[1, 2])
```

    8
    


```python
print(arr2[:, 2])
```

    [ 4  8 12]
    


```python
for i in arr2:  # 迭代行
    print(i)
```

    [2 3 4 5]
    [6 7 8 9]
    [10 11 12 13]
    


```python
for i in arr2.T:  # 迭代列
    print(i)
```

    [ 2  6 10]
    [ 3  7 11]
    [ 4  8 12]
    [ 5  9 13]
    


```python
for i in arr2.flat:  # 一个一个元素迭代
    print(i)
```

    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    
