
打印当前Numpy版本


```python
import numpy as np
print(np.__version__)
```

    1.14.2
    

构造一个全零的矩阵，并打印其占用的内存大小


```python
z = np.zeros((5,5))
print("%d bytes"%(z.size * z.itemsize))
```

    8
    200 bytes
    

打印一个函数的帮助文档，比如numpy.add


```python
# print(help(np.info(np.add)))
```

创建一个10-49的数组，并将其倒序排列


```python
tang_array = np.arange(10,50,1)
tang_array = tang_array[::-1]
print(tang_array)
```

    [49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26
     25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10]
    

找到一个数组中不为0的索引


```python
print(np.nonzero([1,2,3,0,0,0,3,11,2,0,0,0,19]))
```

    (array([ 0,  1,  2,  6,  7,  8, 12], dtype=int64),)
    

随机构造一个3*3矩阵，并打印其中最大与最小值


```python
tang_array = np.random.random((3*3))
print(tang_array.min())
print(tang_array.max())
```

    0.08248771043540448
    0.9789060539073025
    

构造一个5*5的矩阵，令其值都为1，并在最外层加上一圈0


```python
tang_array = np.ones((5,5))
tang_array = np.pad(tang_array,pad_width=1, mode='constant', constant_values=0)
print(tang_array)
```

    [[0. 0. 0. 0. 0. 0. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 0. 0. 0. 0. 0. 0.]]
    


```python
# print(help(np.pad))
```

构建一个shape为（6，7，8）的矩阵，并找到第100个元素的索引值


```python
print(np.unravel_index(100,(6,7,8)))
```

    (1, 5, 4)
    

对一个5*5的矩阵做归一化操作


```python
tang_array = np.random.random((5,5))
tang_max = tang_array.max()
tang_min = tang_array.min()
# tang_array = (tang_array-tang_min)/(tang_max-tang_array)
# print(tang_array)
```

找到两个数组中相同的值


```python
z1 = np.random.randint(0,10,10)
z2 = np.random.randint(0,10,10)
print(z1)
print(z2)
print(np.intersect1d(z1,z2))
```

    [9 3 6 8 9 7 8 7 4 8]
    [6 7 9 2 5 5 2 2 1 2]
    [6 7 9]
    

得到今天明天昨天的日期


```python
today = np.datetime64('today','D')
yesterday = today - np.timedelta64(1,'D')
tomorrow = today + np.timedelta64(1,'D')
print(today)
print(yesterday)
print(tomorrow)
```

    2019-05-16
    2019-05-15
    2019-05-17
    

得到一个月中所有的天


```python
print(np.arange('2017-10','2017-11',dtype='datetime64[D]'))
```

    ['2017-10-01' '2017-10-02' '2017-10-03' '2017-10-04' '2017-10-05'
     '2017-10-06' '2017-10-07' '2017-10-08' '2017-10-09' '2017-10-10'
     '2017-10-11' '2017-10-12' '2017-10-13' '2017-10-14' '2017-10-15'
     '2017-10-16' '2017-10-17' '2017-10-18' '2017-10-19' '2017-10-20'
     '2017-10-21' '2017-10-22' '2017-10-23' '2017-10-24' '2017-10-25'
     '2017-10-26' '2017-10-27' '2017-10-28' '2017-10-29' '2017-10-30'
     '2017-10-31']
    

得到一个数的整数部分


```python
z = np.random.uniform(0,10,10)
print(np.floor(z))
```

    [1. 0. 9. 4. 3. 8. 0. 5. 2. 2.]
    

构造一个数组，让它不能被改变


```python
z = np.zeros(5)
z.flags.writeable = False
```

打印大数据的部分值，全部值


```python
np.set_printoptions(threshold=5)
# np.set_printoptions(threshold=np.nan)
z = np.zeros((15,15))
print(z)
```

    [[0. 0. 0. ... 0. 0. 0.]
     [0. 0. 0. ... 0. 0. 0.]
     [0. 0. 0. ... 0. 0. 0.]
     ...
     [0. 0. 0. ... 0. 0. 0.]
     [0. 0. 0. ... 0. 0. 0.]
     [0. 0. 0. ... 0. 0. 0.]]
    

找到在一个数组中，最接近一个数的索引


```python
z = np.arange(100)
v = np.random.uniform(0,100)
print(v)
index = (np.abs(z-v)).argmin()
print(z[index])
```

    51.679941671708484
    52
    

32位float类型和32位int类型转换


```python
z = np.arange(10,dtype=np.int32)
print(z.dtype)
z = z.astype(np.float32)
print(z.dtype)
```

    int32
    float32
    

打印数组元素位置坐标与数值


```python
z = np.arange(9).reshape(3,3)
for index,value in np.ndenumerate(z):
    print(index,value)
```

    (0, 0) 0
    (0, 1) 1
    (0, 2) 2
    (1, 0) 3
    (1, 1) 4
    (1, 2) 5
    (2, 0) 6
    (2, 1) 7
    (2, 2) 8
    

按照数组的某一列进行排序


```python
z = np.random.randint(0,10,(3,3))
print(z)
print(z[z[:,1].argsort()])
```

    [[3 6 8]
     [1 5 1]
     [8 4 6]]
    [[8 4 6]
     [1 5 1]
     [3 6 8]]
    

统计数组中每个数值出现的次数


```python
z = np.array([1,1,2,2,3,4,5,6,7,8,9,0,0])
print(np.bincount(z))
```

    [2 2 2 ... 1 1 1]
    

如何对一个四维数组的最后两维来求和


```python
z = np.random.randint(0,10,(4,4,4,4))
print(z.sum(axis=(-2,-1)))
```

    [[76 66 65 90]
     [67 80 88 85]
     [80 51 74 79]
     [63 61 62 71]]
    

交换矩阵中的两行


```python
z = np.arange(25).reshape(5,5)
print(z)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]
     [20 21 22 23 24]]
    


```python
z[[0,1]] = z[[1,0]]
print(z)
```

    [[ 5  6  7  8  9]
     [ 0  1  2  3  4]
     [10 11 12 13 14]
     [15 16 17 18 19]
     [20 21 22 23 24]]
    

找到一个数组中最常出现的数字


```python
z = np.random.randint(0,10,50)
print(np.bincount(z).argmax())
```

    4
    

快速查找TOP K


```python
z = np.arange(10000)
np.random.shuffle(z)
n = 5
print(z[np.argpartition(-z,n)][:n])
```




    array([9999, 9998, 9995, ..., 4143, 4546, 1724])



去除掉一个数组中，所有元素都相同的数据


```python
a = np.array([1,2,3,4])
b = np.array([1,2,3,5])
print(np.all(a==b))
print(np.any(a==b))
```

    False
    True
    


```python
z = np.random.randint(0,3,(10,3))
print(z)
```

    [[1 2 2]
     [1 2 0]
     [2 2 0]
     ...
     [2 1 1]
     [0 0 2]
     [2 2 2]]
    


```python
print(np.all(z[:,1:] == z[:,:-1],axis=1))
```

    [False False False ... False False  True]
    
